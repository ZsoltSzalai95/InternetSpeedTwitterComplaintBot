from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import NoSuchElementException

chrome_driver_path = "C:/Users/.../chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

PROMISED_UP=150
PROMISED_DOWN=100

TWITTER_USER="YOUR_USER"
TWITTER_PASSWORD="YOUR_USER"

TWITTER_URL="https://twitter.com/"
SPEEDNET_URL="https://www.speedtest.net/"

download=10
upload=20

MY_TEXT=f"Hello Internetprovider XY. MY internetspeed is down:{download}, up:{upload}. This is worse compared to your promised down:{PROMISED_DOWN}, up:{PROMISED_UP}"


#Open Speednet and check out internet speed, and save data to variables


driver.get(SPEEDNET_URL)
sleep(2)

driver.find_element_by_css_selector("#_evidon-banner-acceptbutton").click()
sleep(2)

driver.find_element_by_css_selector(".start-text").click()


sleep(60)
download =int(driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
print(download)
upload=int(driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text)
print(upload)


#Compare measured variables to PROMISED service
#SET up condition- if either of the two measured interspeeds (up/down) is lower then promised, LOG IN AND TWEET TO TWITTER!

if upload< PROMISED_UP or download< PROMISED_DOWN:
    driver.get(TWITTER_URL)
    sleep(2)
    driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div").click()
    sleep(2)
    login=driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input").send_keys(TWITTER_USER)
    next_button=driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]/div").click()
    sleep(2)
    password_input=driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input").send_keys(TWITTER_PASSWORD)
    login_TWITTER=driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div").click()
    sleep(4)
    #SEND TWEET
    text_box=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div").send_keys(MY_TEXT)


#CLICK ON TWEET BUTTON


driver.quit()