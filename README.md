# secret santa bot

Do you want to organize a secret santa between you and your friends but COVID is stopping you? Use this bot to randomly choose secret santas and send everyone the name of the person they should send their gift to by SMS.
### You must create a json file named config.json and it must contain these keys. These values are obtained when configuring your twilio account, except the country_code. That one depends on the number that will recieve the messages. It assumes they're all from the same country.
{
    "account_sid": "XXXXXXXXXXX",
    "auth_token": "XXXXXXXXXXXXX",
    "twilio_number": "+111111111",
    "country_code": "+52"
}

> Extra note: You must verify all the numbers you will be sending a message to first. This is done from within the twilio console. Google 'Twilio Verify Caller ID'

## Before running this code
* Create config.json file
* Verify outgoing numbers in the twilio console

## To run the code
* git clone this repo
* if you want, create a virtualenv
* pip install the requirements file (it's only the Twilio client)
* run 'python main.py'