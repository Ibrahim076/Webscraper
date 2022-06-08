from cgitb import html
from urllib.parse import urlparse
import json
from traceback import print_stack
from unittest import main
from urllib import response
import requests_html
import time
from idna import ulabel
from numpy import append 
import requests
import csv
import urllib.parse
import urllib.request
import sys
from bs4 import BeautifulSoup
import search

if __name__ == '__main__':
    search
print(f"scraping keywords")
with open("urls.csv", "r") as urls, open("results.csv", "w", newline="") as f_output:
    print(f"reading urls file")
    sites = csv.reader(urls, delimiter=',')
    output = csv.writer(f_output)
    output.writerow(['url', 'Magento'])
    print(f"writing headers to file")
    for site in sites:
        if site[0] != 'url':
            proxies = {
                'https:':'103.152.117.110:9812',
                'http':'208.113.134.223:80'
            }
            try:
                css_file = []
                js_file = []
                proxy_support = urllib.request.ProxyHandler(proxies)
                opener = urllib.request.build_opener(proxy_support)
                urllib.request.install_opener(opener)
                r = urllib.request.Request('https://'+site[0],headers={'User-Agent': 'Mozilla/5.0'})
                print(site[0])
                with urllib.request.urlopen(r) as o:
                    b = o.read()
                    s = b.decode("utf-8")
                    soup = BeautifulSoup(s, 'lxml')    
                    css = soup.find_all('link' )
                    js = soup.find_all('script')
                    for i in css:
                        if i['href'] != '':
                            style = i['href']
                            if style not in css_file:
                                css_file.append(style)
                    for i in js:
                        if i['src'] != '':
                            script = i['src'] 
                            if script not in js_file:
                                js_file.append(script)   
            except Exception as e: 
                print(site[0],':', e)                             
# def writter():

        # magento = False
        # foreach css_files en js_files
        # for file in css_files
        #   if file.find('skin/frontend/') != -1:
        #       magento = True
        #       break
        # doe hetzelfde voor js files
        # if magento:
        #    output.writerow([site])
            print(f"scraping: {site[0]}")
            magento = False
            css = 'skin/frontend/'
            js = 'media/js'
            for file in css_file:
                if css in (file) != -1:
                    magento = True
                    break
        
         

            for file in js_file:
                if js in (file) != -1:
                    magento = True
                    break

     
            if magento:
                output.writerow([site,magento])
                print(f"writing: {site[0]} to file")
            else:
                output.writerow([site,'is geen magento site'])
    # if('skin/frontend/' in css) or ( 'media/js' in js):
    #     output.writerow([site, "True"])
    #     print('text ')
    # else:

    #     output.writerow([site, "False"]) 
    #     print('test ')
    #     time.sleep(0.05)    
pass
print(f"completed scraping")


