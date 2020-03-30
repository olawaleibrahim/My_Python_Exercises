import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
texts = res.text
soup = BeautifulSoup(res.text, 'html.parser')
#print(str(soup.body.contents))
#print(soup.find_all('a'))
#print(soup.find(id='22673933'))

#print(soup.select('#score_22673933'))

links = soup.select('.storylink')
votes = soup.select('score')

print(links[4])


#with open('web_document_soup.txt', mode='w') as doc:
    #doc.write(str(soup))