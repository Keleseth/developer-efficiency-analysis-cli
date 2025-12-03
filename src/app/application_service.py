from typing import TYPE_CHECKING, Sequence

if TYPE_CHECKING:
    from src.core.contracts import (
        CommandParserProtocol,
        ReaderProtocol,
        RendererProtocol
    )
    from src.core.data_models import CliOptions
    from src.reports.registry import ReportRegistry


class ApplicationService:
    """
    Класс - оркестратор работы приложения. Собирает вместе компоненты
    приложения и управляет их взаимодействием.

    Атрибуты:
        command_parser: Компонент для парсинга аргументов командной строки.
        reader: Компонент для чтения и нормализации входных данных.
        renderer: Компонент для отображения отчётов.
        report_registry: Реестр зарегистрированных генераторов отчётов.
    """

    def __init__(
        self,
        command_parser: 'CommandParserProtocol',
        reader: 'ReaderProtocol',
        renderer: 'RendererProtocol',
        report_registry: 'ReportRegistry'
    ) -> None:
        self.command_parser = command_parser
        self.reader = reader
        self.renderer = renderer
        self.report_registry = report_registry

    def run(
        self,
        args: Sequence[str]
    ) -> None:
        """
        Точка входа для запуска процесса формирования отчёта. Ожидает
        аргументы командной строки в виде последовательности строк.
        """
        cli_options: CliOptions = self.command_parser.parse(
            args=args
        )
        developers_records = self.reader.read(
            paths=cli_options.files or []
        )
        report_handler = self.report_registry.get_report_handler(
            name=cli_options.report
        )
        data_to_render = report_handler.generate(
            records=developers_records
        )
        self.renderer.render(
            data_to_render=data_to_render
        )
