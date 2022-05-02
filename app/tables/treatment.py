
# Table treatment

def create_table_treatment():
    treatment_table = """CREATE TABLE IF NOT EXISTS treatment (
	treatment_ID INT NOT NULL,
	appointmentType VARCHAR(120) NOT NULL,
	treatmentType VARCHAR(120) NOT NULL,
	medication VARCHAR(10) NOT NULL,
	symtoms VARCHAR(120) NOT NULL,
	tooth VARCHAR(60) NOT NULL,
	comments VARCHAR(60) NOT NULL,
	appointment_ID INT NOT NULL,
	employee_SSN VARCHAR(10) NOT NULL,
	PRIMARY KEY (treatment_ID, appointment_ID, employee_SSN),
	INDEX fk_treatment_appointment (appointment_ID ASC) VISIBLE,
	INDEX fk_treatment_employee (employee_SSN ASC) VISIBLE,
	CONSTRAINT fk_treatment_appointment
		FOREIGN KEY (appointment_ID)
		REFERENCES appointment (appointment_ID),
	CONSTRAINT fk_treatment_employee
		FOREIGN KEY (employee_SSN)
		REFERENCES employee (SSN));
    """

    return treatment_table

def insert_into_treatment(treatment_ID, appointmentType, treatmentType, medication, symtoms, tooth, comments, appointment_ID, employee_SSN, connection):
    
    sql_treatment_query = "INSERT INTO treatment (treatment_ID, appointmentType, treatmentType, medication, symtoms, tooth, comments, appointment_ID, employee_SSN) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

    val = (treatment_ID, appointmentType, treatmentType, medication, symtoms, tooth, comments, appointment_ID, employee_SSN)
	
    cursor = connection.cursor()
    cursor.execute(sql_treatment_query, val)
    connection.commit()
    cursor.close()

def fill_treatment(connection):
    for i in range(10):
        insert_into_treatment(i, "appointment type", "treatment type", "no", "n/a", "clean", "n/a", i+1, i, connection)

