# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是信息辅助类
"""
模块介绍
-------

这是一个信息辅助类

设计模式：

    无

关键点：    

    （1）sqlite3  

主要功能：            

    （1）写数据

    （2）读数据                                                     

使用示例
-------


类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



import yaml
import shutil
import os
import getpass
from Veda.utils.tools import *
import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String
from sqlalchemy.orm import sessionmaker



####### 信息辅助类 ##########################################################
### 设计模式：                                                            ###
###     无                                                               ###
### 关键点：                                                              ###
### （1）sqlite3                                                          ###
### 主要功能：                                                            ###
### （1）写数据                                                           ###
### （2）读数据                                                           ###
############################################################################



###### 信息辅助类 #####################################################################
######################################################################################



def get_veda_workspace():
    """
    函数功能：

        定义一个获取工作空间的函数
    """

    veda_user = getpass.getuser()
    veda_hidden_path = '/home/{}/.veda/config'.format(veda_user)
    config_path = '{}/veda_local_config.yaml'.format(veda_hidden_path)
    config_key = 'veda_workspace'
    veda_workspace = get_config(config_path,config_key)

    return veda_workspace



def create_sqlite3_tmp_db(path):
    """
    函数功能：

        定义一个创建数据库文件的函数

    参数：
        path (str): 路径
    """

    conn = sqlite3.connect(path)
    conn.close()



def create_sqlite3_tmp_engine(veda_workspace):
    """
    函数功能：

        定义一个创建数据库引擎的函数

    参数：
        veda_workspace (str): 路径
    """

    engine = create_engine('sqlite:///{}/vedainfo/sqlite3/veda_local_sqlite3.db'.format(veda_workspace))
    # engine = create_engine('sqlite:////home/shihua/tulip/AEwork/Veda/demo.db')

    return engine



def create_sqlite3_declarative_base():
    """
    函数功能：

        定义一个创建ORM抽象类的函数

    参数：
        无

    返回：
        Base (Object)：ORM实例
    """    

    Base = declarative_base()

    return Base



def create_sqlite3_session(engine):
    """
    函数功能：

        定义一个创建ORM抽象类的函数

    参数：
        engine (object): 连接引擎

    返回：
        session (Object)：会话实例
    """      

    Session = sessionmaker(bind = engine)
    session = Session()

    return session


### 预执行语句
# tmp_path = '{}/vedainfo/sqlite3/veda_local_sqlite3.db'.format(veda_workspace)
# create_sqlite3_tmp_db(tmp_path)
veda_workspace = get_veda_workspace()
engine = create_sqlite3_tmp_engine(veda_workspace)
Base = create_sqlite3_declarative_base()


### 数据库ORM类
class VedapkgInfo(Base):

    __tablename__ = "VedapkgInfo"

    name = Column(String(200),primary_key = True)
    version = Column(String(200))
    author = Column(String(200))
    summary = Column(String(1000))
    state = Column(String(200))
    requires = Column(String(600))


### 预执行语句
session = create_sqlite3_session(engine)



#################################################################################################
#################################################################################################


