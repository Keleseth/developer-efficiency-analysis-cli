from src.core.constants import PERFORMANCE
from tests.constants import VALID_ARGS


def test_application_service_run(
    app_service_dependencies
):
    application_service = app_service_dependencies['application_service']
    command_parser = app_service_dependencies['command_parser']
    reader = app_service_dependencies['reader']
    report_registry = app_service_dependencies['report_registry']
    report_handler = app_service_dependencies['report_handler']
    renderer = app_service_dependencies['renderer']

    application_service.run(
        args=VALID_ARGS
    )
    command_parser.parse.assert_called_once_with(
        args=VALID_ARGS
    )
    reader.read.assert_called_once_with(
        paths=['mock.csv']
    )
    report_registry.get_report_handler.assert_called_once_with(name=PERFORMANCE)
    report_handler.generate.assert_called_once_with(
        records=['mock_record']
    )
    renderer.render.assert_called_once_with(
        data_to_render='mock_report'
    )
