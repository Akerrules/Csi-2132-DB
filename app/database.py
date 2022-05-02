from importlib import import_module
import mysql.connector
from mysql.connector import Error, connect

from tables import user, invoice, appointment, appointmentProcedure, branches, employee, fee, feecharge, insuranceClaim, insuranceClaim, patient, patientBilling, patientChart, procedure, reviews, treatment, treatment


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


def create_tables(db_name, connection):
    sql = f"SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = '{db_name}';"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    if result[0][0] == 0:
        with connection.cursor() as cursor:
            cursor.execute(user.create_table_user())
            cursor.execute(patient.create_table_patient())
            cursor.execute(invoice.create_table_invoice())
            cursor.execute(appointment.create_table_appointment())
            cursor.execute(appointmentProcedure.create_table_appointmentprocedure())
            cursor.execute(branches.create_table_branches())
            cursor.execute(employee.create_table_employee())
            cursor.execute(reviews.create_table_reviews())
            cursor.execute(feecharge.create_table_feecharge())
            cursor.execute(fee.create_table_fee())
            cursor.execute(insuranceClaim.create_table_insuranceclaim())
            cursor.execute(patientBilling.create_table_patientBilling())
            cursor.execute(treatment.create_table_treatment())
            cursor.execute(patientChart.create_table_patientChart())
            cursor.execute(procedure.create_table_tprocedure())
            connection.commit()
            fill_database(connection)
            print("Table creation successfull")
    else:
        print("Tables already exists")

def fill_database(connection):
    branches.fill_branches(connection)
    user.fill_user(connection)
    employee.fill_employee(connection)
    patient.fill_patient(connection)
    invoice.fill_invoice(connection)
    appointment.fill_appointment(connection)
    appointmentProcedure.fill_appointmentprocedure(connection)
    insuranceClaim.fill_insuranceclaim(connection)
    patientBilling.fill_patientBilling(connection)
    feecharge.fill_feecharge(connection)
    fee.fill_fee(connection)
    procedure.fill_tprocedure(connection)
    treatment.fill_treatment(connection)
    patientChart.fill_patientChart(connection)
    reviews.fill_reviews(connection)

    print("Table filled")
    connection.commit()
