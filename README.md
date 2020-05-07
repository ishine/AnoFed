# AnoFed
用于标注、查看和修改结果的中文NLP分词工具，使用Django开发，使用前需要 pip 安装 Django 和 mysqlclient，结果保存在数据库。

# 功能
## 标注功能
打开 /func1 网页，右上角按钮上传文本,左侧栏选择主题，右侧栏显示该主题下已保存的词
<img src="https://github.com/vacaly/AnoFed/blob/master/pics/1.png" alt="alt text" width="600"><br>
中间文本栏用鼠标标记需要添加的词语，弹出框提示该待添加词语的全文出现次数，可以修改词频和词性
<br><img src="https://github.com/vacaly/AnoFed/blob/master/pics/2.png" alt="alt text" width="600"><br>
<br><img src="https://github.com/vacaly/AnoFed/blob/master/pics/3.png" alt="alt text" width="600"><br>

## 反馈功能
打开 /func2 网页，右上角按钮上传文本，中间栏显示分词结果，下图使用的是结巴分词，你可以修改 [view.py](https://github.com/vacaly/AnoFed/blob/master/AnoFed/views.py#L48)文件里 jiebaToken 函数，更换分词器。图中不同颜色代表不同词性，黄色为名词，蓝色为动词（之后会丰富词性种类的）
<br><img src="https://github.com/vacaly/AnoFed/blob/master/pics/4.png" alt="alt text" width="600"><br>
分词结果可以进行编辑，比如本文中“上看”并不是一个动词，“上”为介词，“看”为动词，因此可以点击词语旁边的叉号删除这个分词结果。
<br><img src="https://github.com/vacaly/AnoFed/blob/master/pics/5.png" alt="alt text" width="600"><br>
删除成功后，出错句子和错分词语被保存到数据库。

## Build & Run
- 用适合自己系统的方式安装 Django 和 mysqlclient
- 创建 Django 项目
  ```bash
  $ django-admin startproject DjangoProjects
  $ cd DjangoProjects
  $ django-admin startapp AnoFed
  ```
  目录结构如下
  ```
  DjangoProjects
  |-- DjangoProjects
  |   |-- __init__.py
  |   |-- settings.py
  |   |-- urls.py
  |   `-- wsgi.py
  |-- AnoFed
  |   |-- __init__.py
  |   |-- admin.py
  |   |-- apps.py
  |   |-- migrations
  |   |-- models.py
  |   |-- tests.py
  |   `-- views.py
  `-- manage.py
  ```
  用本项目的 models.py settings.py urls.py views.py 代替原始文件
  将本项目的 /templates /static 添加到 /AnoFed目录下
  修改[settings.py](https://github.com/vacaly/AnoFed/blob/master/AnoFed/settings.py#L77)中关于数据库的配置
  ```python
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangodb',
        'USER': 'USER',
        'PASSWORD': 'PASSWORD',
        'HOST':'localhost',
        'PORT':'3306',
    }
  }
  ```
  需要在mysql中创建一个同名数据库，数据库对应的用户名和密码要正确
  ```mysql
  mysql> CREATE DATABASE djangodb
  ```
  修改[settings.py](https://github.com/vacaly/AnoFed/blob/master/AnoFed/settings.py#L124)中静态文件路径
  ```python
  STATIC_URL = 'your-django-peojects-path/AnoFed/static/'
  ```
  在命令行运行
  ```bash
  $ python manage.py migrate
  $ python manage.py makemigrations AnoFed
  $ python manage.py migrate AnoFed
  ```
  看到几行 "Creating table…" 的字样，数据表就创建好了。
- 运行项目
  在命令行运行
  ```bash
  $ python manage.py runserver
  ```
  在浏览器打开http://0.0.0.0:8000/func1/ 进行标注，http://0.0.0.0:8000/func2/ 进行反馈
## 构想
最近会持续开发这个项目，六月前会有一次主要更新
- [ ] 关系标注功能（同义、反义关系，实体间关系）
- [ ] 分词器和关系提取器进一步模块化，从网页模版代码中独立出来
- [ ] 用反馈结果重新训练分词器和关系提取器
