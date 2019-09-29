import time
import re
import json
import pandas as pd, numpy as np
import os
import requests
import ssl
from pandas.io.json import json_normalize
from urllib.request import urlopen
from selenium import webdriver
from sys import path
from bs4 import BeautifulSoup as bs

def install():
    # Adds the extensions commands to the command file
    import consts
    print("Installing InstaEXT")
    print(consts.COMMANDS_FILE)
    commandsFile = open(consts.COMMANDS_FILE, "a")
    commandsFile.write("insta,InstaEXT\n")
    commandsFile.close()
    return 

def init():
    # A very useful function that does a lot of things!
    return


def OLGAWebScrapeExt(category, search):
    directory = input("Enter full drive-location for photo results: ")
    if(category=="u"|category=="U"):
        username = search
        browser = webdriver.Chrome('chromedriver')## Move this on commit
        browser.get('https://www.instagram.com/'+username+'/?hl=en')
        Pagelength = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    elif(category=="h"|category=="H"):
        hashtag = search
        browser = webdriver.Chrome('chromedriver')
        browser.get('https://www.instagram.com/explore/tags/'+hashtag)
        Pagelength = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    links=[]
    source = browser.page_source
    data=bs(source, 'html.parser')
    body = data.find('body')
    script = body.find('span')
    for link in script.findAll('a'):
        if re.match("/p", link.get('href')):
            links.append('https://www.instagram.com'+link.get('href'))
    Pagelength = browser.execute_script("window.scrollTo(0, document.body.scrollHeight/1.5);")
    source = browser.page_source
    data=bs(source, 'html.parser')
    body = data.find('body')
    script = body.find('span')
    for link in script.findAll('a'):
        #print(link)
        if re.match("/p", link.get('href')):
            links.append('https://www.instagram.com'+link.get('href'))#sleep time is required. If you don't use this Instagram may interrupt the script and doesn't scroll through pages
    time.sleep(5) 
    Pagelength = browser.execute_script("window.scrollTo(document.body.scrollHeight/1.5, document.body.scrollHeight/3.0);")
    source = browser.page_source
    data=bs(source, 'html.parser')
    body = data.find('body')
    script = body.find('span')
    for link in script.findAll('a'):
        if re.match("/p", link.get('href')):
            links.append('https://www.instagram.com'+link.get('href'))
    time.sleep(10) 
    result=pd.DataFrame()
    for i in range(len(links)):
        try:
            context = ssl._create_unverified_context()#Mask SSL CERT ERROR
            page = urlopen(links[i], context=context).read()#Include custom context
            data=bs(page, 'html.parser')
            body = data.find('body')
            script = body.find('script')
            raw = script.text.strip().replace('window._sharedData =', '').replace(';', '')
            json_data=json.loads(raw)
            posts =json_data['entry_data']['PostPage'][0]['graphql']
            posts= json.dumps(posts)
            posts = json.loads(posts)
            x = pd.DataFrame.from_dict(json_normalize(posts), orient='columns') 
            x.columns =  x.columns.str.replace("shortcode_media.", "")
            result=result.append(x)
            print("Found img " + str(i))
        except:
            np.nan
    result = result.drop_duplicates(subset = 'shortcode')
    result.index = range(len(result.index))
    print(result)
    result.index = range(len(result.index))
    #directory="/Users/admin/Desktop/OLGAScrape/"
    for i in range(len(result)):
        r = requests.get(result['display_url'][i])
        with open(directory+result['shortcode'][i]+".jpg", 'wb') as f:
            f.write(r.content)


def listen(command):
    # Takes and processes command from OLGA
    
    # Adds olga's directory to be accessible
    import os
    olgaDir = os.getcwd().replace("Extensions"+os.sep, "")
    path.append(olgaDir)
    from olga import makeOOO

    # Package output into an Olga Output Object
    output = None
    if(command=="insta"):
        search = ""
        category = input("Choose Hashtag (H) or Username (U): ")
        if(category=="h"|category=="H"):
            search = input("Enter a hashtag: #")
            OLGAWebScrapeExt(category, search)
        elif(category=="u"|category=="U"):
            search = input("Enter a username: www.instagram.com/")
            OLGAWebScrapeExt(category, search)
        output = makeOOO(text="Success")
    return output
