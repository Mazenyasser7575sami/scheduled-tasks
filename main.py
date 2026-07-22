# # To run and test the code you need to update 4 places:
# # 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# # 2. Go to your email provider and make it allow less secure apps.
# # 3. Update the SMTP ADDRESS to match your email provider.
# # 4. Update birthdays.csv to contain today's month and day.
# # See the solution video in the 100 Days of Python Course for explainations.
from http import client

import requests
# pip install flask twilio
# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
phone_number='+15417033743'
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure





import pandas
Recovery_code='EPDDVRS9PRKGAGTY6QM8AXYT'

api_key = os.environ.get("API_KEY")
account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")
LAT=59.329323
LON=18.068581
paramaters={'lat':LAT,'lon':LON,'units':'metric','appid':api_key,'cnt':4}
# response=requests.get('https://api.openweathermap.org/data/2.5/forecast',params={'lat':'30.044420','lon':'31.235712','appid':'6ef922911a338ab4af4554817d3fd9ac'})
response=requests.get('https://api.openweathermap.org/data/2.5/forecast',params=paramaters)
print(response.json())

# api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}
# response=requests.get('https://api.openweathermap.org/data/2.5/forecast?lat=30.044420&lon=31.235712&appid=6ef922911a338ab4af4554817d3fd9ac&units=metric')
respone_list=response.json().get('list')
# print(respone_list)

weather_item=[new_tem for item in respone_list for new_tem in item.get('weather')]
print(weather_item)
code_id=[item['id'] for item in weather_item if item['id']<700]
will_rain=False
for n in code_id:
    if n<700:
        Will_rain=True
if Will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Bring Up Your Umbrella",
        from_=phone_number,
        to="+201222123986",
    )

    print(message.body)

# print(response.json())

# from datetime import datetime
# import pandas
# import random
# import smtplib
# import os

# # import os and use it to get the Github repository secrets
# MY_EMAIL = os.environ.get("MY_EMAIL")
# MY_PASSWORD = os.environ.get("MY_PASSWORD")

# birth_file=read_csv(filepath_or_buffer='birthdays.csv')
# #see which is best for data to be dict,list as it is
# birth_dict=birth_file.to_dict(orient='records')
# print(birth_file)
# print(birth_dict)

# #import the date time
# now=dt.datetime.now()
# year=now.year
# month=now.month
# day=now.day
# print(f"{year}-{month}-{day}")
# #check the date
# is_the_date=False
# birth_person=[]
# for(index,row) in birth_file.iterrows() :
#     if row['month']==month and row['day']==day :
#         is_the_date=True
#         print(type(row))
#         birth_person.append(row)
# print(type(birth_person))
# print(birth_person)
# # name=birth_person['name']
# # print(name)

# print(len(birth_person))
# for item in birth_person:
#     # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
#     rand_int = randint(0, 2) + 1
#     # print(rand_int)
#     name=item['name']
#     letter_path = f'letter_templates/letter_{rand_int}.txt'
#     with open(letter_path, 'r') as f:
#         lettercontent = f.read()
#     # print(lettercontent)
#     lettercontent = lettercontent.replace('[NAME]', f'{name}')
#     print(lettercontent)
#     with smtplib.SMTP('smtp.gmail.com', 587) as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=my_email_password)
#         connection.sendmail(from_addr=my_email, msg=f'subject:Happy birth day {name}\n\n {lettercontent}',
#                             to_addrs=item['email'])
