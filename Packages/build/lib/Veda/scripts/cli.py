# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个veda常用命令行接口类
"""
模块介绍
-------

这是一个veda常用命令行接口类

设计模式：

    无

关键点：    

    （1）click 

主要功能：            

    （1）vedapkg

    （2）vedainfo

    （3）vedacontroller

    （4）vedaenv                                                     

使用示例
-------


类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



import click
from Veda.manage.commandmode import *
from Veda.manage.vedapkg import *
from Veda.manage.vedainfo import *
from Veda.manage.vedacontroller import *
from Veda.manage.vedaenv import *
from clickhouse_driver import Client


####### CLI命令行接口 #######################################################
### 设计模式：                                                            ###
###     无                                                               ###
### 关键点：                                                              ###
### （1）click                                                           ###
### 主要功能：                                                            ###
### （1）vedapkg                                                          ###
### （2）vedainfo                                                         ###
### （3）vedacontroller                                                   ###
### （4）vedaenv                                                          ###
############################################################################



###### CLI命令行接口 #####################################################################
#########################################################################################



@click.group()
def veda():
    print("hello veda")



### 实际命令角色创建 ############################################################
role_vedapkg = VedapkgRole('Vedapkg')
role_vedainfo = VedainfoRole('Vedainfo')
role_vedacontroller = VedacontrollerRole('Vedacontroller')
role_vedaenv = VedaenvRole('Vedaenv')



### Veda调度器创建 #############################################################
invoker_veda = VedaInvoker()



### vedapkg创建工作空间
print("##### 2 ######")
@click.command()
@click.option("--vedapkg_name", help="vedapkg name")
def vedapkgcreateworkspace(vedapkg_name):
    invoker_veda.set_command(VedaCommandVedapkgCreateWorkspace(role_vedapkg)).action(
        vedapkg_name = vedapkg_name)



### vedapkg向工作空间添加组件
print("##### 3 ######")
@click.command()
@click.option("--vedapkg_name", help="vedapkg name")
@click.option("--vedapkg_component_type", help="vedapkg component type")
@click.option("--vedapkg_component_path", help="vedapkg component path")
def vedapkgaddcomponent(vedapkg_name,vedapkg_component_type,vedapkg_component_path):
    invoker_veda.set_command(VedaCommandVedapkgAddComponent(role_vedapkg)).action(
        vedapkg_name = vedapkg_name,
        vedapkg_component_type = vedapkg_component_type,
        vedapkg_component_path = vedapkg_component_path)



### vedapkg打包工作空间
print("##### 4 ######")
@click.command()
@click.option("--vedapkg_name", help="vedapkg name")
def vedapkgpack(vedapkg_name):
    invoker_veda.set_command(VedaCommandVedapkgPack(role_vedapkg)).action(
        vedapkg_name = vedapkg_name)



### vedainfo本地初始化 
print("##### 5 ######")
@click.command()
def vedapkginfoinit():
    invoker_veda.set_command(VedaCommandVedainfoInit(role_vedainfo)).action()



### vedainfo注册信息 不能重复注册
print("##### 6 ######")
@click.command()
@click.option("--name", help="name")
@click.option("--version", help="version")
@click.option("--author", help="author")
@click.option("--summary",help="summary")
@click.option("--state",help="state")
@click.option("--requires",help='requires')
def vedapkginforegister(name,version,author,summary,state,requires):
    invoker_veda.set_command(VedaCommandVedainfoRegister(role_vedainfo)).action(
        name = name,
        version = version,
        author = author,
        summary = summary,
        state = state,
        requires = requires
    )



### vedainfo更新信息
print("##### 7 ######")
@click.command()
@click.option("--name", help="name")
@click.option("--info_key", help="info key")
@click.option("--info_value", help="info value")
def vedapkginfoupdate(name,info_key,info_value):
    invoker_veda.set_command(VedaCommandVedainfoUpdate(role_vedainfo)).action(
        name = name,
        info_key = info_key,
        info_value = info_value
    )



### vedainfo查询信息
print("##### 8 ######")
@click.command()
@click.option("--name", help="name")
def vedapkginfoquery(name):
    vedapkg_info = invoker_veda.set_command(VedaCommandVedainfoQuery(role_vedainfo)).action(
        name = name
    )
    print(vedapkg_info)



### vedainfo远端注册信息 可重复注册
print("##### 9 ######")
@click.command()
@click.option("--name", help="name")
@click.option("--version", help="version")
@click.option("--author", help="author")
@click.option("--summary",help="summary")
@click.option("--state",help="state")
@click.option("--requires",help='requires')
@click.option("--host", help="host")
@click.option("--port",help="port")
@click.option("--clickhouse_user",help="clickhouse_user")
@click.option("--clickhouse_password",help='clickhouse_password')
def vedainforegisterremote(name,version,author,summary,state,requires,host,port,clickhouse_user,clickhouse_password):
    invoker_veda.set_command(VedaCommandVedainfoRegisterRemote(role_vedainfo)).action(
        name = name,
        version = version,
        author = author,
        summary = summary,
        state = state,
        requires = requires,
        host = host,
        port = port,
        clickhouse_user = clickhouse_user,
        clickhouse_password = clickhouse_password
    )



### vedainfo远端查询信息
print("##### 10 ######")
@click.command()
@click.option("--name", help="name")
@click.option("--host", help="host")
@click.option("--port",help="port")
@click.option("--clickhouse_user",help="clickhouse user")
@click.option("--clickhouse_password",help='clickhouse password')
def vedainfoqueryremote(name,host,port,clickhouse_user,clickhouse_password):
    vedapkg_info_remote = invoker_veda.set_command(VedaCommandVedainfoQueryRemote(role_vedainfo)).action(
        name = name,
        host = host,
        port = port,
        clickhouse_user = clickhouse_user,
        clickhouse_password = clickhouse_password
    )
    print(vedapkg_info_remote)



### vedainfo远端更新信息
print("##### 11 #####")
@click.command()
@click.option("--name", help="name")
@click.option("--host", help="host")
@click.option("--port",help="port")
@click.option("--clickhouse_user",help="clickhouse user")
@click.option("--clickhouse_password",help='clickhouse password')
@click.option("--info_key", help="info key")
@click.option("--info_value", help="info value")
def vedainfoupdateremote(name,host,port,clickhouse_user,clickhouse_password,info_key,info_value):
    invoker_veda.set_command(VedaCommandVedainfoUpdateRemote(role_vedainfo)).action(    
        name = name,
        host = host,
        port = port,
        clickhouse_user = clickhouse_user,
        clickhouse_password = clickhouse_password,
        info_key = info_key,
        info_value = info_value    
    )



### vedacontroller从远端算法库拉取算法包
print("##### 12 #####")
@click.command()
@click.option("--connect_info", help="connect_info")
@click.option("--access_key", help="access_key")
@click.option("--secret_key",help="secret_key")
@click.option("--secure",help="secure")
@click.option("--object_file",help='object_file')
@click.option("--bucket", help="bucket")
def vedacontrollerpullremote(connect_info,access_key,secret_key,secure,object_file,bucket):
    invoker_veda.set_command(VedaCommandVedacontrollerPullRemote(role_vedacontroller)).action(
        connect_info = connect_info,
        access_key = access_key,
        secret_key = secret_key,
        secure = False,
        object_file = object_file,
        bucket = bucket
    )



### vedacontroller推送算法包到远端算法库    
print("##### 13 #####")
@click.command()
@click.option("--connect_info", help="connect_info")
@click.option("--access_key", help="access_key")
@click.option("--secret_key",help="secret_key")
@click.option("--secure",help="secure")
@click.option("--object_file",help='object_file')
@click.option("--bucket", help="bucket")
def vedacontrollerpushremote(connect_info,access_key,secret_key,secure,object_file,bucket):
    invoker_veda.set_command(VedaCommandVedacontrollerPushRemote(role_vedacontroller)).action(
        connect_info = connect_info,
        access_key = access_key,
        secret_key = secret_key,
        secure = False,
        object_file = object_file,
        bucket = bucket
    )



### vedaenv列出可用的module    
print("##### 14 ######")
@click.command()
@click.option("--avail_para", help="avail")
def vedaenvavail(avail_para):
    invoker_veda.set_command(VedaCommandVedaenvAvail(role_vedaenv)).action(
        avail_para = avail_para
    )



### vedaenv列出已加载的module
print("##### 15 ######")
@click.command()
def vedaenvlist():
    invoker_veda.set_command(VedaCommandVedaenvList(role_vedaenv)).action()



### vedaenv加载module
print("##### 16 ######")
@click.command()
@click.option("--load_path", help="load path")
@click.option("--password", help="password")
@click.option("--target_path", help="target_path")
def vedaenvload(load_path,password,target_path):
    invoker_veda.set_command(VedaCommandVedaenvLoad(role_vedaenv)).action(
        load_path = load_path,
        password = password,
        target_path = target_path
    )



### vedaenv运行ansible命令
print("##### 17 ######")
@click.command()
@click.option("--group", help="group")
@click.option("--mode", help="mode")
@click.option("--exec_script", help="exec_script")
def vedaenvansible(group,mode,exec_script):
    invoker_veda.set_command(VedaCommandVedaenvAnsible(role_vedaenv)).action(
        group = group,
        mode = mode,
        exec_script = exec_script
    )




### 向veda命令组添加命令

### 2
veda.add_command(vedapkgcreateworkspace)
### 3
veda.add_command(vedapkgaddcomponent)
### 4
veda.add_command(vedapkgpack)
### 5
veda.add_command(vedapkginfoinit)
### 6
veda.add_command(vedapkginforegister)
### 7 
veda.add_command(vedapkginfoupdate)
### 8
veda.add_command(vedapkginfoquery)
### 9
veda.add_command(vedainforegisterremote)
### 10
veda.add_command(vedainfoqueryremote)
### 11 
veda.add_command(vedainfoupdateremote)
### 12
veda.add_command(vedacontrollerpullremote)
### 13
veda.add_command(vedacontrollerpushremote)
### 14
veda.add_command(vedaenvavail)
### 15
veda.add_command(vedaenvlist)
### 16
veda.add_command(vedaenvload)
### 17
veda.add_command(vedaenvansible)



### 测试shell
###2  python ./Demo/cli.py vedapkgcreateworkspace --vedapkg_name 'test_vedapkg_1'
###   vedactl vedapkgcreateworkspace --vedapkg_name 'test_vedapkg_1'
###3  python ./Demo/cli.py vedapkgaddcomponent --vedapkg_name 'test_vedapkg_1' --vedapkg_component_type 'Data' --vedapkg_component_path '/home/shihua/tulip/AEwork/Veda/Demo/test_veda.py'
###   vedactl vedapkgaddcomponent --vedapkg_name 'test_vedapkg_1' --vedapkg_component_type 'Data' --vedapkg_component_path '/home/shihua/tulip/AEwork/Veda/Demo/test_veda.py'
###4  python ./Demo/cli.py vedapkgpack --vedapkg_name 'test_vedapkg_1'
###   vedactl vedapkgpack --vedapkg_name 'test_vedapkg_1'
###5  python ./Demo/cli.py vedapkginfoinit
###   vedactl vedapkginfoinit
###6  python ./Demo/cli.py vedapkginforegister --name 'test_vedapkg_2' --version 'beta-0.1' --author 'shihua' --summary 'This is a test package' --state 'Test' --requires 'TestPKG'
###   vedactl vedapkginforegister --name 'test_vedapkg_2' --version 'beta-0.1' --author 'shihua' --summary 'This is a test package' --state 'Test' --requires 'TestPKG'
###7  python ./Demo/cli.py vedapkginfoupdate --name 'test_vedapkg_2' --info_key 'version' --info_value 'beta-0.2'
###   vedactl vedapkginfoupdate --name 'test_vedapkg_2' --info_key 'version' --info_value 'beta-0.2'
###8  python ./Demo/cli.py vedapkginfoquery --name 'test_vedapkg_1'
###   vedactl vedapkginfoquery --name 'test_vedapkg_1'
###9  python ./Demo/cli.py vedainforegisterremote --name 'test_vedapkg_2' --version 'beta-0.1' --author 'shihua' --summary 'This is a test package!' --state 'Test' --requires 'TestPKG' --host '10.2.12.248' --port '9000' --clickhouse_user 'admin' --clickhouse_password 'admin'
###   vedactl vedainforegisterremote --name 'test_vedapkg_2' --version 'beta-0.1' --author 'shihua' --summary 'This is a test package!' --state 'Test' --requires 'TestPKG' --host '10.2.12.248' --port '9000' --clickhouse_user 'admin' --clickhouse_password 'admin'
###10 python ./Demo/cli.py vedainfoqueryremote --name 'test_vedapkg_2' --host '10.2.12.248' --port '9000' --clickhouse_user 'admin' --clickhouse_password 'admin'
###   vedactl vedainfoqueryremote --name 'test_vedapkg_2' --host '10.2.12.248' --port '9000' --clickhouse_user 'admin' --clickhouse_password 'admin'
###11 python ./Demo/cli.py vedainfoupdateremote --name 'test_vedapkg_2' --host '10.2.12.248' --port '9000' --clickhouse_user 'admin' --clickhouse_password 'admin' --info_key 'author' --info_value 'shihua_test'
###   vedactl vedainfoupdateremote --name 'test_vedapkg_2' --host '10.2.12.248' --port '9000' --clickhouse_user 'admin' --clickhouse_password 'admin' --info_key 'author' --info_value 'shihua_test'
###12 python ./Demo/cli.py vedacontrollerpullremote --connect_info '10.2.12.248:9111' --access_key 'minioadmin' --secret_key 'minioadmin' --secure False --object_file 'test_local.vedapkg' --bucket 'vedapkg_remote'
###   vedactl vedacontrollerpullremote --connect_info '10.2.12.248:9111' --access_key 'minioadmin' --secret_key 'minioadmin' --secure False --object_file 'test_local.vedapkg' --bucket 'vedapkg_remote'
###13 python ./Demo/cli.py vedacontrollerpushremote --connect_info '10.2.12.248:9111' --access_key 'minioadmin' --secret_key 'minioadmin' --secure False --object_file 'test_local.vedapkg' --bucket 'vedapkg_remote'
###   vedactl vedacontrollerpushremote --connect_info '10.2.12.248:9111' --access_key 'minioadmin' --secret_key 'minioadmin' --secure False --object_file 'test_local.vedapkg' --bucket 'vedapkg_remote'
###14 python ./Demo/cli.py vedaenvavail --avail_para 'test'
###   vedactl vedaenvavail --avail_para 'test'
###15 python ./Demo/cli.py vedaenvlist
###   vedactl vedaenvlist
###16 python ./Demo/cli.py vedaenvload --load_path '/home/shihua/tulip/test/veda/5.2.1' --password 'ATTACK7121553rb1' --target_path '/usr/share/modules/modulefiles/test/5.2.1'
###   vedactl vedaenvload --load_path '/home/shihua/tulip/test/veda/5.2.1' --password 'ATTACK7121553rb1' --target_path '/usr/share/modules/modulefiles/test/5.2.1'
###17 python ./Demo/cli.py vedaenvansible --group 'shihua002' --mode 'shell' --exec_script 'pwd'
###   vedactl vedaenvansible --group 'shihua002' --mode 'shell' --exec_script 'pwd'



if __name__ == '__main__':
    veda()



#####################################################################################################################################################################################
#####################################################################################################################################################################################