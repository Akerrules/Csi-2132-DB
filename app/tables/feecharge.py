# Table feecharge

def create_table_feecharge():
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

    return feeCharge_table

def insert_into_feecharge(feeCharge_ID, charge, invoice_ID, payment_ID, fee_ID, connection):
    
    sql_feecharge_query = "INSERT INTO feecharge (feeCharge_ID, charge, invoice_ID, payment_ID, fee_ID) VALUES (%s, %s, %s, %s, %s)"

    val = (feeCharge_ID, charge, invoice_ID, payment_ID, fee_ID)
	
    cursor = connection.cursor()
    cursor.execute(sql_feecharge_query, val)
    connection.commit()
    cursor.close()

def fill_feecharge(connection):
    for i in range(10):
        insert_into_feecharge(i, "55", i, i, i, connection)