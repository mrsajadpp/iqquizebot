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
    try:
        date_parts = date.split("/")
        return f"{date_parts[1]}{date_parts[0]}{date_parts[2]}"
    except IndexError:
        raise ValueError(f"Invalid date format: {date}. Expected DD/MM/YYYY.")


def load_data(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        exit(1)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        exit(1)


def scroll_to_element(driver, element):
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
    time.sleep(1) 


def fill_form(data):
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://www.manoramaquiz.in/signUp")

        full_name_field = wait.until(
            EC.presence_of_element_located((By.ID, "fullName"))
        )
        scroll_to_element(driver, full_name_field)
        full_name_field.send_keys(data["fullName"])

        school_dropdown = driver.find_element(By.ID, "rc_select_0")
        scroll_to_element(driver, school_dropdown)
        school_dropdown.click()
        time.sleep(1)
        school_dropdown.send_keys(data["schoolName"])
        school_dropdown.send_keys(Keys.RETURN)

        phone_field = driver.find_element(By.ID, "PhoneNumber")
        scroll_to_element(driver, phone_field)
        phone_field.send_keys(data["phoneNumber"])

        email_field = driver.find_element(By.ID, "email")
        scroll_to_element(driver, email_field)
        email_field.send_keys(data["email"])

        dob_input = driver.find_element(By.ID, "dob")
        scroll_to_element(driver, dob_input)
        dob_input.send_keys(data["dob"])

        role_tab_script = """
            const elements = document.querySelectorAll('.role-tab');
            if (elements.length >= 4) {
                elements[3].scrollIntoView({behavior: 'smooth', block: 'center'});
                elements[3].click();
            } else {
                console.error('4th role-tab not found');
            }
        """
        driver.execute_script(role_tab_script)
        time.sleep(2)

        submit_button = driver.find_element(By.CLASS_NAME, "submit-button")
        scroll_to_element(driver, submit_button)
        submit_button.click()
        print(f"Form for {data['fullName']} submitted successfully.")
        time.sleep(2)

        driver.get("https://www.manoramaquiz.in/")

        password = convert_date(data["dob"])
        password_field = wait.until(
            EC.visibility_of_element_located((By.ID, "password"))
        )
        scroll_to_element(driver, password_field)
        password_field.send_keys(password)

        email_login_field = wait.until(
            EC.visibility_of_element_located((By.ID, "username"))
        )
        scroll_to_element(driver, email_login_field)
        email_login_field.send_keys(data["email"])

        submit_button = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "submit-button"))
        )
        scroll_to_element(driver, submit_button)
        submit_button.click()
        print(f"Login for {data['fullName']} successful.")

        time.sleep(3)

        start_quiz_button = driver.find_element(By.CSS_SELECTOR, ".button-container .banner-button")
        start_quiz_button.click()

        time.sleep(2)

        inputs = driver.find_elements(By.CSS_SELECTOR, ".answer-cells .answer-cell")

        answers = ['B', 'A', 'R', 'O', 'D', 'A']

        for i, value in enumerate(answers):
             inputs[i].send_keys(value)

        time.sleep(1)

        next_quiz_button = driver.find_element(By.CSS_SELECTOR, ".next-btn")
        scroll_to_element(driver, next_quiz_button)
        next_quiz_button.click()

        time.sleep(1)

        inputs_two = driver.find_elements(By.CSS_SELECTOR, ".answer-cells .answer-cell")

        answers_two = ['L', 'A', 'L', 'A', 'L', 'A', 'J', 'P', 'A', 'T', 'R', 'A', 'I']

        for i, value in enumerate(answers_two):
             inputs_two[i].send_keys(value)

        time.sleep(1)

        next_quiz_button = driver.find_element(By.CSS_SELECTOR, ".next-btn")
        scroll_to_element(driver, next_quiz_button)
        next_quiz_button.click()

        time.sleep(1)

        inputs_three = driver.find_elements(By.CSS_SELECTOR, ".answer-cells .answer-cell")

        answers_three = ['E', 'S', 'A']

        for i, value in enumerate(answers_three):
             inputs_three[i].send_keys(value)

        time.sleep(1)

        next_quiz_button = driver.find_element(By.CSS_SELECTOR, ".next-btn")
        scroll_to_element(driver, next_quiz_button)
        next_quiz_button.click()

        time.sleep(1)

        inputs_four = driver.find_elements(By.CSS_SELECTOR, ".answer-cells .answer-cell")

        answers_four = ['S', 'O', 'U', 'T', 'H', 'K', 'O', 'R', 'E', 'A']

        for i, value in enumerate(answers_four):
             inputs_four[i].send_keys(value)

        time.sleep(1)

        next_quiz_button = driver.find_element(By.CSS_SELECTOR, ".next-btn")
        scroll_to_element(driver, next_quiz_button)
        next_quiz_button.click()

        time.sleep(1)


        inputs_five = driver.find_elements(By.CSS_SELECTOR, ".answer-cells .answer-cell")

        answers_five = ['S', 'N', 'E', 'H', 'A', 'L', 'A', 'Y', 'A', 'M']

        for i, value in enumerate(answers_five):
             inputs_five[i].send_keys(value)

        time.sleep(1)

        next_quiz_button = driver.find_element(By.CSS_SELECTOR, ".submit-btn")
        scroll_to_element(driver, next_quiz_button)
        next_quiz_button.click()

        time.sleep(1)

    except Exception as e:
        print(f"An error occurred for {data['fullName']}: {e}")

    finally:
        time.sleep(2)
        driver.quit()
        print(f"Completed processing for {data['fullName']}")


if __name__ == "__main__":
    json_file_path = "fake_user_data.json"
    form_data = load_data(json_file_path)

    for user in form_data:
        fill_form(user)
