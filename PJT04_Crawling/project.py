import requests
from bs4 import BeautifulSoup
import pandas as pd


def getNewsInfo():
    newsTitle = soup.find_all('a', {'class':'news_tit'})
    titleList = []
    for title in newsTitle:
        titleList.append(title.text)

    newsLink = soup.find_all('a', {'class':'info'})
    linkList = []
    for link in newsLink:
        linkList.append(link['href'])
    linkList = linkList[1::2]

    return titleList, linkList


def clickNews():
    a, b = getNewsInfo()
    print(a)
    print(b)
    all_contentList = []
    idx = 0
    for i in b:
        html = requests.get(i)
        soup = BeautifulSoup(html.text, 'html.parser')
        newsContents = soup.find('article', {'id':'dic_area'})

        all_contentList.append([a[idx],b[idx], newsContents.text.strip()])
        idx += 1

    print(len(all_contentList))
    return all_contentList


allPages = []
for n in range(1, 71, 10):
    print('------------------------------------')
    url = f'https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EB%84%B7%ED%94%8C%EB%A6%AD%EC%8A%A4%20%EC%B6%94%EC%B2%9C%20%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98&sort=0&photo=3&field=0&pd=0&ds=&de=&cluster_rank=10&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start={n}'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    news = clickNews()
    allPages.extend(news)

    print(news)

print('END')

#[['title', 'url', 'content'], ['title', 'url', 'content'], ['title', 'url', 'content'], ['title', 'url', 'content']]

df = pd.DataFrame(allPages,columns = ['타이틀', 'URL', '기사내용'])
df = df.applymap(lambda x:x.replace('\n', '').replace('\t', '').replace('  ', ''))
print(df)
df.to_csv('test.csv',encoding = 'UTF-8')














