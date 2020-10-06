from twilio.rest import Client

def sendMsg(to, body):
    acc_sid = 'AC6a12b6e9009709ccaa1931baa2df387f'
    auth_token = 'b555557222f124ca73cdbf4b67807052'

    client = Client(acc_sid, auth_token)

    msg = client.messages.create(
        from_= '+16266289601',
        body = body,
        to = to)


if __name__ == "__main__":
    sendMsg('+917836952729', 'Hello Testing api')