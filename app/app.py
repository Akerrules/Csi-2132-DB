import datetime


import database
from tables import *
import tables.user
import tables.patient
import tables.appointment
import tables.employee
from flask import Flask, render_template, request, redirect, url_for, session

connection = database.create_db_connection(
    "localhost", "root", "8qHj2C*RfePh!W", "db_dental")

database.create_tables("db_dental", connection)

app = Flask(__name__)
app.secret_key = 'dental'

@app.route('/')
def index():
    return render_template('index.html',wrong=False)


@app.route('/login', methods=['POST'])
def login():
    userName = request.form.get('userName')
    password = request.form.get('password')

    if not tables.user.check_connection(userName, password, connection):
      
        return render_template('index.html', wrong=True)
    else:
        user = tables.user.getUser(userName, password, connection)
        session['user'] = user.type
        print(user.type)
        if user.type == "Receptionist":
            return redirect(url_for('receptionist'))
        elif user.type == "Dentist" or user.type == "Hygienist":
            return redirect(url_for('dentist', username=userName))
        else:
            return redirect(url_for('patient', username=userName))


@app.route('/receptionist')
def receptionist():
    if session['user'] != None and session['user'] == "Receptionist":
        patients = tables.patient.getAllPatient(connection)
        patientNames = tables.patient.getPatientNames(connection)
        employeeNames = tables.employee.getEmployeeNames(connection)
        return render_template('Receptionist.html', patients=patients, patientNames=patientNames, employeeNames=employeeNames)
    else:
        return redirect('/')


@app.route('/patientInfo')
def patientInfo():
    return render_template('patientInfo.html',exist=False)


@app.route('/patientInfo/create', methods=['POST'])
def createPatient():
    userName = request.form.get('userName')
    if  tables.user.userExist(userName,connection):
        return render_template("patientInfo.html", exist=True)

    firstName = request.form.get('firstName')
    lastName = request.form.get('lastName')
    password = request.form.get('password')
    gender = request.form.get('gender')
    insurance = request.form.get('insurance')
    ssn = request.form.get('ssn')
    DOB = request.form.get('birthday')
    street_Num = request.form.get('streetNb')
    street_name = request.form.get('streetName')
    apt_number = request.form.get('aptNb')
    city = request.form.get('city')
    state = request.form.get('state')
    zip = request.form.get('zip')
    email = userName + "@user.com"

    tables.user.insert_into_user(
        userName, "Patient", password, email, connection)
    tables.patient.insert_into_patient(0, lastName, firstName, gender, insurance, ssn,
                                    DOB, street_Num, street_name, apt_number, city, state, zip, userName, connection)
    return redirect(url_for('receptionist'))

            
    

@app.route('/patientInfo/edit/<int:id>', methods=['GET', 'POST'])
def editPatient(id):
    patient = tables.patient.getPatient(id, connection)

    if request.method == 'GET':
        return render_template('editPatient.html', patient=patient)
    else:
        insurance = request.form.get('insurance')
        street_Num = request.form.get('streetNb')
        street_name = request.form.get('streetName')
        apt_number = request.form.get('aptNb')
        city = request.form.get('city')
        state = request.form.get('state')
        zip = request.form.get('zip')
        tables.patient.updatePatient(
            id, insurance, street_Num, street_name, apt_number, city, state, zip, connection)
        return redirect(url_for('receptionist'))


@app.route('/appointment', methods=['POST'])
def setAppointment():
    patient = request.form.get('patient')
    dentist = request.form.get('dentist')
    type = request.form.get('type')
    time = request.form.get('time')
    startTime = request.form.get('startTime')
    endTime = request.form.get('endTime')
    tables.appointment.insert_into_appointment(
        -1, time, startTime, endTime, type, "Not complete", dentist, patient, 0, connection)

    if session['user'] == "Receptionist":
        return redirect(url_for('receptionist'))
    else:
        return redirect(url_for('patient', username=patient))


@app.route('/dentist/<username>')
def dentist(username):
    if session['user'] != None and session['user'] == "Dentist" or session['user'] == "Hygienist":
        appointments = tables.appointment.getUpcomingAppointment(
            username, connection)
        return render_template('dentist.html', appointments=appointments)
    else:
        return redirect('/')


@app.route('/medicalHistory/<username>')
def medicalHistory(username):
    appointments = tables.appointment.getAllAppointmentPatient(
        username, connection)
    return render_template('PatientMedical.html', appointments=appointments, username=username)

@app.route('/logOut')
def logOut():
    session['user']=None
    return redirect('/')


@app.route('/patient/<username>')
def patient(username):
    if session['user'] != None and session['user'] == "Patient":
        appointments = tables.appointment.getUpcomingAppointmentPatient(
            username, connection)
        employeeNames = tables.employee.getEmployeeNames(connection)

        return render_template('Patient.html', appointments=appointments, username=username, employeeNames=employeeNames)
    else:
        return redirect('/')

# python -m flask run
