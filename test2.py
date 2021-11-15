from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
print("test case started")
#open Google Chrome browser
driver = webdriver.Chrome()
#maximize the window size
driver.maximize_window()
#delete the cookies
driver.delete_all_cookies()
#navigate to the url
driver.get("https://www.gmail.com")
#identify the user name text box and enter the value
driver.find_element_by_id("identifierId").send_keys("aniketshawtest@gmail.com")
time.sleep(2)
#click on the next button
driver.find_element_by_xpath("//span[@class='VfPpkd-vQzf8d'][1]").click()
time.sleep(3)
#identify the password text box and enter the value
driver.find_element_by_name("password").send_keys("Ani@1221")
time.sleep(3)
#click on the next button
# if NEXT class required --->
# <span jsname="V67aGc" class="VfPpkd-vQzf8d">Next</span>
driver.find_element_by_xpath("//span[contains(text(),'Next')][1]").click()
time.sleep(10)
#close the browser
driver.close()