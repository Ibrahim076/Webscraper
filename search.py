from ast import Num
from pydoc import pager
import site
from jmespath import search
from requests import Session
from bs4 import BeautifulSoup
from bs4.element import Tag
import csv
import pandas as pd
from urllib.parse import urlparse



df = pd.DataFrame(columns=['url'])
with open("urls.csv", "w", newline="") as url_file:
    url_output = csv.writer(url_file)
    url_output.writerow(['url'])

    with open('keywords.csv', 'r') as fp:   
        # # check of er meerdere pagina's zijn
        # # num = 100
        # # start = 100*(page-1)
        # page = 1
        # num = 100
        # maxpage = num*(page -1)


        for keyword in fp.read():
            params = {"q": keyword, 'gl': 'NL', 'num': 100}
            headers = {
                "User-Agent":
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.147 Safari/537.36"
            }
        with Session() as session:
            r = session.get(
                "https://google.com/search", params=params, headers=headers, timeout=5)

            soup = BeautifulSoup(r.content, 'lxml')

            result_div = soup.find_all('div', attrs={'class': 'g'})

   

           
         

            links = []
        


    
            for r in result_div:
                try:
                    link = r.find('a', href=True)
                    if link != '': 
                        domain = urlparse(link['href']).netloc
                        if domain not in links:
                            links.append(domain.replace('nl.', '').replace('www.', ''))
                     

                except Exception as e:
                    print(e)
                    continue
            
           
            for link in links:
                url_output.writerow([link])
pass