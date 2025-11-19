import os
import re
from datetime import datetime, timedelta


my_path = os.path.dirname(__file__)
base_path = os.path.dirname(os.path.dirname(my_path))
e_okulik_path = os.path.join(base_path, 'eugene_okulik', "hw_13", 'data.txt')


def reading_file_line():
    with open(e_okulik_path, 'r') as okulik_txt:
        for line in okulik_txt:
            yield line.strip()


def operation_line(line, line_number):
    date_pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6})'
    match = re.search(date_pattern, line)
    date_str = match.group(1)
    date = datetime.fromisoformat(date_str)


    if line_number == 1:
        result = date + timedelta(weeks=1)
        print(f"1. {result}")
    elif line_number == 2:
        result = date.strftime('%A')
        print(f"2. {result}")
    elif line_number == 3:
        days_ago = (datetime.now() - date).days
        print(f"3. {days_ago}")


for i, line in enumerate(reading_file_line(), start=1):
    operation_line(line, i)
