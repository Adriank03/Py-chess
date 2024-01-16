import mysql.connector
db = mysql.connector.connect(
    host = 'sql5.freesqldatabase.com',
    user = 'sql5674283',
    password = 'W5jPmDwEzn',
    database = 'sql5674283',
    port = 3306
)
mycursor = db.cursor()
def createUser(name, passw):
   mycursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (name, passw))
   db.commit()

def showAllPlayers():
    mycursor.execute("SELECT * FROM users")
    for x in mycursor:
        print(x)

def deleteUser(username):
     mycursor.execute("DELETE FROM users WHERE username=%s", (username,))

def findUser(username):
    print("hey)")
    mycursor.execute("SELECT * FROM users WHERE username=%s", (username,))
    return mycursor

