import re

# Регулярные выражения для парсинга
name_regex = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
number_regex = r'^\d+(\.\d+)?$'
string_regex = r"^'([^']*)'$"
dict_start_regex = r'^\{'
dict_end_regex = r'^\}$'

def parse_line(line):
    """Парсит строку конфигурационного языка."""
    line = line.strip()
    
    # Обработка объявления константы
    const_decl_match = re.match(r'(\w+) is (.+);', line)
    if const_decl_match:
        name = const_decl_match.group(1)
        value = const_decl_match.group(2)
        return ("const", name, value)
    
    # Обработка словаря
    if line.startswith("{") and line.endswith("}"):
        return ("dict", line)
    
    # Обработка имени -> значение
    key_value_match = re.match(r'(\w+) -> (.+);', line)
    if key_value_match:
        key = key_value_match.group(1)
        value = key_value_match.group(2)
        return ("key_value", key, value)
    
    raise ValueError(f"Синтаксическая ошибка в строке: {line}")

def parse_file(input_file_path):
    """Считывает и обрабатывает строки конфигурационного файла."""
    with open(input_file_path, 'r') as infile:
        return infile.readlines()
