# Table Reviews

from random import randrange


def create_table_reviews():
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

    return reviews_table


def insert_into_reviews(reviewsID, POE, communication, cleanliness, value, branches_ID, patientID, connection):
    sql_reviews_query = "INSERT INTO reviews (reviewsID, POE, communication, cleanliness, value, branches_ID, patientID) VALUES (%s, %s, %s, %s, %s, %s, %s)"

    val = (reviewsID, POE, communication,
           cleanliness, value, branches_ID, patientID)

    cursor = connection.cursor()
    cursor.execute(sql_reviews_query, val)
    connection.commit()
    cursor.close()

def fill_reviews(connection):
    for i in range(10):
        insert_into_reviews(i, "great", "incredible", "clean", randrange(5), i, i+1, connection)
