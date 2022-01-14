import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# This testing program will login into Udemy with using url, inputting values, and clicking submit button. It should then able to login you in.
# working on conditional commands (status)

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver")

driver.get("https://www.udemy.com/join/login-popup/?skip_suggest=1&locale=en_US&next=https%3A%2F%2Fwww.udemy.com%2Flogout%2F&response_type=html")

ele1 = driver.find_element_by_name("email")

print(ele1.is_displayed()) # returns true/false based on element status ele1 = username

print(ele1.is_enabled()) # returns true/false

ele2 = driver.find_element_by_name("password")

print(ele2.is_displayed()) # returns true/false based on element status ele2 = password

print(ele2.is_enabled()) # returns true/false

ele1.send_keys("") #input username (for protection: make sure you don't share program with sensitive information, do it at your own private time
ele2.send_keys("") #input password (for protection: make sure you don't share program with sensitive information, do it at your own private time

ele3 = driver.find_element_by_name("submit").click() #click functon by clicking submit after creds are inserted

#time.sleep(5)

#driver.quit() #Closes all the browsers
