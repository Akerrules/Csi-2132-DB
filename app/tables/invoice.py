# Table invoice

import datetime


class Invoice():
    def __init__(self, invoice_ID, issueDate, discount, penalty, phoneNumber):
        self.invoice_ID = invoice_ID
        self.issueDate = issueDate
        self.discount = discount
        self.penalty = penalty
        self.phoneNumber = phoneNumber


def create_table_invoice():
    invoice_table = """CREATE TABLE IF NOT EXISTS invoice (
	invoice_ID INT NOT NULL,
	issueDate DATE NOT NULL,
	discount DOUBLE NOT NULL,
	penalty INT NOT NULL,
	phoneNumber VARCHAR(120) NOT NULL,
	PRIMARY KEY (invoice_ID));
	"""

    return invoice_table


def insert_into_invoice(invoice_ID, issueDate, discount, penalty, phoneNumber, connection):

    sql_invoice_query = "INSERT INTO invoice (invoice_ID, issueDate, discount, penalty, phoneNumber) VALUES (%s, %s, %s, %s, %s)"

    val = (invoice_ID, issueDate, discount, penalty, phoneNumber)

    cursor = connection.cursor()
    cursor.execute(sql_invoice_query, val)
    connection.commit()
    cursor.close()


def fill_invoice(connection):
    for i in range(10):
        insert_into_invoice(i, datetime.datetime.now(),
                            "55.5", "0", "000-000-0000", connection)
