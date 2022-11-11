# Used to import the webdriver from selenium
from selenium import webdriver
import os


# Get the path of chromedriver which you have install

def startBot(username, password, url):
    chrome_driver_path = "/Users/Ashita Aswal/Downloads/chromedriver_win32"


    # giving the path of chromedriver to selenium webdriver
    driver = webdriver.Chrome(chrome_driver_path+"\\chromedriver.exe")

    # opening the website in chrome.
    driver.get("https://www.naukri.com/nlogin/login")

    # find the id or name or class of
    # username by inspecting on username input
    driver.find_element_by_name(
        "id/class/ashitaaswal8@gmail.com").send_keys(username)

    # find the password by inspecting on password input
    driver.find_element_by_name(
        "id/class/ashita8").send_keys(password)

    # click on submit
    driver.find_element_by_css_selector(
        "id/class/name/css selector of login button").click()


# Driver Code
# Enter below your login credentials
username = "ashitaaswal8@gmail.com"
password = "ashita8"

# URL of the login page of site
# which you want to automate login.
url = "Enter the URL of login page of website"

# Call the function
startBot(username, password, url)
