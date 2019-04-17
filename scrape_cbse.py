from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from csv import writer
import re

def loadPage():
    driver.get("http://cbseaff.nic.in/cbse_aff/schdir_Report/userview.aspx")
    #selecting  "State Wise" radio button
    radio1 = driver.find_element_by_xpath("//input[@id='optlist_2']")
    radio1.click()
    driver.implicitly_wait(WAIT_TIME)

WAIT_TIME = 3
driver = webdriver.Chrome()
loadPage()

with open('COMPLETE.csv','w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Name','Address','Phone','Email','State']
    csv_writer.writerow(headers) 

    for i in range(1,38): #TOTAL_NO_OF_STATES = 38

        #selecting the state
        Select(driver.find_element_by_xpath("//select[@id='ddlitem']")).select_by_index(i)
        driver.implicitly_wait(WAIT_TIME)

        #clicking search button
        driver.find_element_by_xpath("//input[@id='search']").click()
        driver.implicitly_wait(WAIT_TIME)

        #finding the total number of pages to loop
        total_schools = int(driver.find_element_by_xpath("//span[@id='tot']").text)
        total_pages = int(total_schools/25) + 1

        for k in range(total_pages):
            print("Page ",k+1,"/",total_pages," of ",Select(driver.find_element_by_xpath("//select[@id='ddlitem']")).first_selected_option.text," (",i,")")
            soup = BeautifulSoup(driver.page_source,'html.parser')
    
            #rows will contain atmost 26 results of which 1st entry is the header
            rows = soup.select("table#T1 > tbody > tr > td > table")
            rows.pop(0) #removes header table
            state = Select(driver.find_element_by_xpath("//select[@id='ddlitem']")).first_selected_option.text
            for row in rows:
                col1 = row.select("tbody > tr > td")[1]
                col2 = row.select("tbody > tr > td")[2]

                name = col1.select("tbody > tr a")[0].getText()
                # re.sub(r"[\n\t\s]*", "", str) is used to strip whitespace, tab and newline from str
                address = re.sub(r"[\n\t]*", "", col2.select("table > tbody > tr")[0].getText()[9:])
                phone = re.sub(r"[\n\t]*", "", col2.select("table > tbody > tr")[1].getText()[10:])
                email = re.sub(r"[\n\t\s]*", "", col2.select("table > tbody > tr")[2].getText()[8:])
                
                csv_writer.writerow([name,address,phone,email,state])    
            #goto next page
            nextButton = driver.find_element_by_xpath("//input[@id='Button1']")
            driver.execute_script("arguments[0].click();", nextButton)

        #reload the page to bypass a bug [check github issue for more details]
        loadPage()
        Select(driver.find_element_by_xpath("//select[@id='ddlitem']")).select_by_index(i)
        driver.implicitly_wait(WAIT_TIME)

driver.close()