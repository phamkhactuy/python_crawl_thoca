import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
from urllib.request import urlopen
from bs4 import BeautifulSoup
###
import MySQLdb
db = MySQLdb.connect(host="127.0.0.1", port=2017, user="root", passwd="Quynh307", db="PKTUY")
c = db.cursor()
a1="http://vanhoc.xitrum.net/thoca/"
c.execute("SELECT url,datcre FROM thoca")
a2=0
for url,datcre in c:
    if url.startswith('http://vanhoc.xitrum.net/thoca/'):
        a2=a2+1
        #print(f'{a2} URL: {url}:{datcre}')
        url1 = url
        html = urlopen(url)
        soup = BeautifulSoup(html, 'html.parser')
        type(soup)
        title = soup.title
        print(title)
        text = soup.get_text()
        soup.find_all('a')
        all_links = soup.find_all("a")
        for link in all_links:
            #print(link.get("href"))
            a1=link.get("href")
            ax=f"http://vanhoc.xitrum.net{a1}"
            sql=f"insert into thoca values('{ax}',NOW())"
            c.execute(sql)
        db.commit()

#print(c.fetchone())
