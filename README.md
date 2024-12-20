# Конфигурационный инструмент

Этот инструмент командной строки предназначен для преобразования текстов конфигурационных файлов, написанных на учебном конфигурационном языке, в формат XML. Он выполняет синтаксический анализ, вычисление константных выражений и генерирует XML-выход на основе входных данных.

## Описание

Инструмент позволяет:

- Преобразовывать текст конфигурации, записанный на учебном конфигурационном языке, в формат XML.
- Вычислять константные выражения, написанные в префиксной форме.
- Поддерживает операции сложения и функцию `abs()`.
- Обрабатывать сложные структуры данных, такие как словари (name -> value), и поддерживает различные типы значений (числа, строки, словари).
- Выявлять синтаксические ошибки в конфигурационных файлах и сообщать об этом пользователю.

## Особенности
Поддержка вложенных словарей.
Поддержка вычислений на этапе трансляции (в префиксной форме).
Возможность работы с различными типами значений: числа, строки, словари.
Простота использования через командную строку.
Выявление и вывод ошибок синтаксиса при неправильном формате входного файла.
Требования
Python 3.7+.
Для запуска требуется наличие файлов конфигурации в формате учебного конфигурационного языка и файл для вывода результата в формате XML.
Возможность работы с командной строкой.
## Установка
Склонируйте репозиторий или скачайте исходный код.
git clone <ссылка_на_репозиторий>
cd <папка_проекта>
## Установите зависимости:
pip install -r requirements.txt
## Запуск
Для запуска инструмента используйте следующую команду:

python config_tool.py --input <путь_к_входному_файлу> --output <путь_к_выходному_файлу>
--input — путь к входному файлу в формате учебного конфигурационного языка.
--output — путь к выходному XML файлу.
## Пример:
python config_parser.py config-db.txt output_db.xml
## Тесты
![](image.png)
