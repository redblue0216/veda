# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个vedadata类，主要提供配置管理和初始化功能
"""
模块介绍
-------

这是一个vedadata类，主要提供配置管理和初始化功能

设计模式：

    无

关键点：    

    （1）os

主要功能：            

    （1）配置管理

    （2）初始化                                                   

使用示例
-------


类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



import os 
import yaml
import sqlite3
import getpass



####### vedadata命令角色类 ##################################################
### 设计模式：                                                            ###
###     无                                                               ###
### 关键点：                                                              ###
### （1）os                                                              ###
### 主要功能：                                                            ###
### （1）配置管理                                                          ###
### （2）初始化                                                           ###
############################################################################



###### vedadata命令角色类 #####################################################################
##############################################################################################



class VedadataRole(object):
    """
    类介绍：

        这是一个veda配置和元数据管理类
    """

    
    def __init__(self,name):
        """
        属性功能：

            初始化属性

        参数：
            name (str): 命令模块名称
        """

        self.name = name


    def create_veda_workspace(self,**kwargs):
        """
        方法功能：

            定义一个创建veda工作空间的方法

        参数：
            veda_workspace (str): veda工作空间路径
        
        返回：
            veda_workspace (str): veda工作空间路径
        """

        veda_workspace = kwargs['veda_workspace']
        vedapkg_packages_path = '{}/vedapkg/packages'.format(veda_workspace)
        vedapkg_installation_path = '{}/vedapkg/installation'.format(veda_workspace)
        vedaenv_modulefiles_path = '{}/vedaenv/modulefiles'.format(veda_workspace)
        vedadata_config_path = '{}/vedadata/config'.format(veda_workspace)
        vedainfo_sqlite3_path = '{}/vedainfo/sqlite3'.format(veda_workspace)
        vedacontroller = '{}/vedacontroller'.format(veda_workspace)
        if not os.path.exists(vedapkg_packages_path):
            os.makedirs(vedapkg_packages_path)
        if not os.path.exists(vedapkg_installation_path):
            os.makedirs(vedapkg_installation_path)
        if not os.path.exists(vedaenv_modulefiles_path):
            os.makedirs(vedaenv_modulefiles_path)
        if not os.path.exists(vedadata_config_path):
            os.makedirs(vedadata_config_path)
        if not os.path.exists(vedainfo_sqlite3_path):
            os.makedirs(vedainfo_sqlite3_path)
        if not os.path.exists(vedacontroller):
            os.makedirs(vedacontroller)
        print("---------------------------- Veda workspace create successful! ---------------------------------")

        return veda_workspace


    def create_config_file(self,**kwargs):
        """
        方法功能：

            定义一个创建配置文件的方法

        参数：
            veda_workspace (str): veda工作空间路径

        返回：
            无
        """

        veda_workspace = kwargs['veda_workspace']
        data={
            'veda_workspace': veda_workspace,
        }
        yaml_path = '{}/vedadata/config/veda_local_config.yaml'.format(veda_workspace)
        file=open(yaml_path,'w',encoding='utf-8')
        yaml.dump(data,file)
        file.close()
        veda_user = getpass.getuser()
        veda_hidden_path = '/home/{}/.veda/config'.format(veda_user)
        os.system('mkdir -p {}'.format(veda_hidden_path))
        veda_tmp_path = '/home/{}/.veda/tmp'.format(veda_user)
        os.system('mkdir -p {}'.format(veda_tmp_path))
        dst = '{}/veda_local_config.yaml'.format(veda_hidden_path)
        os.system('cp {} {}'.format(yaml_path,veda_hidden_path))
        print("---------------------------- Veda config create successful! ---------------------------------")


    def create_sqlite3_db(self,**kwargs):
        """
        方法功能：

            定义一个创建后端数据库的方法

        参数：
            veda_workspace (str): veda工作空间路径

        返回：
            无
        """

        veda_workspace = kwargs['veda_workspace']
        sqlite3_path = '{}/vedainfo/sqlite3/veda_local_sqlite3.db'.format(veda_workspace)
        conn = sqlite3.connect(sqlite3_path)
        conn.close()
        print("---------------------------- Veda info create successful! ---------------------------------")



######################################################################################################################
######################################################################################################################


