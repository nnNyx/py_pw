import mysql.connector


class SQLManager:
    def __init__(self):
        self.cnx = mysql.connector.connect(
            user="root", database="password_manager", password="root", autocommit=True
        )

    def createTable(self):
        with self.cnx.cursor() as cursor:
            cursor.execute(
                "CREATE TABLE accounts (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(40), email VARCHAR(60), site VARCHAR(80), password VARCHAR(120))"
            )
            print("Table created.")

    def showTables(self):
        with self.cnx.cursor() as cursor:
            cursor.execute("SHOW tables")
            print(list(cursor))

    def describeTable(self):
        with self.cnx.cursor() as cursor:
            cursor.execute("DESCRIBE accounts")
            print(list(cursor))

    def resetIncrement(self):
        with self.cnx.cursor() as cursor:
            cursor.execute("ALTER TABLE accounts AUTO_INCREMENT = 1")
            print("Reset increment")

    def deleteData(self):
        with self.cnx.cursor() as cursor:
            cursor.execute("DELETE FROM accounts")

    def make_user(self, username, email, site, password):
        with self.cnx.cursor() as cursor:
            insert_query = (
                "INSERT INTO accounts (username, email, site, password) VALUES (%s, %s, %s, %s)"
            )
            insertion_vars = (str(username), str(email), str(site), str(password))
            cursor.execute(insert_query, insertion_vars) #anti injection



manage = SQLManager()
x = int(
    input(
        "1-Show Tables\n2-Describe Table\n3-Reset Increment\n4-Delete Data\n5-Create table\n"
    )
)
if x == 1:
    manage.showTables()
elif x == 2:
    manage.describeTable()
elif x == 3:
    manage.resetIncrement()
elif x == 4:
    manage.deleteData()
elif x == 5:
    manage.createTable()
elif not 0 < x < 6:
    print("Not an option.")