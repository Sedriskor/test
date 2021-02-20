import requests
from bs4 import BeautifulSoup
import time
import sys

today = time.strftime('%m/%d').lstrip('0') #lstrip:字串左邊去掉'__'

ptt_url = 'https://www.ptt.cc'


def choice_web_ptt():
    index = input('請輸入看板名稱(q=離開)： ')
    if index == 'q':
        sys.exit()
    index = '/bbs/' + index + '/index.html'
    return index


def get_web_ptt(index):
    resp = requests.get(ptt_url + index) #擷取網址
    if resp.status_code != 200: #發生錯誤時回傳訊息
        print('URL發生錯誤:' + url)
        return
    else:
        return resp.text


def ptt_article(dom):
    soup = BeautifulSoup(dom, 'html5lib') #分析擷取內容

    prev_url = soup.find('div', 'btn-group btn-group-paging').find_all('a')[1]['href'] #上一頁網址
    #find 'div'中的'btn-group btn-group-paging'的全部超連結(a)資料
    # print(prev_url) #check input

    print('-----------------------------------')#分隔線

    articles = [] #儲存取得文章資料
    rents = soup.find_all('div', 'r-ent')
    for rent in rents: #分析文章組成
        title = rent.find('div', 'title').text.strip()
        # href = rent.find('div', 'title').find('a')['href']#該文章網址
        count = rent.find('div', 'nrec').text.strip()
        data = rent.find('div', 'meta').find('div', 'date').text.strip()
        article = '%s %s: %s' % (data, count, title)

        try: #篩選文章(日期/推文數)
            if today == data and int(count) > 10: #加入推文 > 10的文章
                articles.append(article)
        except:
            if today == data and count == '爆': #加入推文 = 爆的文章
                articles.append(article)

    return articles, prev_url #回傳這網址的標題及上頁網址


def main():
    while True:
        index =choice_web_ptt()
        dom =get_web_ptt(index)
        articles, prev_url = ptt_article(dom)

        while len(articles) != 0:     #當articles) != 0時 執行以下代碼
            for article in articles:
                print(article)

            prev_url_dom = get_web_ptt(prev_url)
            articles, prev_url = ptt_article(prev_url_dom)


if __name__ =='__main__':
    main()