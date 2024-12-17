import sys
import xml.etree.ElementTree as ET
from xml.dom import minidom
from evaluator import parse_expression as eval_prefix

def parse_expression(expression, context):
    """
    Вычисляет значение выражений: строки, числа и префиксные выражения.
    """
    expression = expression.strip()
    if expression.startswith("'") and expression.endswith("'"):  # Строки
        return expression[1:-1]  # Убираем кавычки
    elif expression.startswith("$") and expression.endswith("$"):  # Префиксные выражения
        expression = expression[1:-1]  # Убираем $ с начала и конца
        # Подставляем значения переменных из контекста
        for var, value in context.items():
            expression = expression.replace(var, str(value))
        try:
            return eval_prefix(expression)  # Используем парсер префиксной формы
        except Exception as e:
            raise ValueError(f"Ошибка в выражении '{expression}': {str(e)}")
    else:  # Числа
        try:
            return float(expression)
        except ValueError:
            raise ValueError(f"Невозможно преобразовать '{expression}' в число.")

def parse_line(line):
    """
    Парсит строку конфигурации.
    """
    line = line.strip()
    if "is" in line:  # Объявление константы
        name, value = line.split(" is ")
        return ("const", name.strip(), value.strip(";").strip())
    elif "->" in line:  # Ключ-значение
        name, value = line.split(" -> ")
        return ("key_value", name.strip(), value.strip(";").strip())
    return ("unknown",)

def parse_file(input_file_path):
    """
    Чтение файла конфигурации.
    """
    with open(input_file_path, "r", encoding="utf-8") as f:
        return f.readlines()

def process_file(input_file_path, output_file_path):
    """
    Обрабатывает входной файл и генерирует выходной XML файл.
    """
    lines = parse_file(input_file_path)
    root = ET.Element("config")
    context = {}  # Словарь для хранения значений переменных

    for line in lines:
        try:
            result = parse_line(line)
            if result[0] == "const":
                name, value = result[1], result[2]
                evaluated_value = parse_expression(value, context)  # Вычисляем значение
                context[name] = evaluated_value  # Добавляем в контекст
                const_element = ET.SubElement(root, "constant", name=name)
                const_element.text = str(evaluated_value)
            elif result[0] == "key_value":
                key, value = result[1], result[2]
                evaluated_value = parse_expression(value, context)  # Вычисляем значение
                key_value_element = ET.SubElement(root, "key_value", name=key)
                key_value_element.text = str(evaluated_value)
        except Exception as e:
            print(f"Ошибка в строке '{line}': {str(e)}")

    # Преобразуем XML в читаемый формат
    xml_str = ET.tostring(root, 'utf-8')
    parsed_xml = minidom.parseString(xml_str)
    pretty_xml_str = parsed_xml.toprettyxml(indent="  ")

    # Записываем результат в файл
    with open(output_file_path, "w", encoding="utf-8") as f:
        f.write(pretty_xml_str)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: python config_parser.py <входной файл> <выходной файл>")
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    process_file(input_file_path, output_file_path)
    print(f"Конфигурация успешно преобразована в XML файл: {output_file_path}")
