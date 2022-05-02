# Table Branches

class Branches():
    def __init__(self, branches_ID, city, name):
        self.branches_ID = branches_ID
        self.city = city
        self.name = name

def create_table_branches():
    branches_table = """CREATE TABLE IF NOT EXISTS branches (
	branches_ID INT NOT NULL,
	city VARCHAR(40) NOT NULL,
	name VARCHAR(60) NOT NULL,
	PRIMARY KEY (branches_ID));
	"""

    return branches_table


def insert_into_branches(id, city, name, connection):
    sql_branches_query = "INSERT INTO branches (branches_ID, city, name) VALUES (%s, %s, %s)"
    val = (id, city, name)
    
    cursor = connection.cursor()
    cursor.execute(sql_branches_query, val)
    connection.commit()
    cursor.close()


def fill_branches(connection):
    for i in range(10):
        insert_into_branches(i, "ottawa", f"branch{i}", connection)

def getBranches(connection):
    sql_select = "select * from branches"
    cursor = connection.cursor()
    cursor.execute(sql_select)
    branches = cursor.fetchall()

    lst_branches = [ ]

    for row in branches:
        lst_branches.append(Branches(row[0], row[1], row[2]))
    
    return lst_branches