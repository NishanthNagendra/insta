from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver import ActionChains as ac
import pyautogui
import os
import time
user = ""
pwd = ""
category = input('Enter a category : ')
url = "https://www.instagram.com/accounts/login/?source=auth_switcher"
cOptions = ChromeOptions()
# Start in fullscreen, incognito and user agent as iphone
cOptions.add_argument("--start-maximized")
cOptions.add_argument("--incognito")
cOptions.add_argument('--user-agent="Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"')
driver = webdriver.WebDriver(executable_path="chromedriver.exe", chrome_options=cOptions)
driver.delete_all_cookies()
driver.get(url)
wait = WebDriverWait(driver, 10)
assert "Instagram" in driver.title
# To input username and password
driver.implicitly_wait(2)
element_present = wait.until(EC.visibility_of_element_located((By.NAME, 'username')))
elem = driver.find_element_by_name('username')
elem.send_keys(user)
elem = driver.find_element_by_name('password')
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
# To click not now button
element_present = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/button')))
elem = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/button')
elem.click()
# To click on upload button
element_present = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav[2]/div/div/div[2]/div/div/div[3]/span')))
elem = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav[2]/div/div/div[2]/div/div/div[3]/span')
elem.click()
time.sleep(1)
path = os.getcwd() + "\\005.jpeg"
pyautogui.typewrite(path, interval = 0.01)
pyautogui.hotkey('alt', 'O')
# To zoom out the picture
element_present = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="react-root"]/section/div[2]/div[2]/div/div/div/button[1]/span')))
button_parent = driver.find_element_by_xpath('//*[@id="react-root"]/section/div[2]/div[2]/div/div/div/button[1]/span')
ac(driver).move_to_element(button_parent).click(button_parent).perform()
# To click on next
element_present = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="react-root"]/section/div[1]/header/div/div[2]/button')))
elem = driver.find_element_by_xpath('//*[@id="react-root"]/section/div[1]/header/div/div[2]/button')
elem.click()
# Open a new tab
pyautogui.hotkey('ctrl', 't')
hashurl = "https://www.all-hashtag.com/hashtag-generator.php"
driver.switch_to.window(driver.window_handles[1])
driver.get(hashurl)
# To enter the category
element_present = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="keyword"]')))
elem = driver.find_element_by_xpath('//*[@id="keyword"]')
elem.send_keys(category)
# To choose top option
element_present = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="header-gen-form"]/fieldset/label[1]')))
button_parent = driver.find_element_by_xpath('//*[@id="header-gen-form"]/fieldset/label[1]')
ac(driver).move_to_element(button_parent).click(button_parent).perform()
# To click generate button
element_present = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="header-gen-form"]/button')))
button_parent = driver.find_element_by_xpath('//*[@id="header-gen-form"]/button')
ac(driver).move_to_element(button_parent).click(button_parent).perform()
# To copy hashtags
element_present = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="copy-hashtags"]')))
button_parent = driver.find_element_by_xpath('//*[@id="copy-hashtags"]')
hashtags = button_parent.text
pyautogui.hotkey('ctrl', 'f4')
# Switch focus to first tab
driver.switch_to.window(driver.window_handles[0])
element_present = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="react-root"]/section/div[2]/section[1]/div[1]/textarea')))
elem = driver.find_element_by_xpath('//*[@id="react-root"]/section/div[2]/section[1]/div[1]/textarea')
elem.send_keys(hashtags)
element_present = EC.visibility_of_element_located((By.XPATH, '//*[@id="react-root"]/section/div[1]/header/div/div[2]/button'))
elem = driver.find_element_by_xpath('//*[@id="react-root"]/section/div[1]/header/div/div[2]/button')
elem.click()
# driver.close()
