#!/usr/bin/env python3
# 2048
# Requires selenium and https://github.com/mozilla/geckodriver/.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox()
driver.get("https://play2048.co/")

while True:
    root = driver.find_element_by_xpath("html")
    root.send_keys(Keys.UP)
    root.send_keys(Keys.RIGHT)
    root.send_keys(Keys.DOWN)
    root.send_keys(Keys.LEFT)
    try:
        if driver.find_element_by_link_text("Try again"):
            print("Game Over!")
            break
    except NoSuchElementException:
        pass
