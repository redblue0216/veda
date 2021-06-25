# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个vedacontroller类，主要提供一些特殊操作
"""
模块介绍
-------

这是一个vedacontroller类，主要提供一些特殊操作

设计模式：

    无

关键点：    

    （1）Minio  

主要功能：            

    （1）推数据

    （2）拉数据                                                     

使用示例
-------


类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



from ServerManager.ServerCommandInterface import *



####### vedacontroller命令角色类 ############################################
### 设计模式：                                                            ###
###     无                                                               ###
### 关键点：                                                              ###
### （1）Minio                                                           ###
### 主要功能：                                                            ###
### （1）推数据                                                           ###
### （2）拉数据                                                           ###
############################################################################



###### vedacontroller命令角色类 #####################################################################
####################################################################################################



class VedacontrollerRole(object):
    """
    类介绍：

        这是一个Veda算法库控制管理类，主要功能包括与远端算法库的推送、拉取算法包的操作，
    """

    
    def __init__(self,name):
        """
        属性功能：

            初始化属性

        参数：
            name (str): 命令模块名称
        """

        self.name = name


    def vedacontroller_pull_remote(self,**kwargs):
        """
        方法功能：

            定义一个从远端拉取算法包的方法

        参数：
            connect_info (str): 连接地址
            access_key (str): 用户名
            secret_key (str): 密码
            secure (bool): 安全设置
            object_file (str): 文件名称
            bucket (str): 桶名称

        返回：
            无
        """

        connect_info = kwargs['connect_info']
        access_key = kwargs['access_key']
        secret_key = kwargs['secret_key']
        secure = kwargs['secure']
        object_file = kwargs['object_file']
        bucket = kwargs['bucket']
        minio_interface = ServerManagerCommandInterface()
        minio_value = minio_interface.GetObject(connect_info = connect_info,
                                                access_key = access_key,
                                                secret_key = secret_key,
                                                secure = secure,
                                                object_file = object_file,
                                                bucket = bucket)                              
        print("---------------------- Vedacontroller pull remote successful! -------------------------")


    def vedacontroller_push_remote(self,**kwargs):
        """
        方法功能：

            定义一个向远端推送算法包的方法

        参数：
            connect_info (str): 连接地址
            access_key (str): 用户名
            secret_key (str): 密码
            secure (bool): 安全设置
            object_file (str): 文件名称
            bucket (str): 桶名称

        返回：
            无        
        """

        connect_info = kwargs['connect_info']
        access_key = kwargs['access_key']
        secret_key = kwargs['secret_key']
        secure = kwargs['secure']
        object_file = kwargs['object_file']
        bucket = kwargs['bucket']
        minio_interface = ServerManagerCommandInterface()
        minio_value = minio_interface.PutObject(connect_info = connect_info,
                                                access_key = access_key,
                                                secret_key = secret_key,
                                                secure = secure,
                                                object_file = object_file,
                                                bucket = bucket)                              
        print("---------------------- Vedacontroller push remote successful! -------------------------")        



#############################################################################################################
#############################################################################################################


