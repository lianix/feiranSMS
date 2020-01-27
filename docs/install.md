## Install FeiranSMS - Feiran School Management System

### update ubuntu
```
sudo apt-get update
sudo apt-get dist-upgrade
```
### install ssh
```
sudo apt-get install ssh
```

### install python
```
sudo apt-get install python-dev
sudo apt-get install python3-venv
sudo apt-get install python-pip
sudo pip install --upgrade pip
```
- change Python's pip source to aliyun
```
sudo mkdir ~/.pip
sudo vim ~/.pip/pip.conf
```
Add the below to pip.conf:
```
[global]
index-url = http://mirrors.aliyun.com/pypi/simple/

[install]
trusted-host=mirrors.aliyun.com

[list]
format=columns
```

### install Mysql
```
sudo apt-get install mysql-server
mysql --version
sudo mysql_secure_installation
// 4 Y enter
sudo service mysql start
```

#### change mysql setting
```
cd /etc/mysql/
vim my.cnf
```
Add the below to the my.cnf
```
[client]
port = 3306
socket = /var/lib/mysql/mysql.sock
default-character-set=utf8

[mysqld]
port = 3306
socket = /var/lib/mysql/mysql.sock
character-set-server=utf8

[mysql]
no-auto-rehash
default-character-set=utf8
```

#### Add permit - Access denied for user 'root'@'localhost'
1. sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf
2. Add　‘skip-grant-tables'　then save and quit
3. service mysql restart
4. mysql -udebian-sys-maint -p
5.  mysql command:　
```
use mysql
update mysql.user set authentication_string=password('新密码') where user='root' and Host ='localhost';
update user set plugin="mysql_native_password";
flush privileges;
quit;
```
6. remove 'skip-grant-tables' from mysqld.cnf

#### create school database
```
sudo service mysql restart
mysql -uroot -p
```
Mysql command:
```
CREATE DATABASE `school` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

quit;
```



### create python virtenv
```
python3.6 -m venv /home/vcmt
```
#### activate
```
source /home/vcmt/bin/activate
```
#### deactivate
```
deactivate
```

### install django for the first time
```
pip install django
```
#### start project
```
django-admin.py  startproject feiranSMS
```
#### create app
```
python manage.py startapp school
```

#### add host name

- vim setting.py
- Add the domain name to the setting.pu
```
ALLOWED_HOSTS = ['feiran.online', 'www.feiran.online', ]
```

#### database
- install pymysql
```
pip install pymysql
```

- add database setting to the setting.py
```
# setting.py
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '数据库名称',
        'USER': '使用者',
        'PASSWORD': '数据库密码',
        'HOST': '127.0.0.1',
    }
}
```
- move database setting to mydb.cnf
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/etc/mydb.cnf',
        }
    }
}
```
copy mydb.cnf to /etc/mydb.cnf

mydb.cnf contents:

```
# my database connection

[client]
database = school
user = root
password = 123
HOST = 127.0.0.1
port = 3306
default-character-set = utf8
```

- support pymysql

vim __init__.py:
```
import pymysql
pymysql.install_as_MySQLdb()
```


#### install uWSGI
- install
```
sudo pip install uwsgi
```

- test
```
uwsgi --http :8000  --chdir ~/work/feiranSMS -w uwsig.wsgi
```
- set

mkdir -p ~/work/feiranSMS
cd ~/work/feiranSMS
vi uwsig.ini

```
# uwsig使用配置文件启动
[uwsgi]
# 项目目录
chdir=/home/lmh/work/feiranSMS
# 指定项目的application
module=feiranSMS.wsgi
#wsgi-file=feiranSMS/wsgi.py
# 指定sock的文件路径
socket=/opt/feiranSMS/uwsgi.sock
#http=127.0.0.1:9000
http= 0.0.0.0:9000
# 进程个数
workers=1
pidfile=/opt/feiranSMS/uwsgi.pid

# 启用主进程
master=true
# 自动移除unix Socket和pid文件当服务停止的时候
vacuum=true
# 序列化接受的内容，如果可能的话
thunder-lock=true
# 启用线程
enable-threads=true
#设置最大缓冲区
buffer-size = 65536
# 设置日志目录
daemonize=/opt/feiranSMS/uwsgi.log
```
- run
```
uwsgi uwsgi.ini
```
- kill uwsgi
  - get the PID
```
ps -ef|grep uwsgi
```
   - kill this PID
```
kill -9 PID
```

#### install Nginx
- install
```
sudo apt-get install nginx
```

- set

sudo vim  /home/lmh/work/feiranSMS/feiranSMS_nginx.conf
```

 server {
        listen 80;
        server_name feiran.online;
        charset UTF-8;

        location / {
                include uwsgi_params;
                uwsgi_pass unix:/opt/feiranSMS/uwsgi.sock;
                uwsgi_read_timeout 5;
        }

        location /static {
                expires 30d;
                autoindex on;
                add_header Cache-Control private;
                alias /home/lmh/work/feiranSMS/static/;
        }
}
```

- enable this site
```
sudo ln -s /home/lmh/work/feiranSMS/feiranSMS_nginx.conf  /etc/nginx/sites-enabled

service nginx configtest
```

- restart the service
```
service nginx restart
uwsgi /home/lmh/work/feiran/uwsgi.ini
```


#### create requirements
```
pip freeze > requirements.txt
```


### install django for the second time
- install python env
```
pip install -r requirements.txt
```
- sync database
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic
```

- test
```
python manage.py runserver 0.0.0.0:80
```
- kill the demo
```
fuser -k 80/tcp

netstat -anp

kill -9 PID

exit:
CTRL+C或Z
```


### disable debug

vim /home/lmh/work/feiran/settings.py
```
DEBUG = False
```