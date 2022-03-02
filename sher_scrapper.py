import requests
from bs4 import BeautifulSoup
global json_content
import sqlite3
conn = sqlite3.connect("khusrau.db")

cur = conn.cursor()
blues_words=["","",""]
tag_strip=['wafa', 'Wahm', 'Wahshat', 'Waiz', 'Wajood', 'Waqt', 'Welcome', 'Yaad', 'Yaad-e-Raftagan', 'Zindagi', 'zindan', 'Zulf']

top100=['https://rekhta.org/tags/wafa-shayari', 'https://rekhta.org/tags/wahm-shayari', 'https://rekhta.org/tags/wahshat-shayari', 'https://rekhta.org/tags/waiz-shayari', 'https://rekhta.org/tags/wajood-shayari', 'https://rekhta.org/tags/waqt-shayari', 'https://rekhta.org/tags/welcome-shayari', 'https://rekhta.org/tags/yaad-shayari', 'https://rekhta.org/tags/yaad-e-raftagan-shayari', 'https://rekhta.org/tags/zindagi-shayari', 'https://rekhta.org/tags/zindan-shayari', 'https://rekhta.org/tags/zulf-shayari']
url="https://rekhta.org/Top-20-Ishq-Sher"
for m in range(0,len(top100)):
    net_url=url+top100[m]
    page = requests.get(top100[m])
    soup = BeautifulSoup(page.content, 'lxml')
    #tree = html.fromstring(page.content)
    meaning_api="https://rekhta.org/Api_ShowMeaning/?id="
    x=0
    poem_title=soup.find("title").get_text()
    print(poem_title)
    #poem_author = soup.find(class_="ghazalAuthor")
    #print(poem_author.get_text())
    word_id=[]
    desc=[]
    word_meaning=""
    sentence1=""
    sentence0=""
    trans=""
    trans_trim=""
    list1=""
    list0=""
    tags_net=""
    poem_raw = soup.find(class_="left_pan pageContentContainer")
    poem_couplet = poem_raw.find_all(class_=" nw_ghazalCard")
    #cur.execute("INSERT INTO ghazal VALUES (?, ?, ?, ?, ?, ?);", (poem_title,poem_author.get_text(),net_url,None,None,None))
    #cur.execute("INSERT INTO author VALUES (?, ?, ?, ?, ?);", (poem_author.get_text(), None, None, None, None))
    for y in range(0,len(poem_couplet)):                             #finds sher
          print(y)
          tag_container = poem_couplet[y].find(class_="tagContainingList")
          if tag_container is not None:
              tags = tag_container.find_all("li")
          else: tags=["yo"]
          lower=poem_couplet[y].find(class_="OptContainingList")
          blues=lower.find_all(class_="skyblue")
          full_g=lower.find(class_="ReadFull")
          for z in range (0,len(blues)):
              blues_words=blues[0].get_text()
              #print(blues_words)
              if blues_words == 'TRANSLATION':
                 blues.pop(0)
          print(blues[0].get_text())
          author_id=blues[0].get_text()
          full_ghazal="https://rekhta.org"+blues[-1]["href"]
          print(full_ghazal)
          couplet = poem_couplet[y]
          poem_line = couplet.find(class_="PContainer")
          for q in range(1, len(tags)):
              tag_sing=tags[q].get_text()
              #tag_length = len(tag_single)
              #print(tag_single[-3])
              if tag_sing[-3] is ",":
                  tag_list=list(tag_sing)
                  tag_list[-3]=""
                  tag_s = ''.join(tag_list)
                  tag_single = tag_s.strip()
              else: tag_single=tag_sing
              tags_net+= tag_single + " + "
          tags_net += tag_strip[m]
          print(tags_net)
          #print(poem_line)
          #for g in range(0,len(poem_line)):
          line = poem_line.find_all(class_="DivLine")
          #print(line)
          for h in range(0, len(line)):                              #finds line
            single_line=line[h]
            #print(h)
            poem_text = single_line.find_all(class_="WM")
            for x in range(0, len(poem_text)):                        #finds words
               poem_word=poem_text[x]
               word=poem_word.get_text()
               word_id=poem_word['data-key']
               meaning_url= meaning_api + word_id + "&lang=0"
               #print(meaning_url)
               meaning_page = requests.get(meaning_url)
               meaning_soup = BeautifulSoup(meaning_page.content, 'lxml')
               meaning_panel= meaning_soup.find(class_="MeaningBoxWrap")
               #print(meaning_panel)
               meaning_lang= meaning_panel.find_all('li')
               #print(meaning_lang[2].get_text())
               word_meaning+= meaning_lang[0].get_text() + " | " +meaning_lang[1].get_text() + " | "+ meaning_lang[2].get_text()
               #print(word_meaning)
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
               cur.execute("INSERT INTO words VALUES (?, ?, ?);", (word_id, word, word_meaning))  # word inserter
               word_meaning = ""
               #conn.commit()
          #cur.execute("INSERT INTO sher2ghazal VALUES (?, ?, ?);", (poem_title,y,sentence0))   #sher2ghazal inserter

          trans_couplet = couplet.find(class_="DivLineSmall PoemImageHost ImageTranslationHost")
          if (trans_couplet is not None):
              trans = trans_couplet.contents[0] + " + " + trans_couplet.contents[-1]
              trans_trim=trans.strip()
          print(sentence0)
          print(top100[m])
          print(sentence1)
          #print(trans_couplet.contents[2])
          cur.execute("INSERT INTO t20_sher VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",(sentence0, sentence0, list0, sentence1, list1, author_id, tags_net, full_ghazal, trans_trim, y, None))  #sher inserter
          sentence1 = ""
          sentence0 = ""
          trans = ""
          trans_trim = ""
          tags_net = ""
          list0 = ""
          list1 = ""
    #page=None
    conn.commit()

conn.close()
