#Lay data 1 link
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
from urllib.request import urlopen
from bs4 import BeautifulSoup
###
url1 = 'http://vanhoc.xitrum.net/thoca/hiendai/6188.html'
html = urlopen(url1)
soup = BeautifulSoup(html, 'html.parser')
type(soup)
title = soup.title
print(title.string)
text = soup.get_text()
soup.find_all('a')
text = soup.get_text()
all_h1 = soup.find_all("div", class_="title", text=True, recursive=False)
for a_h1 in all_h1:
    print(a_h1)
all_h2 = soup.find_all("div", class_="small", text=True, recursive=False)
for a_h2 in all_h2:
    print(a_h2)  
all_h3 = soup.find_all("table", {"border":"0", "width":"90%","cellpadding":"3","cellspacing":"0"})
for a_h3 in all_h3:
    print(a_h3)      
