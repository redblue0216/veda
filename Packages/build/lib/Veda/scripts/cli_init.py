# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个veda初始化命令行接口类
"""
模块介绍
-------

这是一个veda初始化命令行接口类

设计模式：

    无

关键点：    

    （1）click 

主要功能：            

    （1）vedadata                                                    

使用示例
-------


类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



import click
from Veda.manage.commandmode import *
from Veda.manage.vedadata import *


####### CLIINIT命令行接口 ###################################################
### 设计模式：                                                            ###
###     无                                                               ###
### 关键点：                                                              ###
### （1）click                                                           ###
### 主要功能：                                                            ###
### （1）vedadata                                                         ###
############################################################################



###### CLIINIT命令行接口 #####################################################################
#############################################################################################



@click.group()
def vedainit():
    print("hello veda")



### 实际命令角色创建 ############################################################
role_vedadata = VedadataRole('InitVedaLocal')



### Veda调度器创建 #############################################################
invoker_veda = VedaInvoker()



### Veda本地初始化
print("##### 1 ######")
@click.command()
@click.option("--veda_workspace", help="veda workspace")
def vedadata(veda_workspace):
    invoker_veda.set_command(VedaCommandVedaLocalInit(role_vedadata)).action(
        veda_workspace = veda_workspace)



### 向veda命令组添加命令
### 1
vedainit.add_command(vedadata)


### 测试shell
### python ./Demo/cli_init.py vedadata --veda_workspace '/home/shihua/tulip/AEwork/Veda/TEST'
### vedainit vedadata --veda_workspace '/home/shihua/tulip/AEwork/Veda/TEST'



if __name__ == '__main__':
    vedainit()



####################################################################################################################
####################################################################################################################


