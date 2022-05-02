
# Table user
import random


class User():
    def __init__(self, username, type):
        self.username = username
        self.type = type


def create_table_user():
    user_table = """CREATE TABLE IF NOT EXISTS user (
	username VARCHAR(120) NOT NULL,
	type ENUM('Patient', 'Receptionist', 'Dentist', 'Hygienist ') NOT NULL,
	password VARCHAR(120) NOT NULL,
	email VARCHAR(120) NOT NULL,
	PRIMARY KEY (username));
    """

    return user_table


def insert_into_user(username, type, password, email, connection):

    sql_user_query = "INSERT INTO user (username, type, password, email) VALUES (%s, %s, %s, %s)"

    val = (username, type, password, email)

    cursor = connection.cursor()
    cursor.execute(sql_user_query, val)
    connection.commit()
    cursor.close()


def fill_user(connection):
    enum_employee = ["Receptionist", "Dentist", "Hygienist"]

    insert_into_user("test","Patient", "test",
                         "test@user.com", connection)
    insert_into_user("test1","Receptionist", "test",
                         "test1@user.com", connection)
    insert_into_user("test2","Dentist", "test",
                         "test2@user.com", connection)

    insert_into_user("test3","Dentist","test",
                         "test3@user.com", connection)

    insert_into_user("test4","Dentist","test",
                         "test4@user.com", connection)


    for i in range(20):
        rand = int(random.random() * len(enum_employee))
        insert_into_user(f"employee{i}", enum_employee[rand], "pswd",
                         f"employee{i}@user.com", connection)

    for i in range(20):
        insert_into_user(f"patient{i}", "Patient", "pswd",
                         f"patient{i}@user.com", connection)


def check_connection(username, password, connection):
    sql = "select * from user WHERE username = %s AND password = %s"
    val = (username, password)

    cursor = connection.cursor()
    cursor.execute(sql, val)
    branches = cursor.fetchall()

    return len(branches) > 0


def getUser(username, password, connection):
    sql = "select * from user WHERE username = %s AND password = %s"
    val = (username, password)

    cursor = connection.cursor()
    cursor.execute(sql, val)
    branches = cursor.fetchall()

    lst_user = []

    for row in branches:
        lst_user.append(User(row[0], row[1]))

    return lst_user.pop()

def userExist(username, connection):
    sql = "select * from user WHERE username = %s"
    val = [username]

    cursor = connection.cursor()
    cursor.execute(sql, val)
    branches = cursor.fetchall()

    return len(branches)>0
