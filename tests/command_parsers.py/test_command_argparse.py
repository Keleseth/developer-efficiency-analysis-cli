import pytest

from src.core.data_models import CliOptions
from tests.constants import VALID_ARGS, VALID_PARSED_ARGS


def test_argparse_parses_valid_arguments(
    command_argparse,
):
    result: CliOptions = command_argparse.parse(VALID_ARGS)
    assert result.report == VALID_PARSED_ARGS['report']
    assert result.files == VALID_PARSED_ARGS['files']


@pytest.mark.parametrize(
    'missing_args',
    [
        ('--files',),
        ('--report',),
    ]
)
def test_argparse_raises_error_on_missing_arguments(
    command_argparse,
    missing_args
):
    args = [
        arg for arg in VALID_ARGS
        if arg not in missing_args
    ]
    with pytest.raises(SystemExit):
        command_argparse.parse(args)
