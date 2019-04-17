from bs4 import BeautifulSoup
from csv import writer
import re

with open('details.csv','w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Name','Address','Phone','Email']
    csv_writer.writerow(headers) 

    soup = BeautifulSoup(open('samplePage.txt'),'html.parser')
    
    #rows will contain exactly 26 results of which 1st entry is the header
    rows = soup.select("table#T1 > tbody > tr > td > table")
    rows.pop(0) #removes header table
    for row in rows:
        col1 = row.select("tbody > tr > td")[1]
        col2 = row.select("tbody > tr > td")[2]

        name = col1.select("tbody > tr a")[0].getText()
        # re.sub(r"[\n\t\s]*", "", str) is used to strip whitespace, tab and newline from str
        address = re.sub(r"[\n\t]*", "", col2.select("table > tbody > tr")[0].getText()[9:])
        phone = re.sub(r"[\n\t]*", "", col2.select("table > tbody > tr")[1].getText()[10:])
        email = re.sub(r"[\n\t\s]*", "", col2.select("table > tbody > tr")[2].getText()[8:])
        
        csv_writer.writerow([name,address,phone,email])    