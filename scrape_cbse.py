from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from csv import writer

def loadPage():
    driver.get("http://cbseaff.nic.in/cbse_aff/schdir_Report/userview.aspx")
    #selecting  "State Wise" radio button
    radio1 = driver.find_element_by_xpath("//input[@id='optlist_2']")
    radio1.click()
    driver.implicitly_wait(WAIT_TIME)

WAIT_TIME = 3
driver = webdriver.Chrome()
loadPage()

for i in range(1,38): #TOTAL_NO_OF_STATES = 38

    #selecting the state
    Select(driver.find_element_by_xpath("//select[@id='ddlitem']")).select_by_index(i)
    driver.implicitly_wait(WAIT_TIME)

    #clicking search button
    driver.find_element_by_xpath("//input[@id='search']").click()
    driver.implicitly_wait(WAIT_TIME)

    #finding the total number of pages to loop
    total_schools = int(driver.find_element_by_xpath("//span[@id='tot']").text)
    total_pages = int(total_schools/25)
    
    for k in range(total_pages):
        print("Page ",k+1,"/",total_pages," of ",Select(driver.find_element_by_xpath("//select[@id='ddlitem']")).first_selected_option.text)
        nextButton = driver.find_element_by_xpath("//input[@id='Button1']")
        driver.execute_script("arguments[0].click();", nextButton)
     
    #reload the page to bypass a bug [check github issue for more details]
    loadPage()
    Select(driver.find_element_by_xpath("//select[@id='ddlitem']")).select_by_index(i)
    driver.implicitly_wait(WAIT_TIME)

driver.close()