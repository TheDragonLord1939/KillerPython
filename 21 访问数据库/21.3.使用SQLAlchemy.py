# !/usr/bin/env python3
# -*- coding:utf-8 -*-

#导入
from sqlalchemy import Column, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import String, INT, DECIMAL
from sqlalchemy.ext.declarative import declarative_base

#创建对象的基类
Base = declarative_base()

#定义User对象
class Trade(Base):
    #表的名字
    __tablename__ = 'trade'

    #表的结构
    id = Column('id', INT, primary_key=True)
    name = Column('name', String(20))
    account = Column('account', String(20))
    saving = Column('saving', DECIMAL)
    expend = Column('expend', DECIMAL)
    income = Column('income', DECIMAL)

#初始化数据库连接
engine = create_engine('mysql+pymysql://root:123456@node3:3306/test')
#创建DBSession类型
DBSession = sessionmaker(bind=engine)

#创建Session对象
session = DBSession()
#创建新User对象
new_user = Trade(id=11111, name='Bob',account='123456789',saving=11.1,expend=11.1,income=11.1)
#添加到Session
session.add(new_user)
#提交即保存到数据库
session.commit()
#关闭session
session.close()

print('insert over.')

#创建Session
session = DBSession()
#创建Query查询，filter是where条件，最后调用one（）返回唯一行，如果调用all（）则返回所有行：
trade = session.query(Trade).filter(Trade.id == 2).one()
#打印类型和对象的name属性
print('type:', type(trade))
print('name:', trade.name)

#关闭Session
session.close()






