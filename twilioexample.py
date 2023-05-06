import keys
from twilio.rest import Client

client = Client(keys.account_sid, keys.auth_token)

twilio_num = ''
my_cell = ''

text_message = client.messages.create(to=my_cell, from_=twilio_num, body="Test text")

print(text_message.status)

call = client.calls.create(url='https://demo.twilio.com/docs/voice.xml', to=my_cell, from_= twilio_num)