import argparse
from typing import Sequence

from src.core.data_models import CliOptions


class ArgparseCommandParser:
    """
    Реализация протокола CommandParserProtocol с использованием 
    библиотеки argparse.
    """

    def parse(
        self,
        args: Sequence[str]
    ) -> CliOptions:
        parser = argparse.ArgumentParser(
            description='Отчет по данным разработчиков.'
        )
        parser.add_argument(
            '-f',
            '--files',
            required=True,
            nargs='+',
            help='Путь к файлу/файлам с данными.'
        )
        parser.add_argument(
            '-r',
            '--report',
            type=str,
            required=True,
            help='Тип отчета.'
        )
        parsed_args = parser.parse_args(args)
        return CliOptions(
            files=parsed_args.files,
            report=parsed_args.report
        )
