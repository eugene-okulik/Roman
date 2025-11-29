import csv
import dotenv
import mysql.connector as mysql
import os

dotenv.load_dotenv(override=True)

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor()
cursor.execute('''
SELECT s.name, s.second_name, g.title, b.title,  s2.title, l.title, m.value
FROM students s
JOIN books b ON s.id = b.taken_by_student_id
JOIN marks m ON m.student_id = s.id
JOIN `groups` g ON g.id = s.group_id
JOIN lessons l ON m.lesson_id = l.id
JOIN subjects s2 ON l.subject_id = s2.id
''')

base = cursor.fetchall()
setbase = {
    (name.strip(), second_name.strip(), group_title.strip(), book_title.strip(),
     subject_title.strip(), lesson_title.strip(), mark_value.strip())
    for name, second_name, group_title, book_title, subject_title, lesson_title, mark_value in base
}
data = []

with open(r"C:\Users\User\PycharmProjects\Roman\homework\eugene_okulik\Lesson_16\hw_data\data.csv", newline='') as file:
    data_file = csv.DictReader(file)
    for row in data_file:
        name_f = row.get('name', '')
        second_name_f = row.get('second_name', '').strip()
        group_title_f = row.get('group_title', '').strip()
        book_title_f = row.get('book_title', '').strip()
        subject_title_f = row.get('subject_title', '').strip()
        lesson_title_f = row.get('lesson_title', '').strip()
        mark_value_f = row.get('mark_value', '').strip()
        val = (
            name_f, second_name_f, group_title_f, book_title_f,
            subject_title_f, lesson_title_f, mark_value_f
        )
        if val not in setbase:
            data.append(val)

for student in data:
    print(student)
