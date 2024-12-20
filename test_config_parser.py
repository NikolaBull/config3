import os
import subprocess
import xml.etree.ElementTree as ET

def run_test(input_file, expected_output_file, output_file):
    """Запуск теста и сравнение результатов."""
    # Запускаем скрипт config_parser.py
    subprocess.run([
        "python", "config_parser.py", input_file, output_file
    ])

    # Сравниваем с ожидаемым файлом
    with open(expected_output_file, "r", encoding="utf-8") as expected_file:
        expected_content = expected_file.read()

    with open(output_file, "r", encoding="utf-8") as output_file:
        output_content = output_file.read()

    assert expected_content == output_content, (
        f"Тест не пройден.\nОжидаемое:\n{expected_content}\n\nПолученное:\n{output_content}"
    )

    print(f"Тест для {input_file} пройден.")

if __name__ == "__main__":
    # Пути к тестовым файлам
    test_cases = [
        {
            "input": "config-serv.txt",
            "expected_output": "output_serv.xml",
            "output": "test_output_serv.xml"
        },
        {
            "input": "config-calc.txt",
            "expected_output": "output_calc.xml",
            "output": "test_output_calc.xml"
        },
        {
            "input": "config-db.txt",
            "expected_output": "output_db.xml",
            "output": "test_output_db.xml"
        }
    ]

    # Запускаем тесты
    for case in test_cases:
        run_test(case["input"], case["expected_output"], case["output"])

    print("Все тесты пройдены.")
