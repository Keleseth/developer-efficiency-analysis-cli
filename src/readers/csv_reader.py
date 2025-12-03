from csv import DictReader
from typing import (
    Iterator,
    Sequence
)

from src.core.constants import (
    COMPLETED_TASKS,
    EXPERIENCE_YEARS,
    NAME,
    PERFORMANCE,
    POSITION,
    SKILLS,
    TEAM
)
from src.core.data_models import DeveloperRecord
from src.readers.utils import safe_float, safe_int


class CsvReader:
    """
    Реализация протокола ReaderProtocol для чтения CSV файлов.
    """ 

    def read(
        self,
        paths: Sequence[str]
    ) -> Iterator[DeveloperRecord]:
        """
        Принимает список путей к CSV файлам, читает и возвращает
        генератор нормализованных записей DeveloperRecord.
        """
        for path in paths:
            try:
                with open(
                    path, mode='r', newline='', encoding='utf-8-sig'
                ) as file:
                    reader = DictReader(file)
                    for row in reader:
                        if not any(row.values()):
                            continue
                        developer_skills = row.get(SKILLS, '')
                        yield DeveloperRecord(
                            name=row.get(NAME, '').strip(),
                            position=row.get(POSITION, '').strip(),
                            completed_tasks=safe_int(
                                row.get(COMPLETED_TASKS, '0').strip()
                            ),
                            performance=safe_float(
                                row.get(PERFORMANCE, '0.00').strip()
                            ),
                            skills=[
                                skill.strip()
                                for skill in developer_skills.split(',')
                                if skill.strip()
                            ],
                            team=row.get(TEAM, '').strip(),
                            experience_years=safe_int(
                                row.get(EXPERIENCE_YEARS, '0').strip()
                            ),
                        )
            except FileNotFoundError as error:
                raise FileNotFoundError(f'Файл не найден: {path}') from error
