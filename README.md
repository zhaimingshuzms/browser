#### Record-Pictures
- Record Pictures是一个browser
- 在[原项目](https://github.com/ddy-ddy/record-picture/tree/master/record_picture)的基础上进行魔改
#### 用到的技术：

- 前端：html+css+JavaScript（目前没有使用类似vue，react等web框架，课设的时候技术太菜(ಥ﹏ಥ)）
- 后端：python flask

#### 运行步骤:

Step1：安装依赖库

```shell
pip install -r requirements.txt
```

Step2：运行app.py文件
```shell
python app.py
```
Step3：登陆
```shell
登陆账号：duanyu1@qq.com 
密码：123456
```
Step4：删库跑路并重新初始化
```shell
python gen.py
```

- 数据库为data.db文件
- 项目主内容在record_picture文件夹中
- 项目文档在document中，使用markdown的格式，导出为html格式
- 项目总文档和ppt在document目录下（原项目的文档）


#### 项目总框架（原项目的框架）:

````python
.
├── README.md																#项目说明文件
├── app.py																	#项目启动入口
├── config.py																#项目配置文件
├── data.db #项目数据库,使用SQlite
├── document #存放项目说明文档及技术难题
├── record_picture													#项目
│   ├── __init__.py													#配置flask
│   ├── commands.py													#[py][存放指令函数]	
│   ├── errors.py														#[py][存放错误页面调转函数]
│   ├── models.py														#[py][存放数据库表设计函数]
│   ├── static															#[文件夹][存放项目的static]
│   │   ├── css
│   │   ├── image
│   │   └── js
│   ├── templates														#[文件夹][存放所有的html页面]
│   │   ├── base.html
│   │   ├── errors
│   │   │   └── 404.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── show_page_index.html
│   │   ├── user_map.html
│   │   ├── user_pictures.html
│   │   ├── user_profile.html
│   │   ├── user_search.html
│   │   └── user_upload.html
│   ├── util.py															#[py][存放功能函数]
│   └── view.py															#[py][存放视图]
└── user_uploads#用户上传的文件夹
````

