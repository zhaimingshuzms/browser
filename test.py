from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, Column, Integer, MetaData, String

# 连接数据库
engine = create_engine('sqlite:///anno.db')

# 创建数据库会话
Session = sessionmaker(bind=engine)
db = Session()

# 获取元数据
metadata = MetaData()

# 定义表结构
table = Table('post', metadata,
              Column('id', Integer, primary_key=True),
              Column('author_id', Integer),
              Column('created', String),
              Column('title', String),
              Column('body', String),
              Column('body2', String),
              Column('image_path', String),
              )

# 执行查询
query = db.query(table)

# 读取数据
for row in query:
    print(row)

# 关闭数据库会话
db.close()
