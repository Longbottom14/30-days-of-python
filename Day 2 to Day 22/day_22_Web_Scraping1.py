import requests
from bs4 import BeautifulSoup

url_uci ='https://archive.ics.uci.edu/ml/datasets.php'

response = requests.get(url_uci)

soup = BeautifulSoup(response.content,'lxml')

tables = soup.find("table",{'cellpadding':'3'}).find_all("td",{'valign':'top'})

table_rows =[]
for table in tables:
    table_content = table.find_all("table",{'border':'1','cellpadding':'5'})
    #for t in table_content:
        #headers = t.find("tr",{'bgcolor':"#003366"})
            #print(t.prettify())
            #print()
            #print('####################')
            #table_rows.append(t)

#print(table_content)
headers = table_content.find("tr",{'bgcolor':"#003366"})
head = headers.td.p.a
print(head)

