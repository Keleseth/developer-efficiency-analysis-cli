from collections import defaultdict
from typing import Iterable

from src.core.constants import (
    PERFORMANCE_REPORT_FIELDS,
    PERFORMANCE_REPORT_TITLE,
)
from src.core.data_models import DeveloperRecord, ReportData


class PerformanceReport:
    """
    Отчет представляющий среднюю эффективность разработчиков по должностям.
    """

    def generate(
        self,
        records: Iterable[DeveloperRecord]
    ) -> ReportData:
        """
        Получает поток записей Iterable[DeveloperRecord], вычисляет среднюю
        эффективность по каждой должности и возвращает результат ReportData.
        """
        totals = defaultdict(float)
        counts = defaultdict(int)
        for record in records:
            totals[record.position] += record.performance
            counts[record.position] += 1
        rows = [
            [
                position,
                round(totals[position] / counts[position], 2)
            ] # Округляем для нормализации до передачи в класс вывода.
            for position in totals
        ]
        rows.sort(key=lambda elem: elem[1], reverse=True)
        indexed_rows = [[i, *row] for i, row in enumerate(rows, 1)]
        return ReportData(
            title=PERFORMANCE_REPORT_TITLE,
            headers=PERFORMANCE_REPORT_FIELDS,
            rows=indexed_rows,
        )
