"""
Главный модуль приложения.

application_service - Оркестровый класс, управляющий процессом
чтения данных, генерации отчетов и их отображения. Принимает компоненты -
реализации протоколов:
    command_parser: Компонент для парсинга аргументов командной строки.
    reader: Компонент для чтения данных из файлов.
    renderer: Компонент для отображения отчетов.
    report_registry: Реестр доступных отчетов.
application_service.run - точка входа (запуск процесса формирования отчета).
P.S. command_parser: CommandParserProtocol ожидает аргументы командной строки
в виде списка строк, передаваемых через параметр args метода run для удобства
тестирования и подмены компонента на другие реализации при необходимости.
"""

import sys

from src.app.application_service import ApplicationService
from src.reports.registry import report_register
from src.cli.command_argparse import ArgparseCommandParser
from src.readers.csv_reader import CsvReader
from src.renderers.console_renderer import ConsoleRenderer


def main():
    args = sys.argv[1:]
    application_service = ApplicationService(
        command_parser=ArgparseCommandParser(),
        reader=CsvReader(),
        renderer=ConsoleRenderer(),
        report_registry=report_register
    )
    try:
        application_service.run(args=args)
    except ValueError as error:
        print(f'Ошибка при формировании отчета: {error}')
    except FileNotFoundError as error:
        print(str(error))

if __name__ == '__main__':
    main()
