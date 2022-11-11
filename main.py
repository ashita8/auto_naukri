
from selenium import webdriver as wb
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/Ashita Aswal/Downloads/chromedriver_win32" 
#path where your chrome driver is.

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
driver = wb.Chrome(chrome_driver_path+"\\chromedriver.exe")

Skillset = ['Analysis','Python','SQL']
Skillset = [x.lower() for x in Skillset]

driver.get("https://www.naukri.com/software-developer-web-developer-jobs?k=software%20developer%2C%20web%20developer&experience=0&ctcFilter=6to10&ctcFilter=10to15&ctcFilter=15to25&functionAreaIdGid=5&ugTypeGid=12")
#you can change the above url as per yr preference
login_button = driver.find_element_by_link_text("Login")
login_button.click()


WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[3]/div[2]/div[2]/div/div[2]/div/form/div[2]/input'))).click()

driver.find_element_by_xpath('//*[@id="root"]/div[3]/div[2]/div[2]/div/div[2]/div/form/div[2]/input').send_keys("userid/emailid")
driver.find_element_by_xpath('//*[@id="root"]/div[3]/div[2]/div[2]/div/div[2]/div/form/div[3]/input').send_keys("password")

driver.find_element_by_xpath('//*[@id="root"]/div[3]/div[2]/div[2]/div/div[2]/div/form/div[6]/button').click()

time.sleep(5)
listofJobs = driver.find_elements_by_xpath('//*[@id="root"]/div[4]/div/section[2]/div[2]/article')
print("Lenght of Job List: ",len(listofJobs))
count=0
for i in listofJobs:
    try:
        if count < 10:
            i.click()
            driver.switch_to_window(driver.window_handles[1])
            apply = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="root"]/main/div[2]/div[2]/section[1]/div[1]/div[3]/div/button[2]')))
            print(apply.text)
            if apply.text == "APPLY ON COMPANY SITE":
                print("Automation will not go to Company Site")
            else:
                apply.click()
                count = count + 1
            time.sleep(5)
            driver.close()
            time.sleep(1)
            driver.switch_to_window(driver.window_handles[0])
        else:
            break

    except:
        print("i am on except")
        driver.close()
        driver.switch_to_window(driver.window_handles[0])


