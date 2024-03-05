
###Install 
sudo apt install python3-django

###Run 
python manage.py runserver

###check on website
127.0.0.1:8000

若有執行問題 
sudo chmod 777 manage.py

如果要其他客戶端連線使用
python manage.py runserver 0.0.0.0:8000

另外需要修改iotproject/settings.py
加入樹梅派的IP
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '192.168.0.105', '192.168.58.57']

