import requests
from bs4 import BeautifulSoup 
from time import sleep
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
        result_href = []
        for i in range(0,len(post)): 
            result_href.append({
                'href': post[i][post[i].find('href')+6:post[i].find('html')+4]
                })
        
    return result_href

def get_info_goods(url,name_block,key_dict,value_dict):
    time_to_sleep_when_captcha = 5
    html = get_html(url)
    result_info = []
    

    if html:
        soup=BeautifulSoup(html,'html.parser')

        try:
            part_of_Marka_tmp = soup.find(name_block, { key_dict: value_dict}).find('div', class_='col-7 col-sm-12 d-flex align-items-stretch gap').find('a').text
            part_of_Size_tmp =  soup.find(name_block, { key_dict: value_dict}).find('p',class_= 'col-7 col-sm-12').text
            part_of_Condition_tmp = soup.find(name_block, { key_dict: value_dict}).find('div',class_='col-7 col-sm-12').find('p').text
            part_of_Description_tmp = soup.find(name_block, { key_dict: value_dict}).find("ul", {"id":"product-description"})
            part_of_price_tmp = soup.find(name_block, { key_dict: value_dict}).find('div',class_='d-flex flex-column align-self-center text-center product-detail__price mr-sm-3').text
            part_of_seller_tmp = soup.find(name_block, { key_dict: value_dict}).find('div',class_= 'product__seller card card-body mb-3')
            part_of_image_tmp = soup.find(name_block, { key_dict: value_dict}).find('div',class_= 'card d-none d-lg-block gap')

            result_info.append ({
                'Marka': " ".join(part_of_Marka_tmp.split()),
                'Size': " ".join(part_of_Size_tmp.split()),
                'Condition': " ".join(part_of_Condition_tmp.split()),
                'Description': part_of_Description_tmp,
                'Price': " ".join(part_of_price_tmp.split()),
                'Seller': part_of_seller_tmp,
                'Image': part_of_image_tmp
                #'whole part': soup.find(name_block, { key_dict: value_dict})
 
                })
        except:
                sleep(time_to_sleep_when_captcha)
                time_to_sleep_when_captcha += 1



    
    return result_info

if __name__ == "__main__":    
    post = []
    Goods_info = get_href_goods("https://www.maedchenflohmarkt.de/alle-ansehen.html",'a','class','product-image orientation-portrait')
    for Goods in Goods_info:
        #href_info = get_info_goods("https://www.maedchenflohmarkt.de"+Goods['href'],'div','class','product__attributes card card-body gap')
        href_info = get_info_goods("https://www.maedchenflohmarkt.de"+Goods['href'],'div','id','product-detail')
        for info in href_info:
            with open("href_info.txt",'w',encoding='utf8') as f:
                f.write(str(info))



    

        