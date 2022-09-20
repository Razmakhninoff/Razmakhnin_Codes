import requests
from bs4 import BeautifulSoup
import re
import string
import os

print('  --  --- Razmakhnin codes ---  --\n github.com/Razmakhninoff/Razmakhnin_Codes\n')

punc = [p for p in string.punctuation]
end_save = []
links = []          # links on articles

x = int(input())
y = string.capwords(input(), sep=None)

for k in range(1, x+1):
    folder_f = os.mkdir(f'Page_{str(k)}')

for j in range(1, x+1):
    url = f'https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&year=2020&page={j}'
    page_content = requests.get(url, headers={"Accept-Language": 'en-US,en;q=0.5'}).content
    soup = BeautifulSoup(page_content, "html.parser")

    news_links = soup.find_all('span', {'class': 'c-meta__type'}, text=y)
    for i in news_links:
        links.append('https://www.nature.com' + i.find_parent('article').find('a', attrs={
            'href': re.compile("articles")}).get('href'))

    for link in links:
        page_content_2 = requests.get(link, headers={"Accept-Language": 'en-US,en;q=0.5'}).content
        soup_2 = BeautifulSoup(page_content_2, 'html.parser')

        article_title = soup_2.find('h1', class_="c-article-magazine-title").text.strip()

        titles = [p for p in article_title if p not in punc]
        article_file = (''.join(titles)).replace(' ', '_') + '.txt'
        end_save.append(article_file)

        body_text = soup_2.find('div', class_='c-article-body').text

        article_f = open(f'Page_{j}/{article_file}', 'w', encoding="UTF-8")
        article_f.write(body_text)
        article_f.close()

print('Saved all articles.')  # final