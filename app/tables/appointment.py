# Table appointment

import datetime


class Appointment():
    def __init__(self, appointment_ID, date, startTime, endtime, type, status, employee_username, patient_username, invoice_ID):
        self.appointment_ID = appointment_ID
        self.date = date
        self.startTime = startTime
        self.endtime = endtime
        self.type = type
        self.status = status
        self.employee_username = employee_username
        self.patient_username = patient_username
        self.invoice_ID = invoice_ID


def create_table_appointment():
    appointment_table = """CREATE TABLE IF NOT EXISTS appointment (
	appointment_ID INT NOT NULL AUTO_INCREMENT,
	date DATE NOT NULL,
	startTime TIME NOT NULL,
	endtime TIME NOT NULL,
	type VARCHAR(120) NOT NULL,
	status VARCHAR(60) NOT NULL,
	employee_username VARCHAR(120) NOT NULL,
	patient_username VARCHAR(120) NOT NULL,
	invoice_ID INT NOT NULL,
	PRIMARY KEY (appointment_ID, employee_username, patient_username, invoice_ID),
	INDEX fk_appointment_user (employee_username ASC) VISIBLE,
	INDEX fk_appointment_user2 (patient_username ASC) VISIBLE,
	INDEX fk_appointment_invoice (invoice_ID ASC) VISIBLE,
	CONSTRAINT fk_appointment_user
		FOREIGN KEY (employee_username)
		REFERENCES user (username)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION,
	CONSTRAINT fk_appointment_user2
		FOREIGN KEY (patient_username)
		REFERENCES user (username)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION,
	CONSTRAINT fk_appointment_invoice
		FOREIGN KEY (invoice_ID)
		REFERENCES invoice (invoice_ID)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION);
    """

    return appointment_table


def insert_into_appointment(appointment_ID, date, startTime, endtime, type, status, employee_username, patient_username, invoice_ID, connection):

    sql_appointment_query = "INSERT INTO appointment (date, startTime, endtime, type, status, employee_username, patient_username, invoice_ID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

    val = (date, startTime, endtime,
           type, status, employee_username, patient_username, invoice_ID)

    cursor = connection.cursor()
    cursor.execute(sql_appointment_query, val)
    connection.commit()
    cursor.close()


def fill_appointment(connection):
    for i in range(10):
        insert_into_appointment(i, (datetime.datetime.now() + datetime.timedelta(days=1)), (datetime.datetime.now() + datetime.timedelta(days=1)).time(),
                                (datetime.datetime.now() + datetime.timedelta(days=1)).time(), "carries", "", f"employee{i}", f"patient{i}", i, connection)
    insert_into_appointment(0, datetime.date.today(), datetime.datetime.now().time(),
                                    datetime.datetime.now().time(), "carries", "Not completed", f"test2", f"test", i, connection)

    insert_into_appointment(0, datetime.datetime.now() - datetime.timedelta(1), datetime.datetime.now().time(),
                                    datetime.datetime.now().time(), "carries", "Completed", f"test2", f"test", i, connection)

def getUpcomingAppointment(employee_username, connection):
    sql = "select * from appointment WHERE employee_username = %s AND date >= %s"
    val = (employee_username, datetime.date.today())

    cursor = connection.cursor()
    cursor.execute(sql, val)
    appointment = cursor.fetchall()

    lst_appointment = []

    for row in appointment:
        lst_appointment.append(Appointment(
            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))

    return lst_appointment


def getUpcomingAppointmentPatient(patient_username, connection):
    sql = "select * from appointment WHERE patient_username = %s AND date >= %s"
    val = (patient_username, datetime.date.today())

    cursor = connection.cursor()
    cursor.execute(sql, val)
    appointment = cursor.fetchall()

    lst_appointment = []

    for row in appointment:
        lst_appointment.append(Appointment(
            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))

    return lst_appointment


def getAllAppointmentPatient(patient_username, connection):
    sql = "select * from appointment WHERE patient_username = %s"
    val = ([patient_username])

    cursor = connection.cursor()
    cursor.execute(sql, val)
    appointment = cursor.fetchall()

    lst_appointment = []

    for row in appointment:
        lst_appointment.append(Appointment(
            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))

    return lst_appointment
