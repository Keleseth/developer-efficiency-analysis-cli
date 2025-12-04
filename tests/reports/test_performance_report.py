from src.core.constants import (
    PERFORMANCE_REPORT_FIELDS,
    PERFORMANCE_REPORT_TITLE
)
from src.core.data_models import (
    DeveloperRecord,
    ReportData
)


def developer_record_factory(
    position: str,
    performance: float
):
    return DeveloperRecord(
        name='stub',
        position=position,
        completed_tasks=0,
        performance=performance,
        skills=['stub'],
        team='stub',
        experience_years=0
    )


def test_generate_creates_correct_report(
    performance_report_handler,
):
    records = [
        developer_record_factory('Backend', 4.5),
        developer_record_factory('Backend', 4.5),
        developer_record_factory('Frontend', 5.0),
    ]
    report_data = performance_report_handler.generate(records=records)

    assert isinstance(report_data, ReportData)
    assert len(report_data.rows) == 2  # 3 разработчика, но 2 должности
    assert report_data.title == PERFORMANCE_REPORT_TITLE
    assert report_data.headers == PERFORMANCE_REPORT_FIELDS
    assert report_data.rows == [
        [1, 'Frontend', 5.0],
        [2, 'Backend', 4.5],
    ]


def test_generate_handles_empty_data(
    performance_report_handler
):
    report_data = performance_report_handler.generate([])
    assert report_data.rows == []
