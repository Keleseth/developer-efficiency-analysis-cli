import pytest

from tests.constants import TOTAL_RECORDS
from src.core.data_models import DeveloperRecord

def test_csv_reader_reads_valid_file(
    csv_reader,
    two_valid_csv_files
):
    result = list(csv_reader.read(
        paths=two_valid_csv_files
        )
    )
    assert len(result) == TOTAL_RECORDS
    for record in result:
        assert isinstance(record, DeveloperRecord)
        assert isinstance(record.name, str)
        assert isinstance(record.position, str)
        assert isinstance(record.completed_tasks, int)
        assert isinstance(record.performance, float)
        assert isinstance(record.skills, list)
        assert isinstance(record.team, str)
        assert isinstance(record.experience_years, int)


def test_csv_reader_handles_nonexistent_file(
    csv_reader,
):
    with pytest.raises(FileNotFoundError):
        result = csv_reader.read(paths=['where_is_it.csv'])
        next(result)
