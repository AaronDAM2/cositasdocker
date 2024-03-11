# mysql.py
import pymysql

def create_database(conn, cursor):
    cursor.execute("CREATE DATABASE test_db")

def insert_data(conn, cursor):
    sql = "INSERT INTO test_table (name, age) VALUES (%s, %s)"
    values = [
        ("John", 25),
        ("Jane", 30),
        ("Jim", 35),
        ("Joan", 40),
    ]
    cursor.executemany(sql, values)
    conn.commit()

def update_data(conn, cursor):
    sql = "UPDATE test_table SET age = 28 WHERE name = 'John'"
    cursor.execute(sql)
    conn.commit()

def delete_data(conn, cursor):
    sql = "DELETE FROM test_table WHERE name = 'Jane'"
    cursor.execute(sql)
    conn.commit()

def destroy_data(conn, cursor):
    cursor.execute("DROP TABLE test_table")
    cursor.execute("DROP DATABASE test_db")

def main():
    conn = pymysql.connect(
        host="localhost",
        user="admin",
        password="adminpass",
        database="test_db"
    )
    cursor = conn.cursor()

    create_database(conn, cursor)
    cursor.execute("USE test_db")
    cursor.execute("CREATE TABLE test_table (name VARCHAR(255), age INT)")
    insert_data(conn, cursor)
    update_data(conn, cursor)
    delete_data(conn, cursor)
    destroy_data(conn, cursor)

    conn.close()

if __name__ == "__main__":
    main()
