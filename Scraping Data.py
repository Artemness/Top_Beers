import pandas as pd
import numpy as np
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DRIVER_PATH = '/home/artem/PycharmProjects/Top_Beers/chromedriver'
driver = webdriver.Chrome(executable_path = DRIVER_PATH)

names = []
breweries = []
styles = []
abvs = []
ratings = []
avg_ratings = []

driver.get('https://www.beeradvocate.com/beer/top-rated/')
beer_table = driver.find_elements_by_xpath('//*[@id="ba-content"]/table')
print(beer_table)
beer = beer_table[0]
for i in range(1,251):
    try:
        namexpath = '//* /tbody/tr['+str(i+1)+']/td[2]/a/b'
        name = beer.find_element_by_xpath(namexpath).text
    except:
        name = "NaN"
    names.append(name)

    try:
        breweryxpath = '//* /tbody/tr['+str(i+1)+']/td[2]/span/a[1]'
        brewery = beer.find_element_by_xpath(breweryxpath).text
    except:
        brewery = 'NaN'
    breweries.append(brewery)

    try:
        stylesxpath = '//* /tbody/tr['+str(i+1)+']/td[2]/span/a[2]'
        style = beer.find_element_by_xpath(stylesxpath).text
    except:
        style = 'NaN'
    styles.append(style)

    try:
        abvsxpath = '//* /tbody/tr['+str(i+1)+']/td[2]/span'
        abv = beer.find_element_by_xpath(abvsxpath).text
        abv = abv.split('|')[1][1:]
        abv = abv.replace('%', '')
    except:
        abv = 'NaN'
    abvs.append(abv)

    try:
        ratingsxpath = '//* /tbody/tr['+str(i+1)+']/td[3]/b'
        rating = beer.find_element_by_xpath(ratingsxpath).text
        rating.replace(',', '')
    except:
        rating = 'NaN'
    ratings.append(rating)

    try:
        avgratingsxpath = '//* /tbody/tr['+str(i+1)+']/td[4]/b'
        avg_rating = beer.find_element_by_xpath(avgratingsxpath).text
    except:
        avg_rating = 'NaN'
    avg_ratings.append(avg_rating)

df = pd.DataFrame()
df['Beer'] = names
df['Brewery'] = breweries
df['Style'] = styles
df['ABV'] = abvs
df['Num_of_Ratings'] = ratings
df['Average Rating'] = avg_ratings

df.to_csv('Top250Beers.csv', index=False)