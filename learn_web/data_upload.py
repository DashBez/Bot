import requests
from bs4 import BeautifulSoup 


def get_html(url):
    try:
        result = requests.get(url,
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"})
        result.raise_for_status()
        return result.text
    except(requests.RequestException,ValueError):
        print("Сетевая ошибка")
        return False

def get_href_goods(url,name_block,key_dict,value_dict):
    html = get_html(url)
    if html:
        soup=BeautifulSoup(html,'html.parser') 
        news_list = soup(name_block, { key_dict: value_dict})
        post =[]
        for news in news_list:
            post.append(str(news)) 
        result_href = []
        for i in range(0,len(post)): 
            result_href.append({
                'href': post[i][post[i].find('href')+6:post[i].find('html')+4]
                })
        
    return result_href

def get_info_goods(url,name_block,key_dict,value_dict):
    html = get_html(url)
    result_info = []
    if html:
        soup=BeautifulSoup(html,'html.parser')
        news_list = soup(name_block, { key_dict: value_dict})
        for news in news_list:
            part_of_Marka_tmp = news.find_all('div', class_='col-7 col-sm-12 d-flex align-items-stretch gap')
            part_of_Size_tmp = news.find('p',class_= 'col-7 col-sm-12')
            part_of_Condition_tmp = news.find_all('div',class_='col-7 col-sm-12')

            for test_i in part_of_Marka_tmp:
                part_of_Marka = test_i.find('a').text
                result_info.append ({
                   # 'html':news,
                    'Marka': str(part_of_Marka).replace('\n','').replace(' ','')
                })

            for test_i in part_of_Size_tmp:
                part_of_Size = test_i
                result_info.append ({
                    'Size': str(part_of_Size).replace('\n','').replace(' ','')
                })     

            for test_i in part_of_Condition_tmp:
                part_of_Condition = test_i.find('p').text
                result_info.append ({
                    'Condition': str(part_of_Condition).replace('\n','').replace(' ','')
                })                
        

    return result_info

if __name__ == "__main__":    
    post = []
    Goods_info = get_href_goods("https://www.maedchenflohmarkt.de/alle-ansehen.html",'a','class','product-image orientation-portrait')
    for Goods in Goods_info:
        href_info = get_info_goods("https://www.maedchenflohmarkt.de"+Goods['href'],'div','class','product__attributes card card-body gap')
        for info in href_info:
            with open("href_info.txt",'a',encoding='utf8') as f:
                f.write(str(info))



    

        