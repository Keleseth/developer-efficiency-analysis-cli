from typing import (
    Iterable,
    Protocol,
    Sequence,
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from src.core.data_models import (
        CliOptions,
        DeveloperRecord,
        ReportData
    )


class CommandParserProtocol(Protocol):
    """
    Протокол парсера командной строки.

    Метод parse принимает уже подготовленную последовательность аргументов
    (например, sys.argv[1:]). Самостоятельного чтения sys.argv не выполняет.
    """

    def parse(
        self,
        args: Sequence[str]
    ) -> 'CliOptions':
        """
        Парсит аргументы содержащиеся в args и возвращает
        экземпляр CliOptions.
        """
        pass


class ReaderProtocol(Protocol):
    """
    Протокол для чтения и нормализации входных данных.
    """

    def read(
        self,
        paths: Sequence[str]
    ) -> 'Iterable[DeveloperRecord]':
        """
        Читает и нормализует записи из файлов, указанных в paths.
        Возвращает итератор нормализованных записей DeveloperRecord.
        """
        pass


class ReportProtocol(Protocol):
    """
    Протокол отчёта.

    Получает поток нормализованных записей DeveloperRecord, выполняет расчёты и
    возвращает результат для отображения ReportData.
    """

    def generate(
        self,
        records: Iterable['DeveloperRecord']
    ) -> 'ReportData':
        pass


class RendererProtocol(Protocol):
    """
    Протокол вывода результата отчёта.
    """

    def render(
        self,
        data_to_render: 'ReportData'
    ) -> None:
        pass
