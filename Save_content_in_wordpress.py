# -*- coding: utf-8 -*-
import urllib
from bs4 import BeautifulSoup
import MySQLdb
#Luu data 1 link
db = MySQLdb.connect(host="127.0.0.1", port=3308, user="root", passwd="", db="pk01",charset='utf8')
c = db.cursor()
url = "http://vanhoc.xitrum.net/thoca/tk18-19/trang/1.html"
req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"}) 
con = urllib.request.urlopen( req )
print(con)
soup = BeautifulSoup(con, 'html.parser')
type(soup)
title = soup.title
print(title.get_text())
text = soup.get_text()
all_links = soup.find_all("p")
c.execute("SELECT id,post_title FROM wp_posts")
a2=0
for id, posttitle in c:
    if a2<id:
        a2=id
print('-----------------------')
pk=soup.findAll("table", {"border":"0", "width":"90%","cellpadding":"3","cellspacing":"0"})
a=a2
s1=title.get_text()
for l in pk:
    a=a+1
    print(l.get_text())
    l1=l.get_text()
    #l1="Tuy Dep trai"
    if l1.find("Xem tiếp") < 0 :
        sql=f"INSERT INTO `wp_posts`(`ID`, `post_author`, `post_date`, `post_date_gmt`,`post_modified`,`post_modified_gmt`,`post_excerpt`, `post_content`, `post_title`, `post_name`, `guid`,`to_ping`,`pinged`,`post_content_filtered`) VALUES ({a},1,NOW(),NOW(),NOW(),NOW(),'','{l1}','{s1}',{a},'http://localhost8012/phongkham01/?p={a}','','','')"
        c.execute(sql)
        db.commit()
