# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


from datetime import datetime
import pandas
import random
import smtplib
import os

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

birth_file=read_csv(filepath_or_buffer='birthdays.csv')
#see which is best for data to be dict,list as it is
birth_dict=birth_file.to_dict(orient='records')
print(birth_file)
print(birth_dict)

#import the date time
now=dt.datetime.now()
year=now.year
month=now.month
day=now.day
print(f"{year}-{month}-{day}")
#check the date
is_the_date=False
birth_person=[]
for(index,row) in birth_file.iterrows() :
    if row['month']==month and row['day']==day :
        is_the_date=True
        print(type(row))
        birth_person.append(row)
print(type(birth_person))
print(birth_person)
# name=birth_person['name']
# print(name)

print(len(birth_person))
for item in birth_person:
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    rand_int = randint(0, 2) + 1
    # print(rand_int)
    name=item['name']
    letter_path = f'letter_templates/letter_{rand_int}.txt'
    with open(letter_path, 'r') as f:
        lettercontent = f.read()
    # print(lettercontent)
    lettercontent = lettercontent.replace('[NAME]', f'{name}')
    print(lettercontent)
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_email_password)
        connection.sendmail(from_addr=my_email, msg=f'subject:Happy birth day {name}\n\n {lettercontent}',
                            to_addrs=item['email'])
