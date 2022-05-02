# Table Employee

from random import randrange


def create_table_employee():
    employee_table = """CREATE TABLE IF NOT EXISTS employee (
	SSN VARCHAR(10) NOT NULL,
	lastName VARCHAR(120) NOT NULL,
	firstName VARCHAR(120) NOT NULL,
	street_Num INT NOT NULL,
	street_name VARCHAR(60) NOT NULL,
	apt_number INT NOT NULL,
	city VARCHAR(60) NOT NULL,
	state VARCHAR(60) NOT NULL,
	zip VARCHAR(6) NOT NULL,
	role ENUM('Junior', 'Senior') NOT NULL,
	type ENUM('Assistant', 'Receptionist', 'Dentist') NOT NULL,
	salary DOUBLE NOT NULL,
	branches_ID INT NOT NULL,
	user_username VARCHAR(120) NOT NULL,
	PRIMARY KEY (SSN, branches_ID, user_username),
	INDEX fk_employee_branches (branches_ID ASC) VISIBLE,
	INDEX fk_employee_user (user_username ASC) VISIBLE,
	CONSTRAINT fk_employee_branches
		FOREIGN KEY (branches_ID)
		REFERENCES branches (branches_ID),
	CONSTRAINT fk_employee_user
		FOREIGN KEY (user_username)
		REFERENCES user (username)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION);
    """

    return employee_table


def insert_into_employee(SSN, lastName, firstName, street_Num, street_name,
                         apt_number, city, state, zip, role, type, salary, branches_ID, user_username, connection):

    sql_employee_query = f"INSERT INTO employee (SSN, lastName, firstName, street_Num, street_name, apt_number, city, state, zip, role, type, salary, branches_ID, user_username) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    val = (SSN, lastName, firstName, street_Num, street_name, apt_number,
           city, state, zip, role, type, salary, branches_ID, user_username)

    cursor = connection.cursor()
    cursor.execute(sql_employee_query, val)
    connection.commit()
    cursor.close()


def fill_employee(connection):
	insert_into_employee(-1, "test1", "test1", "000", "street",
					"0", "Ottawa", "Ontario", "00000", "Senior", "Receptionist", "500000", randrange(10), "test1", connection)

	insert_into_employee(-2, "test2", "test2", "000", "street",
					"0", "Ottawa", "Ontario", "00000", "Senior", "Dentist", "500000", randrange(10), "test2", connection)

	insert_into_employee(-3, "test3", "test3", "000", "street",
					"0", "Ottawa", "Ontario", "00000", "Senior", "Dentist", "500000", randrange(10), "test3", connection)

	insert_into_employee(-4, "test4", "test4", "000", "street",
					"0", "Ottawa", "Ontario", "00000", "Junior", "Dentist", "500000", randrange(10), "test4", connection)					

	for i in range(20):
		insert_into_employee(i, f"employee{i}", f"employee{i}", f"00{i}", "street",
                             f"{i}", "Ottawa", "Ontario", f"0000{i}", "Junior", "Assistant", "500000", randrange(10), f"employee{i}", connection)


def getEmployeeNames(connection):
    sql_select = "select user_username from employee"
    cursor = connection.cursor()
    cursor.execute(sql_select)
    employee = cursor.fetchall()

    lst_employee = []

    for row in employee:
        lst_employee.append(row[0])

    return lst_employee
