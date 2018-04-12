from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import select as Select
import time
usernameStr = 'YourIDHere'
passwordStr = 'YourPasswordHere'

browser = webdriver.Firefox()
browser.get(('http://egovernance/Egovwebapp/home.aspx'))



username = browser.find_element_by_id('txtUserName')
username.send_keys(usernameStr)

password = browser.find_element_by_id('txtPassword')

password.send_keys(passwordStr)

signInButton = browser.find_element_by_id('ibtnLogin')
signInButton.click()
time.sleep(3)
body=browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
browser.get('http://egovernance/Egovwebapp/SIS/frmFacultyFeedback.aspx')
#if not(signInButton ==''):
    #browser2 = webdriver.Chrome()
    #browser.get(('http://egovernance/Egovwebapp/frmUserProfile.aspx'))
    #egov = browser.find_element_by_name("dlAppList$ctl00$ctl00")
    #egov.click()
    #driver.send_keys(Keys.CONTROL + 'T')
    #elem = browser.find_element_by_xpath("/html/body/div[2]/div[4]/div/a") #href link
    #time.sleep(2) 
    #elem.send_keys(Keys.CONTROL + Keys.RETURN + "2")
drp=Select(browser.find_element_by_class_name('FormDL'))
drp.select_by_value("5619")

    
    
