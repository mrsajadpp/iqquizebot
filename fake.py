# -----------------------------------------------------------------------------
# Developed by: Muhammed Sajad PP
# License: MIT License
# Copyright (c) 2024 Muhammed Sajad PP
# -----------------------------------------------------------------------------
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# -----------------------------------------------------------------------------

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
