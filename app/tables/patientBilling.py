# Table patientBilling

def create_table_patientBilling():
    patientBilling_table = """CREATE TABLE IF NOT EXISTS patientbilling (
	payment_ID INT NOT NULL,
	paymentType ENUM('Check', 'Cash', 'Card') NOT NULL,
	total_charged DOUBLE NOT NULL,
	patient_portion DOUBLE NOT NULL,
	insurance_portion VARCHAR(120) NOT NULL,
	employee_SSN VARCHAR(10) NOT NULL,
	insuranceClaim_ID INT NOT NULL,
	PRIMARY KEY (payment_ID, employee_SSN, insuranceClaim_ID),
	INDEX fk_patientbilling_employee (employee_SSN ASC) VISIBLE,
	INDEX fk_patientbilling_insuranceclaim (insuranceClaim_ID ASC) VISIBLE,
	CONSTRAINT fk_patientbilling_employee
		FOREIGN KEY (employee_SSN)
		REFERENCES employee (SSN)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION,
	CONSTRAINT fk_patientbilling_insuranceclaim
		FOREIGN KEY (insuranceClaim_ID)
		REFERENCES insuranceclaim (insuranceClaim_ID)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION);
    """

    return patientBilling_table


def insert_into_patientbilling(payment_ID, paymentType, total_charged, patient_portion, insurance_portion, employee_SSN, insuranceClaim_ID,  connection):

    sql_patientbilling_query = "INSERT INTO patientbilling (payment_ID, paymentType, total_charged, patient_portion, insurance_portion, employee_SSN, insuranceClaim_ID) VALUES (%s, %s, %s, %s, %s, %s, %s)"

    val = (payment_ID, paymentType, total_charged, patient_portion,
           insurance_portion, employee_SSN, insuranceClaim_ID)

    cursor = connection.cursor()
    cursor.execute(sql_patientbilling_query, val)
    connection.commit()
    cursor.close()


def fill_patientBilling(connection):
    for i in range(10):
        insert_into_patientbilling(
            i, "Check", "554", "50", "40", i, i, connection)
