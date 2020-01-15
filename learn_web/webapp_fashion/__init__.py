from flask import Flask,render_template
#from webapp_fashion.data_upload  import get_info_goods
from webapp_fashion.model import db,News



def create_app():

    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    


    def index():
        title = 'Info Goods' 
        news_list = News.query.all()
        #get_info_goods()               
        return render_template('index.html',page_title=title,news_list=news_list)
    return  app