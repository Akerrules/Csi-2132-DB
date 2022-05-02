# Table patient
class Patient():
    def __init__(self, patientID, lastName, firstName, gender,
                 insurance, ssn, DOB, street_Num, street_name, apt_number, city, state, zip, user_username,):
        self.patientID = patientID
        self.lastName = lastName
        self.firstName = firstName
        self.gender = gender
        self.insurance = insurance
        self.ssn = ssn
        self.DOB = DOB
        self.street_Num = street_Num
        self.street_name = street_name
        self.apt_number = apt_number
        self.city = city
        self.state = state
        self.zip = zip
        self.user_username = user_username


def create_table_patient():
    patient_table = """CREATE TABLE IF NOT EXISTS patient (
	patientID INT NOT NULL AUTO_INCREMENT,
	lastName VARCHAR(120) NOT NULL,
	firstName VARCHAR(120) NOT NULL,
	gender ENUM('Male', 'Female', 'Other') NOT NULL,
	insurance VARCHAR(60) NOT NULL,
	ssn VARCHAR(120) NOT NULL,
	DOB DATE NOT NULL,
	street_Num INT NOT NULL,
	street_name VARCHAR(60) NOT NULL,
	apt_number INT NOT NULL,
	city VARCHAR(60) NOT NULL,
	state VARCHAR(60) NOT NULL,
	zip VARCHAR(6) NOT NULL,
	user_username VARCHAR(120) NOT NULL,
	PRIMARY KEY (patientID, user_username),
	INDEX fk_patient_user (user_username ASC) VISIBLE,
	CONSTRAINT fk_patient_user
		FOREIGN KEY (user_username)
		REFERENCES user (username)
		ON DELETE CASCADE
		ON UPDATE NO ACTION);
    """

    return patient_table


def insert_into_patient(patientID, lastName, firstName, gender,
                        insurance, ssn, DOB, street_Num, street_name, apt_number, city, state, zip, user_username, connection):

    sql_patient_query = "INSERT INTO patient (lastName, firstName, gender, insurance, ssn, DOB, street_Num, street_name, apt_number, city, state, zip, user_username) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s ,%s)"

    val = (lastName, firstName, gender, insurance, ssn, DOB,
           street_Num, street_name, apt_number, city, state, zip, user_username)

    cursor = connection.cursor()
    cursor.execute(sql_patient_query, val)
    connection.commit()
    cursor.close()


def updatePatient2(patientID, lastName, firstName, gender,
                  insurance, ssn, DOB, street_Num, street_name, apt_number, city, state, zip, user_username, connection):

    sql = "UPDATE patient SET lastName = %s, firstName = %s, gender = %s, insurance = %s, ssn = %s, DOB = %s, street_Num = %s, street_name = %s, apt_number = %s, city = %s, state = %s, zip = %s, user_username = %s WHERE patientID = %s"

    val = (lastName, firstName, gender, insurance, ssn, DOB,
           street_Num, street_name, apt_number, city, state, zip, user_username, patientID)

    cursor = connection.cursor()
    cursor.execute(sql, val)
    connection.commit()
    cursor.close()

def updatePatient(patientID, insurance,street_Num, street_name, apt_number, city, state, zip, connection):

    sql = "UPDATE patient SET insurance = %s, street_Num = %s, street_name = %s, apt_number = %s, city = %s, state = %s, zip = %s WHERE patientID = %s"

    val = (insurance, street_Num, street_name, apt_number, city, state, zip, patientID)

    cursor = connection.cursor()
    cursor.execute(sql, val)
    connection.commit()
    cursor.close()

def fill_patient(connection):
    insert_into_patient(-1, "test", "test", "Male", "insurance", f"000000",
                    "2000/01/01", f"000", "street", "0", "Ottawa", "Ontario", "00000", "test", connection)

    for i in range(10):
        insert_into_patient(i, f"patient{i}", f"patient{i}", "Other", "insurance", f"000 00{i}",
                            "2000/01/01", f"00{i}", "street", f"{i}", "Ottawa", "Ontario", f"0000{i}", f"patient{i}", connection)


def getAllPatient(connection):
    sql_select = "select * from patient"
    cursor = connection.cursor()
    cursor.execute(sql_select)
    patient = cursor.fetchall()

    lst_patient = []

    for row in patient:
        lst_patient.append(Patient(row[0], row[1], row[2], row[3], row[4], row[5],
                           row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13]))

    return lst_patient

def getPatient(id, connection):
    sql_select = "select * from patient WHERE patientID = %s"
    val = [(id)]
    cursor = connection.cursor()
    cursor.execute(sql_select, val)
    patient = cursor.fetchall()

    lst_patient = []

    for row in patient:
        lst_patient.append(Patient(row[0], row[1], row[2], row[3], row[4], row[5],
                           row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13]))

    return lst_patient.pop()

def getPatientNames(connection):
    sql_select = "select user_username from patient"
    cursor = connection.cursor()
    cursor.execute(sql_select)
    patient = cursor.fetchall()

    lst_patient = []

    for row in patient:
        lst_patient.append(row[0])
    
    return lst_patient
