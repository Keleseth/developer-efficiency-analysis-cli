from src.core.constants import (
    PERFORMANCE_REPORT_FIELDS,
    PERFORMANCE_REPORT_TITLE
)
from src.core.data_models import ReportData


def test_console_renderer_outputs_correct_data(
    capsys,
    console_renderer,
):
    data = ReportData(
        title=PERFORMANCE_REPORT_TITLE,
        headers=PERFORMANCE_REPORT_FIELDS,
        rows=[[1, 'Backend', 5.0]],
    )
    console_renderer.render(data)
    captured = capsys.readouterr().out
    assert PERFORMANCE_REPORT_TITLE in captured
    assert 'Backend' in captured
    assert '5.00' in captured