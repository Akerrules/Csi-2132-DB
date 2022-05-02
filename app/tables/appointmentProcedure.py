# Table appointmentprocedure

import datetime


def create_table_appointmentprocedure():
    appointmentProcedure_table = """CREATE TABLE IF NOT EXISTS appointmentprocedure (
	appointmentProcedure_ID INT NOT NULL,
	date DATE NOT NULL,
	procedureType VARCHAR(120) NOT NULL,
	appointment_ID INT NOT NULL,
	PRIMARY KEY (appointmentProcedure_ID, appointment_ID),
	INDEX fk_appointmentprocedure_appointment (appointment_ID ASC) VISIBLE,
	CONSTRAINT fk_appointmentprocedure_appointment
		FOREIGN KEY (appointment_ID)
		REFERENCES appointment (appointment_ID)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION);
    """

    return appointmentProcedure_table


def insert_into_appointmentprocedure(appointmentProcedure_ID, date, procedureType, appointment_ID, connection):

    sql_appointmentprocedure_query = "INSERT INTO appointmentprocedure (appointmentProcedure_ID, date, procedureType, appointment_ID) VALUES (%s, %s, %s, %s)"

    val = (appointmentProcedure_ID, date, procedureType, appointment_ID)

    cursor = connection.cursor()
    cursor.execute(sql_appointmentprocedure_query, val)
    connection.commit()
    cursor.close()


def fill_appointmentprocedure(connection):
    for i in range(5):
        insert_into_appointmentprocedure(
            i, (datetime.datetime.now() + datetime.timedelta(days=1)), "Procedure", i+1, connection);

    for x in range(5,10):
        insert_into_appointmentprocedure(
            x, (datetime.datetime.now() + datetime.timedelta(days=2) ), "Surgery", x+1, connection)






