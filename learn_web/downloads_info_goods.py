import requests
from bs4 import BeautifulSoup 
import re

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
        result_info_1 = []
        for i in range(0,len(post)): 
            result_info_1.append({
                'href': post[i][post[i].find('href')+6:post[i].find('html')+4]
                })
        
    return result_info_1

def get_info_goods(url,name_block,key_dict,value_dict):
    html = get_html(url)
    if html:
        soup=BeautifulSoup(html,'html.parser')
        news_list = soup(name_block, { key_dict: value_dict})

        post =[]
    for news in news_list:
        post.append(news)
        
    return post


if __name__ == "__main__":
    Goods_info = get_href_goods("https://www.maedchenflohmarkt.de/alle-ansehen.html",'a','class','product-image orientation-portrait')
    for Goods in Goods_info:
        href_info = get_info_goods("https://www.maedchenflohmarkt.de"+Goods['href'],'div','class','product__attributes card card-body gap')
        with open("href_info.txt",'a',encoding='utf8') as f:
            f.write(str(href_info))
        #tmp = Goods['href']

       

""" 


    for i in range(0,len(post)): 
        if post[i].find('Marke')>0:

            tmp_Marka = post[i][post[i].find('/brand/')+7:post[i].find('.html')]
            #elif post[i].find('Marke') != -1:
            #    tmp_Marka = [post[i],post[i].find('Marke')]
        else:

            tmp_Marka = post[i].find('Marke')

        result_info.append({
                'inside':post[i],
                'URL':url,
                'Marka':tmp_Marka,
                'Size':post[i][post[i].find('Größe')+62:post[i].find('Größe')+64],
                'Condition':post[i][post[i].find('itemCondition')+45:post[i].find('itemCondition')+60],
                'Color':re.findall(r'#[0-9A-Fa-f]{6}',str(soup('span',{'class': 'product__color'})))  #[0-9Ff] больше чем нужно не понимаю откуда берутся(
                #'Description':re.findall(r'[^"<li>"]', post[i][post[i].find('description')+41:len(post[i])])
                })
    return result_info



   
    for href in Goods_info:
        INFO = get_info_goods("https://www.maedchenflohmarkt.de"+href['href'],'div','class','product__attributes card card-body gap')
        for href_info in INFO:
            print(href_info)

        

    
        INFO = get_info_goods("https://www.maedchenflohmarkt.de"+tmp,'div','class','product__attributes card card-body gap')
        
    print(INFO[0])

    
    for Goods in Goods_info:
        tmp = Goods['href']
        href = get_info_goods("https://www.maedchenflohmarkt.de"+tmp,'div','class','product__attributes card card-body gap')
    print(href)
        #print(href['name'].replace('\\u00',''))
   
    with open("href_info.txt",'w',encoding='utf8') as f:
        for href in href_info:
            f.write(str(href))

    #html = "https://www.maedchenflohmarkt.de"+href_info['href']
    #print(get_info_goods(html))
    """
