from cmath import nan
import time
from numpy import NaN
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


list =['yeezy-foam-runner-onyx-18549939',
        'air-max-1-travis-scott-baroque-brown-17616711',
        'yeezy-boost-350-v2-bone-18025402?size=36']

url=f'https://www.stadiumgoods.com/en-in/shopping/'
url2='https://stockx.com/adidas-yeezy-500-soft-vision'
url3='https://stockx.com/nike-dunk-low-varsity-green'
mydata= pd.read_csv('products.csv',delimiter='\t')

#print(mydata)

options = Options()
options.headless = False
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--window-size=1920,1200")
options.add_argument('user-agent= Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36')

driver=uc.Chrome(use_subprocess=True)
scraped_data= {
    'SKU': [],
    'gender': [],
    'nick_name': [],
    'color': [],
    'stgoods_price': [],
}


for index,shoe in mydata.iterrows():
    #scraping stadium goods
    if shoe['Stadiumgoods'] is not NaN:
        driver.get(shoe['Stadiumgoods'])
        try:
            #find the elements with data and insert data in DF
            SKU = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div/main/div[2]/div/div/div/div[1]/div[2]"))
            )
            gender= driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/main/div[2]/div/div/div/div[2]/div[2]') 
            nick_name = driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div/main/div[2]/div/div/div/div[3]/div[2]')
            colorway = driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div/main/div[2]/div/div/div/div[4]')
            min_price = driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div/main/div[1]/div/section/div[2]/span[1]') 
            scraped_data['SKU'].append(SKU.text) 
            scraped_data['gender'].append(gender.text)
            scraped_data['color'].append(colorway.text)
            scraped_data['nick_name'].append(nick_name.text)
            scraped_data['stgoods_price'].append(min_price.text)                     
        except:
            print('error')
        time.sleep(2)
    else:
        scraped_data['SKU'].append('Not Availabe') 
        scraped_data['gender'].append('Not Availabe')
        scraped_data['color'].append('Not Availabe')
        scraped_data['nick_name'].append('Not Availabe')
        scraped_data['stgoods_price'].append('Not Availabe')
    
    #Scrappinf StockX:
    if shoe['Stock'] is not NaN:
        driver.get(shoe['StockX'])
        SKU = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div/main/div[2]/div/div/div/div[1]/div[2]"))
            )
    


print(scraped_data)

#scraping Stoxkx
#driver.get(url2)
#driver.get(url3)



time.sleep(1000)
