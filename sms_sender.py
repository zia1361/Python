from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACf61b52fbecd9459235414c5f1ed99bac'
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="",
                     from_='+',
                     to='+'
                 )

print(message.sid)