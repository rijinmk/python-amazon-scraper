# +15167012231
# +971565912018
# AC8d734a3bb49eeac7e2c8098f0eb09e8e
# 7f173f7f8134bf857383b094cb8d33e3

from twilio.rest import Client
import json

account_sid = "AC8d734a3bb49eeac7e2c8098f0eb09e8e"
auth_token = "7f173f7f8134bf857383b094cb8d33e3"
client = Client(account_sid, auth_token)

message = client.messages.create(
    body='Hi there!',
    from_='+15167012231',
    to='+971565912018'
)

print(json.loads(message))

# for i in dir(message): 
#     try: 
#         print(message.i)
#     except: 
#         pass