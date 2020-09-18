import mysql.connector

mydb = mysql.connector.connect(host = "localhost",
 username = "root", password = "123", database = "mailinfo")

mycursor = mydb.cursor()

def emailEx():
    mycursor.execute("SELECT `email` FROM Details WHERE ID = 1")

    email = mycursor.fetchall()

    stremail = ''.join(str(e) for e in email)

    return(stremail[2:-3:])

def passEx():
    mycursor.execute("SELECT `pass` FROM Details WHERE ID = 1")

    password = mycursor.fetchall()

    strpass = ''.join(str(e) for e in password)

    return(strpass[2:-3:])

if __name__ == "__main__":
    print(emailEx())
    print(passEx())