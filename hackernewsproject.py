import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
texts = res.text

soup = BeautifulSoup(res.text, 'html.parser')

links = soup.select('.storylink')
subtext = soup.select('.subtext')
# print(votes)
# print(links[1].getText())

def sort_stories_by_votes(hnlist):
    return(sorted(hnlist, key= lambda k: k['point'], reverse=True))

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            point = int(vote[0].getText().replace(' points', ''))
            if point >= 100:
                hn.append({'title': title, 'link': href, 'point': point})

    return sort_stories_by_votes(hn)


answer = create_custom_hn(links, subtext)
pprint.pprint(answer[0:20])