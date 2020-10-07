from twilio.rest import Client
import os
import mysql.connector

def getNum(name):
    mydb = mysql.connector.connect(host = 'localhost',
 username = 'root', password = '123', database = 'mailinfo')

    mycursor = mydb.cursor()

    mycursor.execute(f"select `number` from `MYNUMS` where `name` = '{name}'")

    num = mycursor.fetchall()

    strnum = ''.join(str(e) for e in num)

    return strnum[2:-3:]


def sendMsg(to, body):
    acc_sid = os.environ['ACC_SID']
    auth_token = os.environ['AUTH_TOKEN']

    client = Client(acc_sid, auth_token)

    msg = client.messages.create(
        from_= '+16266289601',
        body = body,
        to = to)


if __name__ == "__main__":
    sendMsg('xxxxx', 'Hello Testing api')
    print(getNum('harsh'))