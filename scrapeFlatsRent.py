
import pandas as pd 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import re

    
#####zakladni tri sloupce - Nazev, Adresa, Cena_mesic


class Scrapuj: 
    def __init__(self, url):
        self.url = url

    def sosej(self, elementik, jmeno):
        options = Options()
        browser = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\chromedriver_win32\chromedriver.exe', options=options)
        browser.get(self.url)
        soup = BeautifulSoup(browser.page_source, 'lxml')
        time.sleep(4)
        for element in soup.find_all(elementik, class_=jmeno):
            print(element)
            pData = element.text
            #time.sleep(0.5)
            if jmeno == "name ng-binding":
                if "Pronájem" in pData:
                    pole.append(pData)
            else:
                pole.append(pData)





#loopujeme pres stranky
urlAdresa = []
df = pd.DataFrame()
df1 = pd.DataFrame()
  
for j in range(1, 10):
    urlAdresa.append("https://www.sreality.cz/hledani/pronajem/byty/praha?velikost=1%2B1&strana="+str(j))



for i in range(0, len(urlAdresa)):
    pokus = Scrapuj(url = urlAdresa[i])

    #pri i = 0 je treba df vytvorit
    if i == 0:
        pole = [] 
        pokus.sosej(elementik = "span", jmeno = "name ng-binding")
        df['Nazev'] = pole

        pole = [] 
        pokus.sosej(elementik = "span", jmeno = "locality ng-binding")
        df['Adresa'] = pole

        pole = [] 
        pokus.sosej("span", "norm-price ng-binding")
        for k in range(0, len(pole)):
            pole[k] = re.sub('[^0-9]', '', pole[k])
            k += 1

        df['Cena_mesic'] = pole


    #pri i >= 1 je treba k existujicimu df prilepit
    else:
        pole = [] 
        pokus.sosej(elementik = "span", jmeno = "name ng-binding")
        df1['Nazev'] = pole

        pole = [] 
        pokus.sosej(elementik = "span", jmeno = "locality ng-binding")
        df1['Adresa'] = pole

        pole = [] 
        pokus.sosej("span", "norm-price ng-binding")
        for k in range(0, len(pole)):
            pole[k] = re.sub('[^0-9]', '', pole[k])
            k += 1

        df1['Cena_mesic'] = pole
        
        #prilepit a vymazat
        df = df.append(df1, ignore_index = True)
        df1 = pd.DataFrame()
    
    i += 1


#Z Nazev dostat plochu a typ bytu
df['Plocha'] = ""

for j in range(0, len(df['Nazev'])):
    if len( str(df['Nazev'][j]).split() ) == 5:
        df['Plocha'][j] = df['Nazev'][j].split()[-2]
    j += 1
    
df['Typ'] = ""

for j in range(0, len(df['Nazev'])):
    if len( str(df['Nazev'][j]).split()) == 5:
        df['Typ'][j] = df['Nazev'][j].split()[-3]
    j += 1






    
    
    
    
    