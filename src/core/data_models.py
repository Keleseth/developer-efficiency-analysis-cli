from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class CliOptions:
    """
    Хранилище нормализованных, введённых пользователем опций командной строки.
    Используется парсером для передачи параметров дальше по приложению.

    Атрибуты:
        report: тип отчёта.
        files: пути к файлам со входными данными.
    """

    report: str
    files: list[str]


@dataclass(frozen=True, slots=True)
class DeveloperRecord:
    """
    Хранилище, содержащее нормализованные данные о разработчике
    считанные из входных файлов.

    Атрибуты соответствуют колонкам входных данных.
    """

    name: str
    position: str
    completed_tasks: int
    performance: float
    skills: list[str]
    team: str
    experience_years: int


@dataclass(frozen=True, slots=True)
class ReportData:
    """
    Отчет готовый для вывода.

    Атрибуты:
        title: заголовок отчёта(если есть).
        headers: заголовки столбцов отчета.
        rows: строки данных: уже рассчитанные значения, готовые для вывода.
    """

    headers: list[str]
    rows: list[list[str | int | float]]
    title: str | None = None
