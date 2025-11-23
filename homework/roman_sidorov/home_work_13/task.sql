INSERT INTO students (name, second_name) values ('Yan', 'Bobrov')

INSERT INTO books (title, taken_by_student_id) 
VALUES ('War and world', 21700), ('Stupid', 21700), ('Harry Poter', 21700)

INSERT INTO `groups` (title, start_date, end_date) 
VALUES ('AQA', 'now 2025', 'feb 2026')

UPDATE students s SET group_id = 21553
Where s.id = 21700

INSERT INTO subjects (title) 
VALUES ('OOP'), ('DB'), ('SQL')

INSERT INTO lessons  (title, subject_id) 
VALUES ('task1_OOP', 12834), ('task2_OOP', 12834), ('task1_DB', 12835), ('task2_DB', 12835), ('task1_SQL', 12836), ('task2_SQL', 12836)

INSERT INTO marks (value,lesson_id,student_id) 
VALUES ('3', 73302, 21700), ('3', 73303, 21700), ('4', 73304, 21700), ('4', 73305, 21700), ('5', 73306, 21700), ('5', 73307, 21700)

SELECT m.value 
FROM marks m 
where m.student_id = 21700

SELECT b.title
from books b 
where b.taken_by_student_id = 21700

SELECT g.title, b.title, m.value, l.title, s2.title
from students s 
join books b on s.id = b.taken_by_student_id
join marks m on m.student_id = s.id
join `groups` g on g.id = s.group_id
join lessons l on m.lesson_id = l.id
join subjects s2 on l.subject_id = s2.id
where s.id = 21700