# import libraries
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd


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

results = driver.find_elements_by_xpath("//div[@class='item item--trading item--instant-withdraw item--730']/div[@class='item__inner']")

# create empty array to store data
data = []
# loop over results
for result in results:
    product_name = result.text
    # append dict to array
    data.append({"product" : product_name})

submit_button = driver.find_element_by_xpath("//div[@class='relative w-full']/ul[@class='pagination mb-4 md:mb-6']/li[4]/a")
submit_button.click()

results = driver.find_elements_by_xpath("//div[@class='item item--trading item--instant-withdraw item--730']/div[@class='item__inner']")

for result in results:
    product_name = result.text
    # append dict to array
    data.append({"product" : product_name})


# close driver 
driver.quit()
# save to pandas dataframe
df = pd.DataFrame(data)

for k in data:
   print (k)

# write to csv
df.to_csv('csgoempireproductsnew.csv')

