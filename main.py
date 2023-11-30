import requests
from bs4 import BeautifulSoup


def sort_by_votes(hnlist):
    sorted_list = sorted(hnlist, key= lambda k: k['votes'], reverse=True)
    return sorted_list[:-5]


def create_custom_hn(pages):
    hn = []
    for page in range(pages + 1):
        tmp = '' if pages == 1 else f'?p={page}'
        res = requests.get(f'https://news.ycombinator.com/news{tmp}')
        soup = BeautifulSoup(res.text, 'html.parser')
        links = soup.select('.titleline > a')
        subtext = soup.select('.subtext')
        for index, item in enumerate(links):
            title = links[index].getText()
            href = links[index].get('href', None)
            vote = subtext[index].select('.score')
            if len(vote):
                points = int(vote[0].getText().replace(' points', ''))
                if points > 99:
                    hn.append({'title': title, 'link': href, 'votes': points})
    return hn


lista = create_custom_hn(2)
print(sort_by_votes(lista))
# print(sort_by_votes(lista))
# print(links)
