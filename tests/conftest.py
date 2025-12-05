import csv
from pathlib import Path
import pytest
from typing import Callable, Iterable
from unittest.mock import Mock

from src.app.application_service import ApplicationService
from src.cli.command_argparse import ArgparseCommandParser
from src.core.constants import PERFORMANCE
from src.core.data_models import CliOptions, DeveloperRecord
from src.readers.csv_reader import CsvReader
from src.renderers.console_renderer import ConsoleRenderer
from src.reports.performance_report import PerformanceReport
from src.reports.registry import ReportRegistry
from tests.constants import (
    DEVELOPERS_DATA_1,
    DEVELOPERS_DATA_2,
    FIELDNAMES
)


# --- Фикстуры csv файлов и ридера --- #


@pytest.fixture
def create_csv_file(
    tmp_path: Path
) -> Callable[[str, list[str], list[dict]], Path]:
    def _create_csv_file(
        filename: str,
        fieldnames: list[str],
        rows: list[dict],
    ) -> Path:
        file_path = tmp_path / filename
        with open(
            file_path,
            'w',
            newline='',
            encoding='utf-8-sig'
        ) as f:
            writer = csv.DictWriter(
                f,
                fieldnames=fieldnames
            )
            writer.writeheader()
            for row in rows:
                writer.writerow(row)
        return file_path
    return _create_csv_file


@pytest.fixture
def two_valid_csv_files(create_csv_file) -> list[Path]:
    file_1 = create_csv_file(
        filename='valid_developers_1.csv',
        fieldnames=FIELDNAMES,
        rows=DEVELOPERS_DATA_1
    )
    file_2 = create_csv_file(
        filename='valid_developers_2.csv',
        fieldnames=FIELDNAMES,
        rows=DEVELOPERS_DATA_2
    )
    return [file_1, file_2]


@pytest.fixture
def csv_reader() -> CsvReader:
    return CsvReader()


# --- Фикстуры для парсеров командной строки --- #


@pytest.fixture
def command_argparse() -> ArgparseCommandParser:
    return ArgparseCommandParser()


# -- Фикстуры для оркестратора ApplicationService и его зависимостей --- #


@pytest.fixture
def app_service_dependencies() -> dict:
    command_parser = Mock(spec=ArgparseCommandParser)
    reader = Mock()
    report_registry = Mock()
    report_handler = Mock()
    renderer = Mock()

    command_parser.parse.return_value = CliOptions(
        report=PERFORMANCE,
        files=['mock.csv']
    )
    reader.read.return_value = ['mock_record']
    report_registry.get_report_handler.return_value = report_handler
    report_handler.generate.return_value = 'mock_report'
    renderer.render.return_value = None
    application_service = ApplicationService(
        command_parser=command_parser,
        reader=reader,
        renderer=renderer,
        report_registry=report_registry
    )
    return {
        'application_service': application_service,
        'command_parser': command_parser,
        'reader': reader,
        'report_registry': report_registry,
        'report_handler': report_handler,
        'renderer': renderer
    }


# --- Фикстуры для реестра отчетов и обработчиков отчетов --- #


@pytest.fixture
def incorrect_developer_record() -> Iterable[DeveloperRecord]:
    yield DeveloperRecord(
        name='Incorrect',
        position='',
        completed_tasks=0,
        performance=None,
        skills=[],
        team='',
        experience_years='1'
    )


@pytest.fixture
def report_registry() -> ReportRegistry:
    registry = ReportRegistry()
    registry.register(
        name=PERFORMANCE,
        report_handler=PerformanceReport
    )
    return registry


@pytest.fixture
def performance_report_handler(
    report_registry: ReportRegistry
) -> PerformanceReport:
    return report_registry.get_report_handler(
        name=PERFORMANCE
    )


# --- Фикстуры для компонента вывода --- #
@pytest.fixture
def console_renderer() -> ConsoleRenderer:
    return ConsoleRenderer()