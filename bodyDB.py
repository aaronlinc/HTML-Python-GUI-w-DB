import sqlite3

# Connect to database
conn = sqlite3.connect('body.db')


def createTable():
    conn.execute("CREATE TABLE if not exists \
        bodyText( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        body TEXT \
        );")

def newRecordMan(body):
    val_str = "'{}'".format(body)

    sql_str = "INSERT INTO bodyText \
        (body)\
        VALUES ({});".format(val_str)
    print (sql_str)
    conn.execute(sql_str)
    conn.commit()
    return conn.total_changes

    
def viewAll():
    # Create sql string
    sql_str = "SELECT * from bodyText"
    cursor = conn.execute(sql_str)

    # Get data from cursor in array
    rows = cursor.fetchall()
    return rows

# Returns a list of strings of all the data in the table
def strList():
        # Create sql string
    sql_str = "SELECT body from bodyText"
    cursor = conn.execute(sql_str)

    # Get data from cursor in array
    rows = cursor.fetchall()

    bodyList = []
    i = 0
    while i < len(rows):
        bodyList.append(rows[i][0])
        i += 1
    return bodyList

def deleteRow(change_id):
    sql_str = "DELETE from bodyText where ID={}"\
              .format(change_id)
    conn.execute(sql_str)
    conn.commit()
    return conn.total_changes


