# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个vedapkg类，主要管理本地算法包的一系列操作
"""
模块介绍
-------

这是一个vedapkg类，主要管理本地算法包的一系列操作

设计模式：

    无

关键点：    

    （1）os  

主要功能：            

    （1）创建包空间

    （2）添加组件

    （3）打包                                                     

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
import tarfile



####### vedapkg命令角色类 ###################################################
### 设计模式：                                                            ###
###     无                                                               ###
### 关键点：                                                              ###
### （1）os                                                              ###
### 主要功能：                                                            ###
### （1）创建空间                                                         ###
### （2）添加组件                                                         ###
### （3）打包                                                             ###
############################################################################



###### vedapkg命令角色类 #####################################################################
#############################################################################################



class VedapkgRole(object):
    """
    类介绍：

        这是一个Vedapkg个体算法包的相关命令实现角色类，主要功能包括创建算法包和添加组件，主要技术基于tar归档技术新建了vedapkg文档格式。
    """

    
    def __init__(self,name):
        """
        属性功能：

            初始化属性

        参数
            name (str): 命令模块名称
        """

        self.name = name


    def vedapkg_create_workspace(self,**kwargs):
        """
        方法功能：

            定义一个创建vedapkg工作空间的方法

        参数：
            无

        返回：
            无
        """

        veda_user = getpass.getuser()
        veda_hidden_path = '/home/{}/.veda/config'.format(veda_user)
        config_path = '{}/veda_local_config.yaml'.format(veda_hidden_path)
        config_key = 'veda_workspace'
        veda_workspace = get_config(config_path,config_key)
        vedapkg_name = kwargs['vedapkg_name']
        vedapkg_base_path = '{}/vedapkg/installation/{}'.format(veda_workspace,vedapkg_name)
        vedapkg_data_path = '{}/Data/'.format(vedapkg_base_path)
        vedapkg_run_path = '{}/Run/'.format(vedapkg_base_path)
        vedapkg_info_path = '{}/Info/'.format(vedapkg_base_path)
        vedapkg_doc_path = '{}/Doc/'.format(vedapkg_base_path)
        if not os.path.exists(vedapkg_data_path):
            os.makedirs(vedapkg_data_path)
        if not os.path.exists(vedapkg_run_path):
            os.makedirs(vedapkg_run_path)
        if not os.path.exists(vedapkg_info_path):
            os.makedirs(vedapkg_info_path)
        if not os.path.exists(vedapkg_doc_path):
            os.makedirs(vedapkg_doc_path)
        print("---------------------------- Vedapkg create workspace successful! ---------------------------------")


    def vedapkg_add_component(self,**kwargs):
        """
        方法功能：

            定义一个vedapkg添加组件的方法

        参数：
            vedapkg_name (str): 包名称
            vedapkg_component_type (str): 包类型
            vedapkg_component_path (str): 包路径

        返回：
            无
        """

        veda_user = getpass.getuser()
        veda_hidden_path = '/home/{}/.veda/config'.format(veda_user)
        config_path = '{}/veda_local_config.yaml'.format(veda_hidden_path)
        config_key = 'veda_workspace'
        veda_workspace = get_config(config_path,config_key)    
        vedapkg_name = kwargs['vedapkg_name']
        vedapkg_component_type = kwargs['vedapkg_component_type']
        vedapkg_component_path = kwargs['vedapkg_component_path']
        dst = '{}/vedapkg/installation/{}/{}'.format(veda_workspace,vedapkg_name,vedapkg_component_type)
        shutil.copy(vedapkg_component_path,dst)
        print("---------------------------- Vedapkg add component successful! ---------------------------------")


    def vedapkg_pack(self,**kwargs):
        """
        方法功能：

            定义一个vedapkg打包方法

        参数：
            vedapkg_name (str): 包名称

        返回:
            无
        """

        veda_user = getpass.getuser()
        veda_hidden_path = '/home/{}/.veda/config'.format(veda_user)
        config_path = '{}/veda_local_config.yaml'.format(veda_hidden_path)
        config_key = 'veda_workspace'
        veda_workspace = get_config(config_path,config_key)
        vedapkg_name = kwargs['vedapkg_name']
        vedapkg_pack_path = '{}/vedapkg/packages/{}.vedapkg'.format(veda_workspace,vedapkg_name)
        vedapkg_installation_path = '{}/vedapkg/installation'.format(veda_workspace)
        tar = tarfile.open(vedapkg_pack_path,'w:gz')
        current_workspace = os.getcwd()
        os.chdir(vedapkg_installation_path)
        tar.add(vedapkg_name)
        tar.close()
        os.chdir(current_workspace)
        print("---------------------------- Vedapkg pack successful! --------------------------------------")



####################################################################################################################
####################################################################################################################


