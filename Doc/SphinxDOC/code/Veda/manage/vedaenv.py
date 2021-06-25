# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个vedaenv类，提供环境配置和分布式命令运行功能
"""
模块介绍
-------

这是一个vedaenv类，提供环境配置和分布式命令运行功能

设计模式：

    无

关键点：    

    （1）Environment Modules

    （2）Ansible  

主要功能：            

    （1）环境配置

    （2）分布式命令运行                                                     

使用示例
-------


类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



import getpass
import os



####### vedaenv命令角色类 ###################################################
### 设计模式：                                                            ###
###     无                                                               ###
### 关键点：                                                              ###
### （1）Environment Modules                                              ###
### （2）Ansible                                                         ###
### 主要功能：                                                            ###
### （1）环境配置                                                          ###
### （2）分布式命令运行                                                    ###
############################################################################



###### vedaenv命令角色类 #####################################################################
#############################################################################################



class VedaenvRole(object):
    """
    类介绍：

        这是一个Veda算法库运行环境动态管理配置类，主要功能动态配置算法运行环境，主要技术采用EnvironmentModules和Ansible
    """
    

    def __init__(self,name):
        """
        属性功能：

            初始化属性

        参数：
            name (str): 命令模块名称
        """        

        self.name = name


    def vedaenv_avail(self,**kwargs):
        """
        方法功能：

            定义一个vedaenv查看可用环境模板方法

        参数：
            avail_para (str): 环境名称

        返回：
            无
        """

        veda_user = getpass.getuser()
        avail_para = kwargs['avail_para']
        if avail_para == 'all':
            os.system("echo '#!/bin/bash' >> /home/{}/.veda/tmp/module_avail.sh".format(veda_user))
            os.system("echo 'module avail' >> /home/{}/.veda/tmp/module_avail.sh".format(veda_user))
            os.system("bash /home/{}/.veda/tmp/module_avail.sh".format(veda_user))
            os.system("rm -rf /home/{}/.veda/tmp/module_avail.sh".format(veda_user))
        else:
            os.system("echo '#!/bin/bash' >> /home/{}/.veda/tmp/module_avail.sh".format(veda_user))
            os.system("echo 'module avail {}' >> /home/{}/.veda/tmp/module_avail.sh".format(avail_para,veda_user))
            os.system("bash /home/{}/.veda/tmp/module_avail.sh".format(veda_user))
            os.system("rm -rf /home/{}/.veda/tmp/module_avail.sh".format(veda_user))            
        print("------------------------ Veda env avail successful! --------------------")


    def vedaenv_list(self,**kwargs):
        """
        方法功能：

            定义一个vedaenv查看已加载环境模板方法

        参数：
            无

        返回：
            无
        """

        veda_user = getpass.getuser()
        os.system("echo '#!/bin/bash' >> /home/{}/.veda/tmp/module_list.sh".format(veda_user))
        os.system("echo 'module list' >> /home/{}/.veda/tmp/module_list.sh".format(veda_user))
        os.system("bash /home/{}/.veda/tmp/module_list.sh".format(veda_user))
        os.system("rm -rf /home/{}/.veda/tmp/module_list.sh".format(veda_user))
        print("------------------------ Veda env list successful! --------------------")


    def vedaenv_load(self,**kwargs):
        """
        方法功能：

            定义一个vedaenv上传可用环境模板方法

        参数：
            load_path (str): modulefile文件路径
            password (str): 系统密码
            target_path (str): 目标路径

        返回：
            无
        """

        load_path = kwargs['load_path']
        password = kwargs['password']
        target_path = kwargs['target_path']
        os.system("echo '{}' | sudo -S cp {} {}".format(password,load_path,target_path))
        print("------------------------ Veda env load successful! --------------------")


    def vedaenv_ansible(self,**kwargs):
        """
        方法功能：
        
            定义一个ansible命令方法

        参数：
            group (str): 对象主机
            mode (str): 模式
            exec_script (str): 命令语句

        返回：
            无
        """

        group = kwargs['group']
        mode = kwargs['mode']
        exec_script = kwargs['exec_script']
        os.system("ansible {} -m {} -a '{}'".format(group,mode,exec_script))
        print("------------------------ Veda env load successful! --------------------")



#####################################################################################################
#####################################################################################################


