from lxml import html+
import requests
import csv
import json

from bs4 import BeautifulSoup
from selenium import webdriver
import sqlite3
#conn = sqlite3.connect("khusrau.db")

#c = conn.cursor()



driver = webdriver.Chrome('C:\chromedriver.exe')
driver.get("https://rekhta.org/couplets")
#page = requests.get("https://rekhta.org/topreadpoets")
html = driver.page_source
soup = BeautifulSoup(html,"lxml")
#page = requests.get("https://rekhta.org/poets/mirza-ghalib")
#soup = BeautifulSoup(page.content, 'lxml')
#tree = html.fromstring(page.content)
x=0
gazal_links=[]

poet=["Adil Mansuri", "Ahmad Faraz", "Ahmad Mushtaq", "Ahmad Nadeem Qasmi", "Aitbar Sajid", "Akbar Allahabadi", "Akhtar Shirani", "Akhtar ul Iman", "Ali Sardar Jafri", "Allama Iqbal", "Ameer Minai", "Asrar ul Haq Majaz", "Bahadur Shah Zafar", "Bashir Badr", "Dagh Dehlvi", "Faiz Ahmad Faiz", "Firaq Gorakhpuri", "Gulzar", "Hafeez Jalandhari", "Hasrat Mohani", "Jaun Eliya", "Jigar Moradabadi", "Kaifi Azmi", "Khumar Barabankavi", "Majrooh Sultanpuri", "Mir Taqi Mir", "Mirza Ghalib", "Momin Khan Momin", "Munawwar Rana", "Muneer Niyazi", "Nasir Kazmi", "Nida Fazli", "Noon Meem Rashid", "Obaidullah Aleem", "Parveen Shakir", "Qateel Shifai", "Rahat Indori", "Saghar Siddiqui", "Sahir Ludhianvi", "Saleem Kausar", "Sauda Mohammad Rafi", "Shad Azimabadi", "Shahryar", "Shakeel Badayuni", "Waseem Barelvi", "Zafar Iqbal"]
poet_url=[]
tag_names=[]
t20 = soup.find(class_=" right-tag-menu")
#print(t20)
poet_raw= t20.find_all("a")
#poem_raw = soup.find(class_="k-widget k-grid")
#print(poet_raw)
for y in range (0, len(poet_raw)):
    p_list=poet_raw[y]
    #poet_list = p_list.find('a').get_text()
    poet_url.append("https://rekhta.org"+ p_list['href'])
    tags=p_list.get_text()
    tag_names.append(tags.strip())
    #desc = p_list.find_all('a')
    #des=desc[1].get_text()
    #url="https://rekhta.org"+poet_url["href"]
print(tag_names)
    #print(poet[y-1])
    #print(poet_list)
    #c.execute("INSERT INTO author VALUES (?, ?, ?, ?, ?);",(poet[y-1], poet_list, url, None, None))
    # Save (commit) the changes
#conn.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
#conn.close()
#    for x in range(0, len(poet_list)):
#        poet_name = poet_list[x]
#        desc = poet_name.string
#        print(desc)
#print(poet_raw)
#webpage = html.fromstring(page.content)
#list=webpage.xpath('//a/@href')
#print(poem_list)
#poem_list = poet_raw.find_all(class_="isNewContainer poetImageInGrid2")
#print(poem_list)
#for link in poet_raw.findAll('a'):
 #   print (link.get('href'))


#print(word_id)
#soup = BeautifulSoup(page.content)
#print(soup.find_all('li'))