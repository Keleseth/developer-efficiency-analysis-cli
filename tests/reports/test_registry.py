import pytest


class FakeReport:
    pass


@pytest.mark.parametrize(
    'registered_report, requested_report, expected_type, raise_exception',
    [
        ('fake', 'fake', FakeReport, False),
        ('FAKE', 'fake', FakeReport, False),
        (None, "unknown", None, True),
    ]
)
def test_report_registry_behavior(
    report_registry,
    registered_report,
    requested_report,
    expected_type,
    raise_exception
):
    if registered_report is not None:
        report_registry.register(
            name=registered_report,
            report_handler=FakeReport
        )

    if raise_exception:
        with pytest.raises(ValueError):
            report_registry.get_report_handler(
                name=requested_report
            )
    else:
        handler = report_registry.get_report_handler(
            name=requested_report
        )
        assert isinstance(handler, expected_type)
