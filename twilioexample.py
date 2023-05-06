import keys
from twilio.rest import Client

client = Client(keys.account_sid, keys.auth_token)

twilio_num = '+19379322599'
my_cell = '+12818258833'

text_message = client.messages.create(to=my_cell, from_=twilio_num, body="Test text")

print(text_message.status)

call = client.calls.create(url='https://demo.twilio.com/docs/voice.xml', to=my_cell, from_= twilio_num)