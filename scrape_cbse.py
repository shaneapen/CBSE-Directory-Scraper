from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from csv import writer

def loadPage():
    driver.get("http://cbseaff.nic.in/cbse_aff/schdir_Report/userview.aspx")
    #selecting  "State Wise" radio button
    radio1 = driver.find_element_by_xpath("//input[@id='optlist_2']")
    radio1.click()
    driver.implicitly_wait(5)

driver = webdriver.Chrome()
loadPage()

for i in range(1,38): #TOTAL_NO_OF_STATES = 38
    
    state = Select(driver.find_element_by_xpath("//select[@id='ddlitem']"))
    state.select_by_index(i)
    driver.implicitly_wait(5)

    district = Select(driver.find_element_by_xpath("//select[@id='DropDownDistrict']"))
    districtCount = len(district.options)
    print("District count=",districtCount)

    for j in range(1,districtCount-1):
        
        district = Select(driver.find_element_by_xpath("//select[@id='DropDownDistrict']"))
        district.select_by_index(j)
        driver.implicitly_wait(5)

        #clicking search button
        driver.find_element_by_xpath("//input[@id='search']").click()
        driver.implicitly_wait(5)

        #loop through the pages
        total_schools = int(driver.find_element_by_xpath("//span[@id='tot']").text)
        total_pages = int(total_schools/25)
        print("PAGES=",total_pages)

        for k in range(total_pages):
            nextButton = driver.find_element_by_xpath("//input[@id='Button1']")
            driver.execute_script("arguments[0].click();", nextButton)
        
        #reload the page to bypass a bug [check github issue for more details]
        loadPage()
        state = Select(driver.find_element_by_xpath("//select[@id='ddlitem']"))
        state.select_by_index(i)
        driver.implicitly_wait(5)

driver.close()
