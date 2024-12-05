import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Convert date from DD/MM/YYYY to MMDDYYYY
def convert_date(date):
    # Split the date by "/"
    date_parts = date.split("/")
    
    # Re-arrange the parts from DD/MM/YYYY to MMDDYYYY
    return f"{date_parts[1]}{date_parts[0]}{date_parts[2]}"


# Load data from a JSON file
def load_data(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


# Fill the form using Selenium
def fill_form(data):
    driver = webdriver.Chrome()  # Ensure chromedriver is in your PATH
    try:
        # Open the signup webpage
        driver.get("https://www.manoramaquiz.in/signUp")
        wait = WebDriverWait(driver, 10)

        # Fill the full name
        full_name_field = wait.until(
            EC.presence_of_element_located((By.ID, "fullName"))
        )
        full_name_field.send_keys(data["fullName"])

        # Select school (use search-based dropdown handling)
        school_dropdown = driver.find_element(By.ID, "rc_select_0")
        school_dropdown.send_keys(data["schoolName"])
        school_dropdown.send_keys(Keys.RETURN)

        # Fill the phone number
        phone_field = driver.find_element(By.ID, "PhoneNumber")
        phone_field.send_keys(data["phoneNumber"])

        # Fill the email
        email_field = driver.find_element(By.ID, "email")
        email_field.send_keys(data["email"])

        # Fill the DOB field
        dob_input = driver.find_element(By.ID, "dob")
        dob_input.send_keys(data["dob"])

        # Locate the 4th child with the class 'role-tab' using JavaScript
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

        # Submit the form
        submit_button = driver.find_element(By.CLASS_NAME, "submit-button")
        submit_button.click()
        print(f"Form for {data['fullName']} submitted successfully.")

       # After submitting the signup form, add improved waiting logic for the login page:
        time.sleep(5)  # Small delay after form submission (optional)

        # Navigate to the login page
        driver.get("https://www.manoramaquiz.in/")

        # Wait for the login page to load properly and for the elements to be visible
        wait = WebDriverWait(driver, 10)

        try:
            # Wait for the password field to be visible
            password_field = wait.until(
                EC.visibility_of_element_located((By.ID, "password"))
            )
            password = convert_date(data["dob"])
            password_field.send_keys(password)  # Use converted DOB as password

            # Wait for the username/email field to be visible
            email_login_field = wait.until(
                EC.visibility_of_element_located((By.ID, "username"))
            )
            email_login_field.send_keys(data["email"])  # Use the email from the form data

            # Wait for the submit button to be clickable and submit the form
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


# Main execution
if __name__ == "__main__":
    # JSON file containing form data
    json_file_path = "fake_user_data.json"
    form_data = load_data(json_file_path)

    # Loop through all users in the data
    for user in form_data:
        fill_form(user)
