# Данные для CSV фикстур
FIELDNAMES = [
    'name',
    'position',
    'completed_tasks',
    'performance',
    'skills',
    'team',
    'experience_years',
]

DEVELOPERS_DATA_1 = [
    {
        'name': 'Alex Ivanov',
        'position': 'Backend Developer',
        'completed_tasks': '45',
        'performance': '4.8',
        'skills': 'Python, Django, PostgreSQL, Docker',
        'team': 'API Team',
        'experience_years': '5',
    },
    {
        'name': 'Maria Petrova',
        'position': 'Frontend Developer',
        'completed_tasks': '38',
        'performance': '4.7',
        'skills': 'React, TypeScript, Redux, CSS',
        'team': 'Web Team',
        'experience_years': '4',
    },
]
DEVELOPERS_DATA_2 = [
    {
        'name': 'Collapse',
        'position': 'offlane',
        'completed_tasks': '10000',
        'performance': '4.8',
        'skills': 'COLLLAPSE',
        'team': 'Team Spirit',
        'experience_years': '3',
    },
    {} # Пустая запись для проверки пропуска пустых строк
]
TOTAL_RECORDS = len(DEVELOPERS_DATA_1) + len(DEVELOPERS_DATA_2) - 1

# Ожидаемые флаги командной строки
REPORT_FLAG = '--report'
FILES_FLAG = '--files'
VALID_ARGS = [REPORT_FLAG, 'performance', FILES_FLAG, 'first.csv', 'second.csv']
VALID_PARSED_ARGS = {
    'report': 'performance',
    'files': ['first.csv', 'second.csv']
}
