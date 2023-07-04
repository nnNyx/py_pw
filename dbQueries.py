import mysql.connector


def connect():
    try:
        cnx = mysql.connector.connect(
            user="root", database="password_manager", password="root"
        )
        return cnx
    except mysql.connector.Error as err:
        print(err)


def make_user(username, email, site, password):
    cnx = connect()
    cursor = cnx.cursor()
    insert_query = (
        "INSERT INTO accounts (username, email, site, password) VALUES (%s, %s, %s, %s)"
    )
    insertion_vars = (str(username), str(email), str(site), str(password))
    cursor.execute(insert_query, insertion_vars)
    
    cnx.commit()


def search_user(username):
    cnx = connect()
    cursor = cnx.cursor()
    cursor.execute(f"SELECT * FROM accounts WHERE username = '{username}'")
    return list(cursor)


def search_email(email):
    cnx = connect()
    cursor = cnx.cursor()
    cursor.execute(f"SELECT * FROM accounts WHERE email = '{email}'")
    return list(cursor)


def search_site(site):
    cnx = connect()
    cursor = cnx.cursor()
    cursor.execute(f"SELECT * FROM accounts WHERE site = '{site}'")
    return list(cursor)


def search_all():
    cnx = connect()
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM accounts")
    return list(cursor)
