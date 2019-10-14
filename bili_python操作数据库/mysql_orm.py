# -*- coding: utf-8 -*-
# @File    : mysql_orm.py
# @Date    : 2019-10-12
# @Author  : Zhang.Cookie

"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,Boolean  #,DateTime

engine = create_engine('mysql://root:123@localhost:3306/orm_news',encoding="utf-8", echo=True)   #对应得user pw  端口 数据裤名
Basemodel = declarative_base()

class News(Basemodel):
    __tablename__ = 'news'
    id = Column(Integer,Primary_key=True,autoincrement=True)
    tutle = Column(String(200),nullable=False)
    # create_at = Column(DateTime)
    is_valid = Column(Boolean)

if __name__ == "__main__":
    #Base.metadata.create_all()
    News.metadata.create_all(engine)

# conn = engine.connect()
# result = conn.execute("select 1")
# print(result.fetchone())
#from mysql_orm import engine
#from mysql_orm import News
"""



from sqlalchemy import *
from sqlalchemy.orm import *

#ORM使用,创建表
#参考链接 https://blog.csdn.net/will130/article/details/48502053
# https://www.cnblogs.com/chengege/articles/11099001.html
def create_orm():
    #from sqlalchemy.ext.declarative import declarative_base
    #功能:创建数据库表格，初始化数据库

    #定义引擎
    engine = create_engine('mysql+mysqlconnector://root:123@localhost:3306/orm_news')
    # engine = create_engine('mysql+mysqlconnector://root:111111@localhost:3306/testalchemy')
    #绑定元信息
    metadata = MetaData(engine)

    #创建表格，初始化数据库
    user = Table('user', metadata,
        Column('id', Integer, primary_key = True),
        Column('name', String(20)),
        Column('fullname', String(40)))
    address = Table('address', metadata,
        Column('id', Integer, primary_key = True),
        Column('user_id', None, ForeignKey('user.id')),
        Column('email', String(60), nullable = False),
    )
    #创建数据表，如果数据表存在则忽视！！！
    metadata.create_all(engine)
    #获取数据库链接，以备后面使用！！！！！
    conn = engine.connect()


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import sessionmaker


engine = create_engine('mysql+mysqlconnector://root:123@localhost:3306/orm_news')
Base=declarative_base()

#多对一:假设多个员工可以属于一个部门,而多个部门不能有同一个员工(只有创建公司才把员工当骆驼用,一个员工身兼数职)
class Dep(Base):
    __tablename__='dep'
    id=Column(Integer,primary_key=True,autoincrement=True)
    dname=Column(String(64),nullable=False,index=True)

class Emp(Base):
    __tablename__='emp'
    id=Column(Integer,primary_key=True,autoincrement=True)
    ename=Column(String(32),nullable=False,index=True)
    dep_id=Column(Integer,ForeignKey('dep.id'))

def init_db():
    Base.metadata.create_all(engine)

def drop_db():
    Base.metadata.drop_all(engine)

drop_db()
init_db()
Session=sessionmaker(bind=engine)
session=Session()

#增
row_obj=Dep(dname='销售') #按关键字传参,无需指定id,因其是自增长的
session.add(row_obj)
session.add_all([
    Dep(dname='技术'),
    Dep(dname='运营'),
    Dep(dname='人事'),
])

session.commit()














