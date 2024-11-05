import psycopg2

try:
    conn = psycopg2.connect(
        "host=localhost dbname=mydatabase user=postgres password=password"
    )
except psycopg2.Error as e:
    print("Error: cound not make connection to db")

try:
    cur = conn.cursor()
except psycopg2.Error as e:
    print(e)

conn.set_session(autocommit=True)

try:
    cur.execute("CREATE DATABASE mydatabase")
except psycopg2.Error as e:
    print(e)


try:
    cur.execute(
        "CREATE TABLE IF NOT EXISTS students (student_id int, name varchar, age int, gender varchar, subject varchar, marks int);"
    )
except psycopg2.Error as e:
    print(e)

try:
    cur.execute(
        "INSERT INTO students (student_id, name, age, gender, subject, marks) VALUES (%s, %s, %s, %s, %s, %s)",
        (1, "Abhi", 28, "Male", "Python", 85),
    )
except psycopg2.Error as e:
    print(e)

try:
    cur.execute(
        "INSERT INTO students (student_id, name, age, gender, subject, marks) VALUES (%s, %s, %s, %s, %s, %s)",
        (2, "Thom", 34, "Male", "Python", 86),
    )
except psycopg2.Error as e:
    print(e)

try:
    cur.execute("SELECT * FROM students;")
except psycopg2.Error as e:
    print(e)

row = cur.fetchone()
while row:
    print(row)
    row = cur.fetchone()

cur.close()
conn.close()