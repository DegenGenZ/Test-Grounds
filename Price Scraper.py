from bs4 import BeautifulSoup
import requests
import urllib.request
import wget

page_to_scrape = (requests.get('https://www.flipkart.com/search?q=oppo&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'))
soup = BeautifulSoup(page_to_scrape.text, 'lxml')
# price_window = soup.find("div", class_="_3pLy-c row")
titles = soup.find_all(class_="_4rR01T")
prices = soup.find_all(class_="_30jeq3 _1_WHN1")
reviews = soup.find_all(class_="_2_R_DZ")
ratings = soup.find_all(class_="_3LWZlK")
# for rating in ratings:
#     print(rating.text)
# for title in titles:
#     print(title.text)
# for price in prices:
#     print(price.text)
for title, price, review, rating in zip(titles, prices, reviews, ratings):
    print(f'The phone : {title.text} costs: {price.text} and has: {review.text} with an overall rating of {rating.text} out of 5.')

# url = "https://apssb.nic.in/Index/notice"
# req = requests.get(url)
# soup = BeautifulSoup(req.text, 'lxml')
# mtlist = []
# for link in soup.find_all('a', target="_blank"):
#     tags = link.get('href')
#     mtlist.append(tags)
# for i in mtlist[:2]:
#     wget.download(i)




