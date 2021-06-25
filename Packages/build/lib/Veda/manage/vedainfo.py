# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个vedainfo类，主要提供算法包信息的一系列操作
"""
模块介绍
-------

这是一个vedainfo类，主要提供算法包信息的一系列操作

设计模式：

    无

关键点：    

    （1）clickhouse

    （2）sqlite3   

主要功能：            

    （1）本地信息查询，注册，更新

    （2）远端信息查询，注册，更新                                                    

使用示例
-------


类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



from Veda.utils.tools import *
import os
import getpass
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String
from sqlalchemy.orm import sessionmaker
from Veda.utils.info import *
from clickhouse_driver import Client



####### vedainfo命令角色类 ##################################################
### 设计模式：                                                            ###
###     无                                                               ###
### 关键点：                                                              ###
### （1）clickhouse                                                      ###
### （2）sqlite3                                                         ###
### 主要功能：                                                            ###
### （1）本地信息查询，注册，更新                                          ###
### （2）远端信息查询，注册，更新                                          ###
############################################################################



###### vedainfo命令角色类 #####################################################################
#############################################################################################



class VedainfoRole(object):
    """
    类介绍：

        这是一个Veda算法库信息维护管理类，主要功能管理本地算法库和远端算法库中算法包的相关信息，主要技术采用Sqlite3和clickhouse
    """

    
    def __init__(self,name):
        """
        属性功能：

            初始化属性

        参数：
            name (str): 命令模块名称
        """

        self.name = name


    def vedainfo_init(self,**kwargs):
        """
        方法功能：

            定义一个vedainfo本地信息初始化方法

        参数：
            无

        返回：
            无
        """

        Base.metadata.create_all(engine)
        print("---------------------------- Veda info init successful! ---------------------------------")


    def vedainfo_register(self,**kwargs):
        """
        方法功能：

            定义一个vedainfo本地注册方法

        参数：
            name (str): 包名称
            version (str): 版本
            author (str): 作者
            summary (str): 介绍
            state (str): 状态
            requires (str): 依赖

        返回：
            无
        """

        name = kwargs['name']
        version = kwargs['version']
        author = kwargs['author']
        summary = kwargs['summary']
        state = kwargs['state']
        requires = kwargs['requires']
        vedainfo = VedapkgInfo(
            name = name,
            version = version,
            author = author,
            summary = summary,
            state = state,
            requires = requires
        )
        session.add(vedainfo)
        session.commit()
        print("---------------------------- Veda info register successful! ---------------------------------")


    def vedainfo_update(self,**kwargs):
        """
        方法功能：

            定义一个vedainfo本地更新信息的方法

        参数：
            name (str): 包名称
            info_key (str): 更新类型
            info_value (str): 更新内容
        """

        name = kwargs['name']
        info_key = kwargs['info_key']
        info_value = kwargs['info_value']
        vedainfo = session.query(VedapkgInfo).filter_by(name = name).first()
        if info_key == 'version':
            vedainfo.version = info_value
        elif info_key == 'author':
            vedainfo.author = info_value
        elif info_key == 'summary':
            vedainfo.summary = info_value
        elif info_key == 'state':
            vedainfo.state = info_value
        else:
            vedainfo.requires = info_value
        session.commit()
        print("---------------------------- Veda info update successful! ---------------------------------")


    def vedainfo_query(self,**kwargs):
        """
        方法功能：

            定义一个vedainfo本地查询的方法

        参数： 
            name (str): 包名称

        返回：
            vedapkg_info_dict (Dict): 包信息字典
        """

        name = kwargs['name']
        vedainfo = session.query(VedapkgInfo).filter_by(name = name).first()
        vedapkg_info_dict = {}
        vedapkg_info_dict['name'] = name 
        vedapkg_info_dict['version'] = vedainfo.version
        vedapkg_info_dict['author'] = vedainfo.author
        vedapkg_info_dict['summary'] = vedainfo.summary
        vedapkg_info_dict['state'] = vedainfo.state
        vedapkg_info_dict['requires'] = vedainfo.requires
        print("---------------------------- Veda info query successful! ---------------------------------")

        return vedapkg_info_dict


    def vedainfo_register_remote(self,**kwargs):
        """
        方法功能：

            定义一个vedainfo远端注册方法

        参数：
            name (str): 包名称
            version (str): 版本
            author (str): 作者
            summary (str): 介绍
            state (str): 状态
            requires (str): 依赖
            host (str): 地址
            port （str): 端口
            clickhouse_user (str): clickhouse用户名
            clickhouse_password (str): clickhouse密码

        返回：
            无
        """        

        name = kwargs['name']
        version = kwargs['version']
        author = kwargs['author']
        summary = kwargs['summary']
        state = kwargs['state']
        requires = kwargs['requires']
        host = kwargs['host']
        port = kwargs['port']
        clickhouse_user = kwargs['clickhouse_user']
        clickhouse_password = kwargs['clickhouse_password']
        client = Client(host=host,port=port,user=clickhouse_user,password=clickhouse_password)
        insert_sql = "INSERT INTO veda.vedainfo VALUES ('{}','{}','{}','{}','{}','{}')".format(name,version,author,summary,state,requires)
        insert_result = client.execute(insert_sql)
        print("---------------------------- Veda info register remote  successful! ---------------------------")


    def vedainfo_query_remote(self,**kwargs):
        """
        方法功能：

            定义一个vedainfo远端查询的方法

        参数： 
            name (str): 包名称
            host (str): 地址
            port （str): 端口
            clickhouse_user (str): clickhouse用户名
            clickhouse_password (str): clickhouse密码            

        返回：
            query_result (Dict): 包信息字典
        """        

        name = kwargs['name']
        host = kwargs['host']
        port = kwargs['port']
        clickhouse_user = kwargs['clickhouse_user']
        clickhouse_password = kwargs['clickhouse_password']
        client = Client(host=host,port=port,user=clickhouse_user,password=clickhouse_password)
        query_sql = "SELECT * FROM veda.vedainfo WHERE name = '{}'".format(name)
        query_result = client.execute(query_sql)
        print("---------------------------- Veda info query remote successful! ---------------------------")

        return query_result
        
    
    def vedainfo_update_remote(self,**kwargs):
        """
        方法功能：

            定义一个vedainfo远端更新信息的方法

        参数：
            name (str): 包名称
            info_key (str): 更新类型
            info_value (str): 更新内容
            host (str): 地址
            port （str): 端口
            clickhouse_user (str): clickhouse用户名
            clickhouse_password (str): clickhouse密码              

        返回：
            无
        """   

        name = kwargs['name']
        info_key = kwargs['info_key']
        info_value = kwargs['info_value']
        host = kwargs['host']
        port = kwargs['port']
        clickhouse_user = kwargs['clickhouse_user']
        clickhouse_password = kwargs['clickhouse_password']
        client = Client(host=host,port=port,user=clickhouse_user,password=clickhouse_password)
        update_sql = "ALTER TABLE veda.vedainfo UPDATE {} = '{}' WHERE name = '{}'".format(info_key,info_value,name)
        update_result = client.execute(update_sql)
        print("---------------------------- Veda info update remote successful! ---------------------------------")        


    
################################################################################################################################################
################################################################################################################################################


