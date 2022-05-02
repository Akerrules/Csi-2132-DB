
# Table fee

def create_table_fee():
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
    return fees_table

def insert_into_fees(fee_ID, price, description, feeCharge_ID, connection):
    
    sql_fees_query = "INSERT INTO fee (fee_ID, price, description, feeCharge_ID) VALUES (%s, %s, %s, %s)"

    val = (fee_ID, price, description, feeCharge_ID)
	
    cursor = connection.cursor()
    cursor.execute(sql_fees_query, val)
    connection.commit()
    cursor.close()

def fill_fee(connection):
    for i in range(10):
        insert_into_fees(i, "555", "description", i, connection)
	

