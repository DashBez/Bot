import requests
from bs4 import BeautifulSoup 

result = requests.get("https://www.maedchenflohmarkt.de/anna-field-traegerkleid-schwarz-elegant/4676960.html",
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"})
soup=BeautifulSoup(result.text,'html.parser') 
news_list = soup('div', {'class' : 'product__attributes card card-body gap'})
# 
post =[]
for news in news_list:
    post.append(str(news))
"""
result_info = []
for i in range(0,len(post)): 
    result_info.append({
        'id': post[i][post[i].find('"id"')+5:post[i].find('"name"')-1],
        'name': post[i][post[i].find('"name"')+8:post[i].find('"category"')-2],
        'category': post[i][post[i].find('"category"')+12:post[i].find('"price"')-2],
        'price': post[i][post[i].find('"price"')+8:post[i].find('"quantity"')-1],
        'quantity': post[i][post[i].find('"quantity"')+11:post[i].find('"brand"')-1],
        'brand': post[i][post[i].find('"brand"')+9:post[i].find('"position"')-2],
        'href': post[i][post[i].find('href')+6:post[i].find('html')+4]
        })
"""
print(post[0])
#выгрузка данных о товарах со страницы со списком товаров
"""
base_post = []
for i in range(0,len(post)):
    var_test = str(post[i])
    tmp_1 = var_test.find('data-ga-product')
    tmp_2 = var_test.find('data-ga-track-click')
    base_post.append(var_test[tmp_1:tmp_2])

for j in range(0,len(base_post)):
    print(base_post[j])

#выгрузка данных о товарe со страницы конкретного товара

base_post = []
for i in range(0,len(post)):
    var_test = str(post[i])
    tmp_1 = var_test.find('href')
    tmp_2 = var_test.find('img alt')
    base_post.append(var_test[tmp_1:tmp_2])

#for j in range(0,len(base_post)):
tmp_repl = base_post[0].replace('"','')
tmp_repl_1 = tmp_repl.replace('><','')
last_repl = tmp_repl_1.replace('href=','')

result_1=requests.get("https://www.maedchenflohmarkt.de"+last_repl,
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"})
soup=BeautifulSoup(result.text,'html.parser') 
post_1 =[]
print(soup)



                    'Size': str(soup('p',{'class': 'col-7 col-sm-12'}))
                            [str(soup('p',{'class': 'col-7 col-sm-12'})).find('col-7 col-sm-12')+42:
                            str(soup('p',{'class': 'col-7 col-sm-12'})).find('col-7 col-sm-12')+44],
                    #'Condition': post[i][post[i].find('itemCondition'):post[i].find(' <i class="mico-question2">')-1]
                    'Color':str(soup('span',{'class': 'product__color'}))
                            [str(soup('span',{'class': 'product__color'})).find('style="background-color')+25:
                             str(soup('span',{'class': 'product__color'})).find('style="background-color')+32
                             ]
"""