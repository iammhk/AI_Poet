from lxml import html
import requests
import json
from bs4 import BeautifulSoup
import sys
global json_content
import sqlite3
conn = sqlite3.connect("khusrau.db")

cur = conn.cursor()

top100=["/ghazals/koii-din-gar-zindagaanii-aur-hai-mirza-ghalib-ghazals"]
url="https://rekhta.org"
for m in range(0,len(top100)):
    net_url=url+top100[m]
    page = requests.get(net_url)
    soup = BeautifulSoup(page.content, 'lxml')
    #tree = html.fromstring(page.content)
    meaning_api="https://world.rekhta.org/api/v2/shayari/GetWordMeaning?lang=1"
    x=0
    poem_title=soup.find("title").get_text()
    print(poem_title)
    poem_author = soup.find(class_="ghazalAuthor")
    print(poem_author.get_text())
    word_id=[]
    desc=[]
    sentence1=""
    sentence0=""
    translate=""
    list1=""
    list0=""
    poem_raw = soup.find(class_="pMC")
    poem_couplet = poem_raw.find_all(class_="w")
    cur.execute("INSERT INTO ghazal VALUES (?, ?, ?, ?, ?, ?);", (poem_title,poem_author.get_text(),net_url,None,None,None))
    cur.execute("INSERT INTO author VALUES (?, ?, ?, ?, ?);", (poem_author.get_text(), None, None, None, None))
    for y in range(0,len(poem_couplet)):                             #finds sher
          print(y)
          couplet = poem_couplet[y]
          poem_line = couplet.find(class_="c")
          #for g in range(0,len(poem_line)):
          line = poem_line.find_all("p")
          for h in range(0, len(line)):                              #finds line
            single_line=line[h]
            #print(h)
            poem_text = single_line.find_all("span")
            for x in range(0, len(poem_text)):                        #finds words
               poem_word=poem_text[x]
               word=poem_word.get_text()

               word_id=poem_word['data-m']
               #print(word_id)
               l = {'Word':word_id}
               url = 'https://world.rekhta.org/api/v2/shayari/GetWordMeaning?lang=1'

               json_content = requests.post(url, l)
               word_json=json_content.json()
               #word=word_json['R']
               #eng=word['E']
               word_json = json.dumps(word_json)
               if h is 0:
                   sentence0 += word
                   sentence0 += " "
                   list0 += word_id
                   list0 += " "
               else:
                   sentence1+=word
                   sentence1+=" "
                   list1 += word_id
                   list1 += " "
                   #print(word, end=' ')
               cur.execute("INSERT INTO words VALUES (?, ?, ?);", (word_id, word, word_json))  # word inserter
               #conn.commit()
          cur.execute("INSERT INTO sher2ghazal VALUES (?, ?, ?);", (poem_title,y,sentence0))   #sher2ghazal inserter

          trans_couplet = couplet.find(class_="t")
          if (trans_couplet is not None):
              trans = trans_couplet.find_all("p")
              for h in range(0, len(line)):
                  single_line = trans[h]
                  # print(h)
                  poem_text = single_line.find_all("span")
                  for x in range(0, len(poem_text)):
                      poem_word = poem_text[x]
                      desc = poem_word.get_text()
                      translate += desc
                      translate += " "
                  translate+="+"
          print(sentence0)
          print(list0)
          print(sentence1)
          print(list1)
          cur.execute("INSERT INTO sher VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",(sentence0, sentence0, list0, sentence1, list1, poem_author.get_text(), None, translate, None, None))  #sher inserter
          sentence1 = ""
          sentence0 = ""
          translate = ""
          list0 = ""
          list1 = ""
    page=None
    conn.commit()

conn.close()




















        #meaning_url= meaning_api + word_id + "&lang=0"
        #print(meaning_url)
        #meaning_page = requests.get(meaning_url)
        #json_content= meaning_page.json()
        #print(json_content['Hi'], end=' ')
        #f.writerow([json_content['En'],json_content['Hi'],json_content['Ur'],json_content['Enm'],json_content['Him'],json_content['Urm']])
        #f = csv.writer(open("test.csv"))
     # with open('poem.csv', 'w') as csvfile:
      #      fieldnames = ["En", "Hi", "Ur", "Enm", "Him" , "Urm"]
      #f = csv.DictWriter(csvfile, fieldnames=fieldnames)
      # Write CSV Header, If you dont need that, remove this line
      #f.writerow(["En", "Hi", "Ur", "Enm", "Him" , "Urm"])

      #for json_content in json_content:
      #f.writerow([json_content['En'],json_content['Hi'],json_content['Ur'],json_content['Enm'],json_content['Him'],json_content['Urm']])
      #data= json.loads(json_content.decode("utf8"))
      #print(data)
            #word_meaning= data['En']['Hi']['Ur']['Enm']
      #print(data)


#print(word_id)
#soup = BeautifulSoup(page.content)
#print(soup.find_all('li'))