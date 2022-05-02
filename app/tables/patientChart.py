
# Table patientChart

def create_table_patientChart():
    patientChart_table = """CREATE TABLE IF NOT EXISTS patientchart (
	record_ID INT NOT NULL,
	details VARCHAR(120) NOT NULL,
	treatment_ID INT NOT NULL,
	employee_SSN VARCHAR(10) NOT NULL,
	PRIMARY KEY (record_ID, treatment_ID, employee_SSN),
	INDEX fk_patientchart_treatment (treatment_ID ASC) VISIBLE,
	INDEX fk_patientchart_employee (employee_SSN ASC) VISIBLE,
	CONSTRAINT fk_patientchart_treatment
		FOREIGN KEY (treatment_ID)
		REFERENCES treatment (treatment_ID)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION,
	CONSTRAINT fk_patientchart_employee
		FOREIGN KEY (employee_SSN)
		REFERENCES employee (SSN)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION);
    """

    return patientChart_table


def insert_into_patientChart(record_ID, details, treatment_ID, employee_SSN, connection):

    sql_patientChart_query = "INSERT INTO patientChart (record_ID, details, treatment_ID, employee_SSN) VALUES (%s, %s, %s, %s)"

    val = (record_ID, details, treatment_ID, employee_SSN)

    cursor = connection.cursor()
    cursor.execute(sql_patientChart_query, val)
    connection.commit()
    cursor.close()

def fill_patientChart(connection):
    for i in range(10):
        insert_into_patientChart(i, "details", i, i, connection)