import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome( executable_path=r"C:\Users\user\Dropbox\PC\Desktop\chromedriver.exe",options=options)
driver.get('https://www.amazon.in/Samsung-Galaxy-Storage-6000mAh-Battery/product-reviews/B0B4F2XCK3/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews')

l1 = list()
l2 = list()

x=1
while x==1:
    
        
    try:
        review_title = driver.find_elements_by_xpath('//a[@data-hook="review-title"]') 
        for i  in review_title:
            tit = i.text
            l1.append(tit)
        
        review = driver.find_elements_by_xpath('//span[@data-hook="review-body"]')
        for i  in review:
            rev = i.text
            l2.append(rev)
        
        
        time.sleep(1)
        button = driver.find_element_by_partial_link_text('Next page')
        button.click()
        time.sleep(1)
        
        
    except:
        x=-1

df1 = pd.DataFrame(l1,columns=['Review_Title'])
df2 = pd.DataFrame(l2,columns=['Review'])

df = pd.concat([df1, df2],axis = 1)
df.to_csv(r"C:\Users\user\Dropbox\PC\Desktop\Samsung Galaxy Review\Review.csv")

driver.close()

