import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint as pp
url = requests.get("https://news.ycombinator.com/")
url2 = requests.get("https://news.ycombinator.com/?p=2")

soup = bs(url.text, 'html.parser')
soup2 = bs(url2.text, 'html.parser')
# print(soup.body)
# print(soup.contents)
# print(soup.find_all('div'))
# print(soup.find_all('a'))
# print(soup.find('a'))
links = soup.select('.titleline')
subtext = soup.select('.subtext')
links2 = soup2.select('.titleline')
subtext2 = soup2.select('.subtext')

all_links = links + links2
all_subtext = subtext + subtext2
# print(subtext[0])
def stories_sorted_by_votes(the_news):
    return sorted(the_news, key= lambda k:k['votes'], reverse=True) 



def links_score_data(links, subtext):
    news = []
    for i, item in enumerate(links):
        title = links[i].getText()
        url = links[i].find('a').get("href")
        vote = subtext[i].select('.score')
        if len(vote):
            votes = int(vote[0].getText().replace(' points', ''))
            if votes > 100:
                news.append({'title':title, 'url':url, 'votes':votes})
    return stories_sorted_by_votes(news)
# pp(links_score_data(links, subtext))
pp(links_score_data(all_links, all_subtext))