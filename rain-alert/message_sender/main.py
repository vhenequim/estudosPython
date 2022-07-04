from twilio.rest import Client

account_sid = 'ACf9a2ecb8048415f27dbb54264c60e63d'
auth_token = '0237f6fd4dde6da35ee3f5f01d34e67a'
client = Client(account_sid, auth_token)

message = client.messages.create(
    messaging_service_sid='MG32c14617f614b572d3c6a3f9fc59276e',
    body='I love big dick',
    to='+5541991179474'
)

print(message.sid)