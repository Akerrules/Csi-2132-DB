def insert_into_branches(id, city, name, connection):
    sql_branches_query = "INSERT INTO branches (branches_ID, city, name) VALUES (%s, %s, %s)"
    val = (id, city, name)
    
    cursor = connection.cursor()
    cursor.execute(sql_branches_query, val)
    connection.commit()
    cursor.close()


def insert_into_employee(SSN, lastName, firstName, street_Num, street_name,
                         apt_number, city, state, zip, role, type, salary, branches_ID, user_username, connection):

    sql_employee_query = f"INSERT INTO employee (SSN, lastName, firstName, street_Num, street_name, apt_number, city, state, zip, role, type, salary, branches_ID, user_username) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    val = (SSN, lastName, firstName, street_Num, street_name, apt_number, city, state, zip, role, type, salary, branches_ID, user_username)

    cursor = connection.cursor()
    cursor.execute(sql_employee_query, val)
    connection.commit()
    cursor.close()

def insert_into_reviews(reviewsID, POE, communication, cleanliness, value, branches_ID, patientID, connection):
    sql_reviews_query = "INSERT INTO reviews (reviewsID, POE, communication, cleanliness, value, branches_ID, patientID) VALUES (%s, %s, %s, %s, %s, %s, %s)"

    val = (reviewsID, POE, communication, cleanliness, value, branches_ID, patientID)
	
    cursor = connection.cursor()
    cursor.execute(sql_reviews_query, val)
    connection.commit()
    cursor.close()

def insert_into_patient(patientID, lastName, firstName, gender, 
    insurance, ssn, DOB, street_Num, street_name, apt_number, city, state, zip, user_username, connection):
    
    sql_patient_query = "INSERT INTO patient (patientID, lastName, firstName, gender, insurance, ssn, DOB, street_Num, street_name, apt_number, city, state, zip, user_username) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s ,%s)"

    val = (patientID, lastName, firstName, gender, insurance, ssn, DOB, street_Num, street_name, apt_number, city, state, zip, user_username)
	
    cursor = connection.cursor()
    cursor.execute(sql_patient_query, val)
    connection.commit()
    cursor.close()
    
def insert_into_user(username, type, password, email, connection):
    
    sql_user_query = "INSERT INTO user (username, type, password, email) VALUES (%s, %s, %s, %s)"

    val = (username, type, password, email)
	
    cursor = connection.cursor()
    cursor.execute(sql_user_query, val)
    connection.commit()
    cursor.close()

def insert_into_patientChart(record_ID, details, treatment_ID, employee_SSN, connection):
    
    sql_patientChart_query = "INSERT INTO patientChart (record_ID, details, treatment_ID, employee_SSN) VALUES (%s, %s, %s, %s)"

    val = (record_ID, details, treatment_ID, employee_SSN)
	
    cursor = connection.cursor()
    cursor.execute(sql_patientChart_query, val)
    connection.commit()
    cursor.close()

def insert_into_treatment(treatment_ID, appointmentType, treatmentType, medication, symtoms, tooth, comments, appointment_ID, employee_SSN, connection):
    
    sql_treatment_query = "INSERT INTO treatment (treatment_ID, appointmentType, treatmentType, medication, symtoms, tooth, comments, appointment_ID, employee_SSN) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

    val = (treatment_ID, appointmentType, treatmentType, medication, symtoms, tooth, comments, appointment_ID, employee_SSN)
	
    cursor = connection.cursor()
    cursor.execute(sql_treatment_query, val)
    connection.commit()
    cursor.close()

def insert_into_invoice(invoice_ID, issueDate, discount, penalty, phoneNumber, connection):
    
    sql_invoice_query = "INSERT INTO invoice (invoice_ID, issueDate, discount, penalty, phoneNumber) VALUES (%s, %s, %s, %s, %s)"

    val = (invoice_ID, issueDate, discount, penalty, phoneNumber)
	
    cursor = connection.cursor()
    cursor.execute(sql_invoice_query, val)
    connection.commit()
    cursor.close()

def insert_into_appointment(appointment_ID, date, startTime, endtime, type, status, user_username, invoice_ID, connection):
    
    sql_appointment_query = "INSERT INTO appointment (appointment_ID, date, startTime, endtime, type, status, user_username, invoice_ID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

    val = (appointment_ID, date, startTime, endtime, type, status, user_username, invoice_ID)
	
    cursor = connection.cursor()
    cursor.execute(sql_appointment_query, val)
    connection.commit()
    cursor.close()

def insert_into_feecharge(feeCharge_ID, charge, invoice_ID, payment_ID, fee_ID, connection):
    
    sql_feecharge_query = "INSERT INTO feecharge (feeCharge_ID, charge, invoice_ID, payment_ID, fee_ID) VALUES (%s, %s, %s, %s, %s)"

    val = (feeCharge_ID, charge, invoice_ID, payment_ID, fee_ID)
	
    cursor = connection.cursor()
    cursor.execute(sql_feecharge_query, val)
    connection.commit()
    cursor.close()

def insert_into_patientbilling(payment_ID, paymentType, total_charged, patient_portion, insurance_portion, employee_SSN, insuranceClaim_ID,  connection):
    
    sql_patientbilling_query = "INSERT INTO patientbilling (payment_ID, paymentType, total_charged, patient_portion, insurance_portion, employee_SSN, insuranceClaim_ID) VALUES (%s, %s, %s, %s, %s, %s, %s)"

    val = (payment_ID, paymentType, total_charged, patient_portion, insurance_portion, employee_SSN, insuranceClaim_ID)
	
    cursor = connection.cursor()
    cursor.execute(sql_patientbilling_query, val)
    connection.commit()
    cursor.close()

def insert_into_appointmentprocedure(appointmentProcedure_ID, date, procedureType, appointment_ID, connection):
    
    sql_appointmentprocedure_query = "INSERT INTO appointmentprocedure (appointmentProcedure_ID, date, procedureType, appointment_ID) VALUES (%s, %s, %s, %s)"

    val = (appointmentProcedure_ID, date, procedureType, appointment_ID)
	
    cursor = connection.cursor()
    cursor.execute(sql_appointmentprocedure_query, val)
    connection.commit()
    cursor.close()

def insert_into_fees(fee_ID, price, description, feeCharge_ID, connection):
    
    sql_fees_query = "INSERT INTO fee (fee_ID, price, description, feeCharge_ID) VALUES (%s, %s, %s, %s)"

    val = (fee_ID, price, description, feeCharge_ID)
	
    cursor = connection.cursor()
    cursor.execute(sql_fees_query, val)
    connection.commit()
    cursor.close()

def insert_into_insuranceclaim(insuranceClaim_ID, treatmentCost, appointmentProcedure_ID, connection):
    
    sql_insuranceclaim_query = "INSERT INTO insuranceclaim (insuranceClaim_ID, treatmentCost, appointmentProcedure_ID) VALUES (%s, %s, %s)"

    val = (insuranceClaim_ID, treatmentCost, appointmentProcedure_ID)
	
    cursor = connection.cursor()
    cursor.execute(sql_insuranceclaim_query, val)
    connection.commit()
    cursor.close()

def insert_into_tprocedure(procedure_ID, price, description, appointmentProcedure_ID, feeCharge_ID, connection):
    
    sql_tprocedure_query = "INSERT INTO tprocedure (procedure_ID, price, description, appointmentProcedure_ID, feeCharge_ID) VALUES (%s, %s, %s, %s, %s)"

    val = (procedure_ID, price, description, appointmentProcedure_ID, feeCharge_ID)
	
    cursor = connection.cursor()
    cursor.execute(sql_tprocedure_query, val)
    connection.commit()
    cursor.close()