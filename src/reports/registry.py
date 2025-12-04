from src.core.constants import PERFORMANCE
from src.core.contracts import ReportProtocol
from src.reports.performance_report import PerformanceReport


class ReportRegistry:
    """
    Реестр обработчиков отчётов.

    Позволяет сопоставлять строковое имя отчёта с классом-обработчиком.
    Используется для выбора нужного отчёта по значению параметра --report.
    """

    def __init__(self) -> None:
        self._report_handlers: dict[str, type[ReportProtocol]] = {}

    def register(
        self,
        name: str,
        report_handler: type[ReportProtocol]
    ) -> None:
        """
        Регистрирует обработчик отчёта под указанным именем.

        Параметры:
            name: Имя отчёта, используемое в командной строке.
            report_handler: Класс обработчика отчёта, 
                реализующий протокол ReportProtocol.
        """
        self._report_handlers[name.lower()] = report_handler

    def get_report_handler(
        self,
        name: str | None
    ) -> ReportProtocol:
        """
        Возвращает экземпляр обработчика отчёта по его имени.
        """
        key = (name or '').lower()
        if key not in self._report_handlers:
            raise ValueError(f'Неизвестный тип отчета: {name}')
        return self._report_handlers[key]()


report_registry = ReportRegistry()
report_registry.register(
    name=PERFORMANCE,
    report_handler=PerformanceReport
)
