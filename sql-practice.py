import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()
cursor.execute("""SELECT courses.course_name, AVG(students.grade)
FROM students
JOIN courses ON students.id = courses.student_id 
GROUP BY courses.course_name""")
conn.commit()
print(cursor.fetchall())