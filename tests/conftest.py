import csv
import pytest

from src.cli.command_argparse import ArgparseCommandParser
from src.readers.csv_reader import CsvReader
from tests.constants import (
    DEVELOPERS_DATA_1,
    DEVELOPERS_DATA_2,
    FIELDNAMES
)


@pytest.fixture
def create_csv_file(tmp_path):
    def _create_csv_file(
        filename: str,
        fieldnames: list[str],
        rows: list[dict],
    ) -> str:
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
def two_valid_csv_files(create_csv_file):
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
def csv_reader():
    return CsvReader()


@pytest.fixture
def command_argparse():
    return ArgparseCommandParser()
