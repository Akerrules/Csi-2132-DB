# Table insuranceclaim

def create_table_insuranceclaim():
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

    return insuranceClaim_table


def insert_into_insuranceclaim(insuranceClaim_ID, treatmentCost, appointmentProcedure_ID, connection):

    sql_insuranceclaim_query = "INSERT INTO insuranceclaim (insuranceClaim_ID, treatmentCost, appointmentProcedure_ID) VALUES (%s, %s, %s)"

    val = (insuranceClaim_ID, treatmentCost, appointmentProcedure_ID)

    cursor = connection.cursor()
    cursor.execute(sql_insuranceclaim_query, val)
    connection.commit()
    cursor.close()


def fill_insuranceclaim(connection):
    for i in range(10):
        insert_into_insuranceclaim(i, "554", i, connection)
