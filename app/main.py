
import app.database as database

connection = database.create_db_connection("localhost", "root", "rootroot", "db_dental")
database.create_tables(connection)
database.fill_database(connection)

# tables.patient.getPatientNames(connection)
# tables.patient.updatePatient(5, "insurance", "55", "eer",55, "test","ff", "00000", connection)
# tables.patient.getPatient(5, connection)
# database.fill_database(connection)
#from tables.user import check_connection
