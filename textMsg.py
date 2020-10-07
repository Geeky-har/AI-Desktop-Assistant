from twilio.rest import Client
import os

def sendMsg(to, body):
    acc_sid = os.environ['ACC_SID']
    auth_token = os.environ['AUTH_TOKEN']

    client = Client(acc_sid, auth_token)

    msg = client.messages.create(
        from_= '+16266289601',
        body = body,
        to = to)


if __name__ == "__main__":
    sendMsg('+917836952729', 'Hello Testing api')