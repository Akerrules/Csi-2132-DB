# Table tprocedure

def create_table_tprocedure():
    procedure_table = """CREATE TABLE IF NOT EXISTS tprocedure (
	procedure_ID INT NOT NULL,
	price DOUBLE NOT NULL,
	description VARCHAR(120) NOT NULL,
	appointmentProcedure_ID INT NOT NULL,
	feeCharge_ID INT NOT NULL,
	PRIMARY KEY (procedure_ID, appointmentProcedure_ID, feeCharge_ID),
	INDEX fk_tprocedure_appointmentprocedure (appointmentProcedure_ID ASC) VISIBLE,
	INDEX fk_tprocedure_feecharge (feeCharge_ID ASC) VISIBLE,
	CONSTRAINT fk_tprocedure_appointmentprocedure
		FOREIGN KEY (appointmentProcedure_ID)
		REFERENCES appointmentprocedure (appointmentProcedure_ID)
		ON DELETE CASCADE
		ON UPDATE NO ACTION,
	CONSTRAINT fk_tprocedure_feecharge
		FOREIGN KEY (feeCharge_ID)
		REFERENCES feecharge (feeCharge_ID)
		ON DELETE CASCADE
		ON UPDATE NO ACTION);"""

    return procedure_table


def insert_into_tprocedure(procedure_ID, price, description, appointmentProcedure_ID, feeCharge_ID, connection):

    sql_tprocedure_query = "INSERT INTO tprocedure (procedure_ID, price, description, appointmentProcedure_ID, feeCharge_ID) VALUES (%s, %s, %s, %s, %s)"

    val = (procedure_ID, price, description,
           appointmentProcedure_ID, feeCharge_ID)

    cursor = connection.cursor()
    cursor.execute(sql_tprocedure_query, val)
    connection.commit()
    cursor.close()

def fill_tprocedure(connection):
    for i in range(10):
        insert_into_tprocedure(i, 555, "description", i, i, connection)
