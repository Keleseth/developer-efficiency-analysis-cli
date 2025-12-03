from tabulate import tabulate

from src.core.data_models import ReportData


class ConsoleRenderer:
    """
    Реалзиация протокола RendererProtocol для консольного вывода отчета
    с использованием библиотеки tabulate.
    """

    def render(
        self,
        data_to_render: ReportData
    ) -> None:
        if data_to_render.title:
            print(data_to_render.title)
        print(tabulate(
            data_to_render.rows,
            headers=data_to_render.headers,
            tablefmt='grid',
            floatfmt='.2f',
            )
        )
