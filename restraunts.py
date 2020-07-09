# Visit pyGuru on youTube

import requests
from bs4 import BeautifulSoup
import pandas as pd

# https://www.whoishostingthis.com/tools/user-agent/

city = input('Enter your city : ')
url = 'https://www.zomato.com/'+city+'/top-restaurants'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}

response = requests.get(url,headers=header)
html = response.text
soup = BeautifulSoup(html,'html.parser')

top_rest = soup.find('div',class_="bb0 collections-grid col-l-16")
list_tr = top_rest.find_all('div',class_="col-s-8 col-l-1by3")

restraunts = []
address = []
cuisine = []
ratings = []

for tr in list_tr:
    name = tr.find("div",class_="res_title zblack bold nowrap").text.replace('\n', ' ')
    rates = tr.find("div",class_="ads-res-snippet-rating-large").text.replace('\n', ' ')
    add =  tr.find("div",class_="nowrap grey-text fontsize5 ttupper").text.replace('\n', ' ')
    food = tr.find("div",class_="nowrap grey-text").text.replace('\n', ' ')

    restraunts.append(name.strip())
    ratings.append(rates.strip())
    address.append(add.strip())
    cuisine.append(food.strip())

header = ['Restraunt','Ratings','Address','Cuisine']
indices = [i for i in range(1,len(restraunts)+1)]
all_rests = zip(restraunts,ratings,address,cuisine)
dt = pd.DataFrame(list(all_rests),index=indices,columns=header)
dt.to_csv('Top restraunts in '+city+'.csv')
print(dt)