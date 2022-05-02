import mysql.connector
from mysql.connector import Error, connect

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        # Creating db if it doesn't exists
        with mysql.connector.connect(
                host=host_name,
                user=user_name,
                password=user_password
        ) as connection:
            create_db_query = f"CREATE DATABASE IF NOT EXISTS {db_name}"
            with connection.cursor() as cursor:
                cursor.execute(create_db_query)

        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )

        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def create_tables(connection):
    branches_table = """CREATE TABLE IF NOT EXISTS branches (
	branches_ID INT NOT NULL,
	city VARCHAR(40) NOT NULL,
	name VARCHAR(60) NOT NULL,
	PRIMARY KEY (branches_ID));
	"""

    # with connection.cursor() as cursor:
    #     cursor.execute(branches_table)
    #     connection.commit()

    # role VARCHAR(6) NOT NULL, // ENUM?
    # type VARCHAR(6) NOT NULL, // ENUM?

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
	branches_branches_ID INT NOT NULL,
	user_username INT NOT NULL,
	PRIMARY KEY (SSN, branches_branches_ID, user_username),
	INDEX fk_employee_branches (branches_branches_ID ASC) VISIBLE,
	INDEX fk_employee_user (user_username ASC) VISIBLE,
	CONSTRAINT fk_employee_branches
		FOREIGN KEY (branches_branches_ID)
		REFERENCES branches (branches_ID),
	CONSTRAINT fk_employee_user
		FOREIGN KEY (user_username)
		REFERENCES user (username)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION);
    """
    # with connection.cursor() as cursor:
    #     cursor.execute(employee_table)
    #     connection.commit()

    #    	POE INT NOT NULL, // To check
    reviews_table = """CREATE TABLE IF NOT EXISTS reviews (
	reviewsID INT NOT NULL,
	POE VARCHAR(120) NOT NULL,
	communication VARCHAR(120) NOT NULL,
	cleanliness VARCHAR(120) NOT NULL,
	value INT NOT NULL,
	branches_ID INT NOT NULL,
	patientID INT NOT NULL,
	PRIMARY KEY (reviewsID, branches_ID, patientID),
	INDEX fk_reviews_branches (branches_ID ASC) VISIBLE,
	INDEX fk_reviews_patient(patientID ASC) VISIBLE,
	CONSTRAINT fk_reviews_branches
		FOREIGN KEY (branches_ID)
		REFERENCES branches (branches_ID),
	CONSTRAINT fk_reviews_patient
		FOREIGN KEY (patientID)
		REFERENCES patient (patientID)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION);
		"""

    # with connection.cursor() as cursor:
    #     cursor.execute(reviews_table)
    #     connection.commit()

    #	insurance VARCHAR(60) NOT NULL, // Is it insurance name?
    patient_table = """CREATE TABLE IF NOT EXISTS patient (
	patientID INT NOT NULL,
	lastName VARCHAR(120) NOT NULL,
	firstName VARCHAR(120) NOT NULL,
	gender ENUM('Male', 'Female', 'Other') NOT NULL,
	insurance VARCHAR(60) NOT NULL,
	ssn VARCHAR(10) NOT NULL,
	DOB DATE NOT NULL,
	street_Num INT NOT NULL,
	street_name VARCHAR(60) NOT NULL,
	apt_number INT NOT NULL,
	city VARCHAR(60) NOT NULL,
	state VARCHAR(60) NOT NULL,
	zip VARCHAR(6) NOT NULL,
	user_username INT NOT NULL,
	PRIMARY KEY (patientID, user_username),
	INDEX fk_patient_user (user_username ASC) VISIBLE,
	CONSTRAINT fk_patient_user
		FOREIGN KEY (user_username)
		REFERENCES user (username)
		ON DELETE CASCADE
		ON UPDATE NO ACTION);
    """

    # with connection.cursor() as cursor:
    #     cursor.execute(patient_table)
    #     connection.commit()

    user_table = """CREATE TABLE IF NOT EXISTS user (
	username INT NOT NULL,
	type ENUM('Patient', 'Employee') NOT NULL,
	password VARCHAR(120) NOT NULL,
	email VARCHAR(120) NOT NULL,
	PRIMARY KEY (username));
    """

    # with connection.cursor() as cursor:
    #     cursor.execute(user_table)
    #     connection.commit()

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

    # with connection.cursor() as cursor:
    #     cursor.execute(patientChart_table)
    #     connection.commit()
    #   appointmentType ENUM() NOT NULL, // Needs values should we delete?
    #	treatmentType ENUM() NOT NULL, // Needs values
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
		REFERENCES appointment (appointment_ID)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION,
	CONSTRAINT fk_treatment_employee
		FOREIGN KEY (employee_SSN)
		REFERENCES employee (SSN , branches_ID)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION);
    """

    # with connection.cursor() as cursor:
    # cursor.execute(treatment_table)
    # connection.commit()

    #  	startTime ENUM() NOT NULL, // Needs values
    #    	status VARCHAR(60), // ENUM?

    appointment_table = """CREATE TABLE IF NOT EXISTS appointment (
	appointment_ID INT NOT NULL,
	date DATE NOT NULL,
	startTime TIME NOT NULL,
	endtime TIME NOT NULL,
	type VARCHAR(120) NOT NULL,
	status VARCHAR(60) NOT NULL,
	user_username INT NOT NULL,
	invoice_ID INT NOT NULL,
	PRIMARY KEY (appointment_ID, user_username, invoice_ID),
	INDEX fk_appointment_user (user_username ASC) VISIBLE,
	INDEX fk_appointment_invoice (invoice_ID ASC) VISIBLE,
	CONSTRAINT fk_appointment_user
		FOREIGN KEY (user_username)
		REFERENCES user (username)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION,
	CONSTRAINT fk_appointment_invoice
		FOREIGN KEY (invoice_ID)
		REFERENCES invoice (invoice_ID)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION);
    """

    # with connection.cursor() as cursor:
    #     cursor.execute(appointment_table)
    #     connection.commit()

    #     	penalty VARCHAR(60), // String?

    invoice_table = """CREATE TABLE IF NOT EXISTS invoice (
	invoice_ID INT NOT NULL,
	issueDate DATE NOT NULL,
	discount DOUBLE NOT NULL,
	penalty INT NOT NULL,
	phoneNumber VARCHAR(120) NOT NULL,
	PRIMARY KEY (invoice_ID));
	"""

    # with connection.cursor() as cursor:
    #     cursor.execute(invoice_table)
    #     connection.commit()

    # charge DOUBLE NOT NULL, // Check type

    feeCharge_table = """CREATE TABLE IF NOT EXISTS feecharge (
	feeCharge_ID INT NOT NULL,
	charge DOUBLE NOT NULL,
	invoice_ID INT NOT NULL,
	payment_ID INT NOT NULL,
	fee_ID INT NOT NULL,
	PRIMARY KEY (feeCharge_ID, invoice_ID),
	UNIQUE INDEX invoice_ID (invoice_ID ASC) VISIBLE,
	UNIQUE INDEX payment_ID (payment_ID ASC) VISIBLE,
	INDEX fk_feecharge_invoice (invoice_ID ASC) VISIBLE,
	CONSTRAINT fk_feecharge_invoice
		FOREIGN KEY (invoice_ID)
		REFERENCES invoice (invoice_ID)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION);
    """

    # with connection.cursor() as cursor:
    #     cursor.execute(feeCharge_table)
    #     connection.commit()
    #     	paymentType ENUM() NOT NULL, // Fill enum

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

    # with connection.cursor() as cursor:
    #     cursor.execute(patientBilling_table)
    #     connection.commit()

    #     	procedureType ENUM() NOT NULL, // FILL enum
    #	// CHECK IF patientCharge,insuranceCharge,total necessary
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

    # with connection.cursor() as cursor:
    #     cursor.execute(appointmentProcedure_table)
    #     connection.commit()

    fees_table = """CREATE TABLE IF NOT EXISTS fee (
	fee_ID INT NOT NULL,
	price DOUBLE NOT NULL,
	description VARCHAR(120) NOT NULL,
	feeCharge_ID INT NOT NULL,
	PRIMARY KEY (fee_ID, feeCharge_ID),
	INDEX fk_fee_feecharge (feeCharge_ID ASC) VISIBLE,
	CONSTRAINT fk_fee_feecharge
		FOREIGN KEY (feeCharge_ID)
		REFERENCES feecharge (feeCharge_ID)
		ON DELETE CASCADE
		ON UPDATE NO ACTION);
    """

    # with connection.cursor() as cursor:
    #     cursor.execute(fees_table)
    #     connection.commit()

    insuranceClaim_table = """CREATE TABLE IF NOT EXISTS insuranceclaim (
	insuranceClaim_ID INT NOT NULL,
	treatmentCost DOUBLE NOT NULL,
	appointmentProcedure_ID INT NOT NULL,
	PRIMARY KEY (insuranceClaim_ID, appointmentProcedure_ID),
	INDEX fk_insuranceclaim_appointmentprocedure (appointmentProcedure_ID ASC) VISIBLE,
	CONSTRAINT fk_insuranceclaim_appointmentprocedure
		FOREIGN KEY (appointmentProcedure_ID)
		REFERENCES appointmentprocedure (appointmentProcedure_ID)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION);
    """

    # with connection.cursor() as cursor:
    #     cursor.execute(insuranceClaim_table)
    #     connection.commit()

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

    # with connection.cursor() as cursor:
    #     cursor.execute(procedure_table)
    #     connection.commit()

    # finalStr = user_table + invoice_table \
    #     + appointment_table + appointmentProcedure_table + branches_table \
    #     + employee_table + reviews_table \
    #     + feeCharge_table + fees_table + insuranceClaim_table + fees_table \
    #     + patient_table + patientBilling_table + \
    #     treatment_table + patientChart_table + procedure_table

    with connection.cursor() as cursor:
        cursor.execute(user_table)
        cursor.execute(invoice_table)
        cursor.execute(appointment_table)
        cursor.execute(appointmentProcedure_table)
        cursor.execute(branches_table)
        cursor.execute(employee_table)
        cursor.execute(reviews_table)
        cursor.execute(feeCharge_table)
        cursor.execute(fees_table)
        cursor.execute(insuranceClaim_table)
        cursor.execute(patient_table)
        cursor.execute(patientBilling_table)
        cursor.execute(treatment_table)
        cursor.execute(patientChart_table)
        cursor.execute(procedure_table)
        connection.commit()

        print("Table creation successfull")


def fill_database():
    sql_branches_query = "INSERT INTO branches (branches_ID, city, name) VALUES (%i, %s)"
    val = (1, "Ottawa", "DentistOttawa")

    sql_employee_query = "INSERT INTO employee (SSN, lastName, firstName, street_Num) VALUES (%i, %s)"
    val = (1, "Ottawa", "DentistOttawa")

