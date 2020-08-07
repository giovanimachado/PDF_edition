# import libraries
from selenium import webdriver
import pyautogui
from time import sleep
from bs4 import BeautifulSoup
import urllib.request
import time
import numpy as np
import pandas as pd

# To prevent download dialog
# profile = webdriver.FirefoxProfile()
# profile.set_preference('browser.download.folderList', 1) # custom location
# profile.set_preference('browser.download.manager.showWhenStarting', False)
# profile.set_preference('browser.download.dir', '/tmp')
# profile.set_preference('browser.helperApps.neverAsk.saveToDisk', "application/pdf")

# specify the url
#urlpage = 'https://groceries.asda.com/search/yogurt' 
urlpage = "https://petrobras.myhbp.org/hmm12/content/delegating/resources.html"
print(urlpage)

# run firefox webdriver from executable path of your choice
# driver = webdriver.Firefox(profile)
driver = webdriver.Firefox()

# get web page
driver.get(urlpage)
# execute script to scroll down the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
# sleep for 30s
time.sleep(30)
# driver.quit()

results = driver.find_elements_by_tag_name('a')
print('Number of results', len(results))
#print(results)

# create empty array to store data
data = set()
# loop over results
for result in results:
    #print(result)
    #product_name = result.text
    #link = result.find_element_by_tag_name('a')
    #product_link = link.get_attribute("href")
    link = result.get_attribute("href")
    # append dict to array
    #data.append({"link" : link})
    data.add(link)
    
print(data)

# save to pandas dataframe
df = pd.DataFrame(data)
print(df)

# write to csv
df.to_csv('HMMLink.csv')

filetypes=[".pdf",".docx"] #you will need to do some kind of pattern matching on your files

myfiles=[]

for link in data: #you can also iterate through br.forms() to print forms on the page!
    for t in filetypes:
        if t in str(link): #check if this link has the file extension we want (you may choose to use reg expressions or something)
            myfiles.append(link)
                        
print("Printing files found: ", myfiles)
print()


# def downloadlink(l):
#     f=open(l.text,"wb") #perhaps you should open in a better way & ensure that file doesn't already exist.
#     r = br.click_link(l)
#     response = br.open(r)
#     #f.write(br.response().read())
#     #print("response: ", response.read())
#     f.write(response.read())
#     print (l.text," has been downloaded")
#     #br.back()

for l in myfiles:
    sleep(5) #throttle so you dont hammer the site
    # downloadlink(l)
    if "pdf" in str(l):
        driver.get(l)
        sleep(2)
        # pyautogui.press('down')
        pyautogui.hotkey('ctrl', 's')
        sleep(.5)
        pyautogui.press('enter')
    else:
        driver.get(l)
        sleep(2)
        pyautogui.press('down')
        sleep(.5)
        pyautogui.press('enter')
        sleep(1)
        pyautogui.press('enter')
  
# close driver 
driver.quit()
