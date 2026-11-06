import requests
from bs4 import BeautifulSoup
url = "https://movie.douban.com/top250"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://movie.douban.com/",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
}
response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.text,'lxml')
movie_items = soup.find_all('div',class_='item')
print(f"一共找到了{len(movie_items)}部电影")
first_movie = movie_items[0]
title = first_movie.find('span',class_='title').text
rating = first_movie.find('span',class_ = 'rating_num').text
print(f"第一部电影：{title},评分：{rating}")