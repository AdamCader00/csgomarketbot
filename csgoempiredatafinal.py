# import libraries
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
import re

page_number = 1
data = []
prices = []
percent_off = []

# specify the url
urlpage = 'https://csgoempire.com/withdraw#730' 
print(urlpage)
# run firefox webdriver from executable path of your choice
driver = webdriver.Chrome(executable_path = '/Users/adamcader/Downloads/chromedriver')

# get web page
driver.get(urlpage)
submit_button = driver.find_element_by_xpath("//button[@class='button-secondary button-secondary--dark w-full']")
submit_button.click()
#execute script to scroll down the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")

time.sleep(15)
#driver.quit()


# find elements by xpath

while page_number < 15:
    time.sleep(5)
    results = driver.find_elements_by_xpath("//*[@class='item item--trading item--sapphire item--instant-withdraw item--730' or @class=@class='item item--trading item--instant-withdraw item--730' or @class='item item--trading item--emerald item--instant-withdraw item--730']/div[@class='item__inner']")
    #prices
    results3 = driver.find_elements_by_xpath("//div[@class='px-1 pb-1']/div[@class='flex flex-wrap items-center justify-between -ml-1 -mb-1']/div[@class='flex-1 ml-1 pb-1']")
    #percent_off
    results2 = driver.find_elements_by_xpath("//div[@class='flex flex-wrap items-center justify-between -ml-1 -mb-1']/div[@class='item__price inline-flex items-center flex-no-shrink ml-1']")

    for result2 in results2:
        product_name2 = result2.text
        prices.append(product_name2)

    for result3 in results3:
        product_name3 = result3.text
        percent_off.append(product_name3)    
        
  
    # loop over results

    for result in results:
        product_name = result.text
        # append dict to array
        data.append(product_name)
    if page_number < 4:
        submit_button = driver.find_element_by_xpath("//div[@class='relative w-full']/ul[@class='pagination mb-4 md:mb-6']/li[9]/a")

    if page_number >= 4:
        submit_button = driver.find_element_by_xpath("//div[@class='relative w-full']/ul[@class='pagination mb-4 md:mb-6']/li[10]/a")
   
    submit_button.click()

    #results = driver.find_elements_by_xpath("//div[@class='item item--trading item--instant-withdraw item--730']/div[@class='item__inner']")
    page_number = page_number + 1
    results = ''
    results2 = ''
    results3 = ''


# close driver 
driver.quit()
# save to pandas dataframe
df = pd.DataFrame(data)


print(len(prices), len(percent_off), len(data))

for i in range(len(prices)):
   #print(prices[i], " ", percent_off[i])
 
   one = re.sub('[^A-Za-z0-9]+', '', percent_off[i])
   one = int(one)
   if one <= 4:
       print("item found", " ", data[i])
  
    

# write to csv
df.to_csv('csgoempireproductsnew.csv')

