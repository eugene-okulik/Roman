import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

student = [
    ('Yanchik', 'Bobr')
]
for name, second_name in student:
    cursor.execute("INSERT INTO students (name, second_name) values (%s, %s)", (name, second_name))
student_id = cursor.lastrowid
print(f"Студент {student_id}")

books = [
    ('War and world', student_id),
    ('Stupid', student_id),
    ('Harry Poter', student_id)
]
cursor.executemany(
    "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)", books)

cursor.execute('''
INSERT INTO `groups` (title, start_date, end_date)
VALUES ('AQA', 'now 2025', 'feb 2026')
''')
group_id = cursor.lastrowid
print(f"Группа {group_id}")

cursor.execute(
    f"UPDATE students s SET group_id = {group_id} Where s.id = {student_id}"
)

subjects_data = ["OOP", "DB", "SQL"]
subject_ids = []
for title in subjects_data:
    cursor.execute("INSERT INTO subjects (title) VALUES (%s)", (title,))
    subject_ids.append(cursor.lastrowid)
print(f"Предметы {subject_ids}")
subject1, subject2, subject3 = subject_ids

lessons_data = [
    ('task1_OOP', subject1),
    ('task2_OOP', subject1),
    ('task1_DB', subject2),
    ('task2_DB', subject2),
    ('task1_SQL', subject3),
    ('task2_SQL', subject3)
]
lessons_ids = []

for title, subj_id in lessons_data:
    cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)", (title, subj_id))
    lessons_ids.append(cursor.lastrowid)
print(f"Занятия {lessons_ids}")

for lesson_id in lessons_ids:
    batch = [
        (3, lesson_id, student_id)
    ]
    cursor.executemany(
        "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)",
        batch
    )

db.commit()

cursor.execute(f"SELECT value FROM marks WHERE student_id = {student_id}")
print(cursor.fetchall())
cursor.execute(f"SELECT title FROM books WHERE taken_by_student_id = {student_id}")
print(cursor.fetchall())
cursor.execute(f''' 
SELECT g.title, b.title, m.value, l.title, s2.title
FROM students s 
JOIN books b ON s.id = b.taken_by_student_id
JOIN marks m ON m.student_id = s.id
JOIN `groups` g ON g.id = s.group_id
JOIN lessons l ON m.lesson_id = l.id
JOIN subjects s2 ON l.subject_id = s2.id
where s.id = {student_id}
''')
print(cursor.fetchall())

db.close()
