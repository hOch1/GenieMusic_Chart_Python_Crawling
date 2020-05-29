import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
url = 'https://www.genie.co.kr/chart/top200'
resp = requests.get(url, headers = headers)
soup = BeautifulSoup(resp.text, 'html.parser')


songs = soup.findAll('a',{'class' : 'title ellipsis'})
peoples = soup.findAll('a',{'class':'artist ellipsis'})

for song, people, i in zip(songs, peoples, range(0,50)):
	title = song.text
	name = people.text
	print(str(i+1)+"위 "+title.strip()+" : "+name.strip())

