from faker import Faker
import re
import json

fake = Faker()

def generate_fake_email(first_name, last_name):
    first_name = re.sub(r'[^a-zA-Z]', '', first_name).lower() 
    last_name = re.sub(r'[^a-zA-Z]', '', last_name).lower()
    return f"{first_name}{last_name}@gmail.com"

user_data = []
for _ in range(400):
    first_name = fake.first_name()
    last_name = fake.last_name()
    
    user = {
        "fullName": f"{first_name} {last_name}",
        "schoolName": "NHSS Kolathur",
        "phoneNumber": fake.phone_number(),
        "email": generate_fake_email(first_name, last_name),
        "dob": fake.date_of_birth(minimum_age=15, maximum_age=18).strftime('%m/%d/%Y')
    }
    user_data.append(user)

with open('fake_user_data.json', 'w') as f:
    json.dump(user_data, f, indent=4)

print("Data has been saved to fake_user_data.json")
