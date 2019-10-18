#!/usr/bin/env python3
# Command-Line Emailer
# Requires selenium and https://github.com/mozilla/geckodriver/.
# And Firefox.
# GMail credentials should be saved in login.json:
# {"username": "", "password": ""}


import json
import sys
import argparse
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

parser = argparse.ArgumentParser(
    description=("Sends an email to a given address from a GMail account.")
)
parser.add_argument("recipient", type=str, help="address to send the email to")
parser.add_argument("body", type=str, nargs=argparse.REMAINDER, help="email body")
args = parser.parse_args()

try:
    with open("login.json") as file:
        login = json.load(file)
except IOError:
    print("Failed to load email credentials!")
    sys.exit(1)

# Go to the login page.
url = (
    "https://accounts.google.com/AccountChooser?service=mail&continue="
    "https://mail.google.com/mail/"
)
driver = webdriver.Firefox()
while True:
    driver.get(url)

    # Sign in.
    login_field = driver.find_element_by_name("identifier")
    login_field.send_keys(login["username"])
    login_field.send_keys(Keys.ENTER)

    password_field_name = "password"
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, password_field_name))
    )

    password_field = driver.find_element_by_name(password_field_name)
    password_field.send_keys(login["password"])
    password_field.send_keys(Keys.ENTER)

    try:
        WebDriverWait(driver, 10).until(EC.title_contains(login["username"]))
        break
    except TimeoutException:
        print("Timed out. Attempting to sign in again.")

# Compose the email.
# Use a keyboard shortcut for Compose.
root = driver.find_element_by_tag_name("html")
root.send_keys("c")

# Wait for the new message window.
to_field_name = "to"
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, to_field_name))
)

to_field = driver.find_element_by_name(to_field_name)
to_field.send_keys(args.recipient)

subject_field = driver.find_element_by_name("subjectbox")
subject_field.send_keys("Hi from Python!")

body_field = driver.find_element_by_xpath("//div[contains(@class, 'editable')]")
body_field.send_keys(" ".join(args.body))

# Send.
body_field.send_keys(Keys.CONTROL + Keys.ENTER)

time.sleep(5)
driver.close()
