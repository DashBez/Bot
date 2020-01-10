import requests

def get_html(url):
    try:
        result = requests.get(url,
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"})
        result.raise_for_status()
        return result.text
    except(ValueError):
        print("Сетевая ошибка")
        return False



if __name__ == '__main__':
    html = get_html("https://www.maedchenflohmarkt.de/alle-ansehen.html")
    if html:
        with open("html_german.html",'w',encoding='utf8') as f:
            f.write(html)



            