#importing dependecies 
import schedule
from bs4 import BeautifulSoup
import requests 
import time
import pandas as pd



job_listings = []

def scrape_jumia():
    #Pagination for loop
    for x in range(1, 3):
            
        #Reading website url
        url = 'https://www.jumia.com.ng/mlp-oraimo-store/?page='
        r=requests.get(url+str(x))
        soup = BeautifulSoup(r.content, 'html.parser')
        products = soup.find_all('div', class_ ='info')


        for product in products: 
            product_name = product.find('h3', class_ = 'name').text
            discounted_price = product.find('div', class_ = 'prc').text
            old_price = product.find('div', class_ = 'old').text
            discount = product.find('div', class_ = 'bdg _dsct _sm').text
        
            #Dictionary to append fetched data
            job_info = {
                'product_name': product_name,
                'old_price':old_price,
                'discounted_price': discounted_price,
                'discount' : discount
            }

            job_listings.append(job_info)
        print(len(job_listings)) 
        time.sleep(3)

    df = pd.DataFrame(job_listings)
    print(df.head())

    df.to_csv('jumia_oraimo_dataset_new.csv')

def job():
    print('scrapping jumia')
    scrape_jumia()

schedule.every(24).hours.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

