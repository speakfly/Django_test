# apartment_system

//首先配置环境  使用的是Ubuntu,该系统自带python3

sudo apt-get update                     //跟新软件
sudo apt-get install mysql-server       //安装MySQL
pip3 install Django                     //安装Django
pip3 install suit                       //安装后台插件
pip3 install PyMySQL                    //python 连接MySQL的驱动
pip3 install xlrd                       //python 读取excel插件
pip3 install xlwt                       //python 写excel插件


//接下来是创建工程  在终端执行如下命令
django-admin startproject dj2           //创建工程 
cd dj2                                  //进入目录
python3 manange.py startapp app         //创建app
vim dj2/settings.py                     //编写配置文件


//dj2/setting.py

//首先可以设置
ALLOWED_HOSTS = ['*']                  //允许非本台电脑进行访问  还需要把对应的端口给开放出来
INSTALLED_APPS  中添加  'app',         //添加应用
INSTALLED_APPS  第一行添加 'suit',      //添加后台插件


//设置数据库配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'apartment',
        'USER': 'ming',
        'PASSWORD': 'ming',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}


//设置中文时区和时间显示格式
LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = False

USE_TZ = False
DATETIME_FORMAT = 'Y-m-d H:i:s'
DATA_FORMAT = 'Y-m-d'

//suit插件配置
STATIC_URL = '/static/'

SUIT_CONFIG = {
    
    'ADMIN_NAME':'apartment_system',
    'LIST_PER_PAGE':10,
}


//配置dj2/setting.py已经完成


vim app/models.py
vim app/admin.py


//设置好了，就可以启动MySQL服务

sudo service mysql start

mysql -u root -p
create database apartment default character set utf8;
grant all privileges on databasename.* to 'username@'%' identified by'password' with grant option;
exit

//然后执行命令

python3 manange.py createsuperuser

//下载可以启动查看自己的后台情况
python3 manange.py runserver 8080

//打开浏览器 127.0.0.1：8080/admin

//接下来是处理视图
vim app/views.py
//还有处理html文件
mkdir app/templates
vim app/templates/index.html

//最后是处理url
vim dj2/urls.py

//基本处理到这里，如有建议请留言
