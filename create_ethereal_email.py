import requests


email_api = 'https://api.nodemailer.com/user'
payload = {
    'requestor': 'nlw_journey_python', # Your name or the name of your project
    'version': '1.0',
}

response = requests.post(email_api, json=payload)
if response.status_code == 200:
    account = response.json()
    with open('ethereal_email.txt', 'w') as file:
        for key, value in account.items():
            file.write(f'{key.capitalize()}: {value}\n')
        
else:
    raise Exception(f'Failed to create ethereal email account: {response.text}')
