# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个辅助类
"""
模块介绍
-------

这是一个辅助类

设计模式：

    无

关键点：    

    （1）无  

主要功能：            

    （1）复制文件

    （2）获取配置                                                     

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



####### 辅助函数集 ###########################################################
### 设计模式：                                                            ###
###     无                                                               ###
### 关键点：                                                              ###
### （1）无                                                               ###
### 主要功能：                                                            ###
### （1）复制数据                                                         ###
### （2）获取配置                                                         ###
############################################################################



###### 辅助函数集 #####################################################################
######################################################################################



def get_config(config_path,config_key):
    """
    函数功能：

        定义一个获取配置函数

    参数：
        config_path (str): 参数路径
        config_key (str): 参数关键字

    返回：
        config_value (str): 参数值
    """

    yaml.warnings({'YAMLLoadWarning':False})
    file = open(config_path,'r',encoding = 'utf-8')
    cfg = file.read()
    cfg_dict = yaml.load(cfg)
    config_value = cfg_dict[config_key]

    return config_value



def copy_file(src,dst):
    """
    函数功能：

        定义一个复制文件函数

    参数：
        src (str): 源文件路径
        dst (str): 目标文件路径

    返回：
        无
    """   

    shutil.copy(src,dst)

    return 'copy file successful!'



########################################################################################################
########################################################################################################

