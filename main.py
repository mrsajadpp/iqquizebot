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

import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def convert_date(date):
    date_parts = date.split("/")
    
    return f"{date_parts[1]}{date_parts[0]}{date_parts[2]}"


def load_data(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


def fill_form(data):
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.manoramaquiz.in/signUp")
        wait = WebDriverWait(driver, 10)

        full_name_field = wait.until(
            EC.presence_of_element_located((By.ID, "fullName"))
        )
        full_name_field.send_keys(data["fullName"])

        school_dropdown = driver.find_element(By.ID, "rc_select_0")
        school_dropdown.send_keys(data["schoolName"])
        school_dropdown.send_keys(Keys.RETURN)

        phone_field = driver.find_element(By.ID, "PhoneNumber")
        phone_field.send_keys(data["phoneNumber"])

        email_field = driver.find_element(By.ID, "email")
        email_field.send_keys(data["email"])

        dob_input = driver.find_element(By.ID, "dob")
        dob_input.send_keys(data["dob"])

        driver.execute_script(
            """
            const elements = document.querySelectorAll('.role-tab');
            if (elements.length >= 4) {
                elements[3].click();  // 4th element (0-indexed)
            } else {
                console.log('4th element not found');
            }
            """
        )
        time.sleep(5)

        submit_button = driver.find_element(By.CLASS_NAME, "submit-button")
        submit_button.click()
        print(f"Form for {data['fullName']} submitted successfully.")

        time.sleep(5)

        driver.get("https://www.manoramaquiz.in/")

        wait = WebDriverWait(driver, 10)

        try:
            password_field = wait.until(
                EC.visibility_of_element_located((By.ID, "password"))
            )
            password = convert_date(data["dob"])
            password_field.send_keys(password)

            email_login_field = wait.until(
                EC.visibility_of_element_located((By.ID, "username"))
            )
            email_login_field.send_keys(data["email"])

            submit_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "submit-button"))
            )
            submit_button.click()
            print(f"Login for {data['fullName']} successful.")
            time.sleep(5)
        except Exception as e:
            print(f"An error occurred while logging in for {data['fullName']}: {e}")


    except Exception as e:
        print(f"An error occurred while processing {data['fullName']}: {e}")
    finally:
        driver.quit()
        print(f"Completed processing for {data['fullName']}")


if __name__ == "__main__":
    json_file_path = "fake_user_data.json"
    form_data = load_data(json_file_path)

    for user in form_data:
        fill_form(user)
