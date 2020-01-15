from webapp_fashion import create_app
from webapp_fashion.data_upload  import get_info_goods

app = create_app()
with app.app_context():
    get_info_goods() 
