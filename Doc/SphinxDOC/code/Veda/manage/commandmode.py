# -*- coding: utf-8 -*-
# author:shihua
# coder:shihua
# 这是一个命令模式类，是Veda算法库的主体框架
"""
模块介绍
-------

这是一个命令模式类，是Veda算法库的主体框架

设计模式：

    命令模式

关键点：    

    （1）命令模式 

主要功能：            

    （1）命令抽象                                                   

使用示例
-------


类说明
------

"""



####### 载入程序包 ##########################################################
############################################################################



from abc import ABCMeta,abstractmethod
from Veda.manage.vedapkg import *



####### veda命令模式框架 #####################################################
### 设计模式：                                                            ###
###     命令模式                                                          ###
### 关键点：                                                              ###
### （1）命令模式                                                         ###
### 主要功能：                                                            ###
### （1）命令抽象                                                         ###
############################################################################



###### 基础模块类 #####################################################################
######################################################################################



class VedaCommand(metaclass = ABCMeta):
    """
    类介绍：

        这是一个命令模式的抽象命令类，主要功能命令实例化与传递
    """


    def __init__(self,role):
        """
        属性功能：

            初始化属性
        
        参数：
            role (object): 角色对象
        """

        self._role = role


    def set_role(self,role):
        """
        方法功能：

            定义一个设置命令角色的方法

        参数：
            role (object): 角色对象

        返回：
            无
        """

        self._role = role 


    @abstractmethod
    def execute(self):
        """
        方法功能：

            定义一个执行命令的抽象方法
        """

        pass



class VedaInvoker(object):
    """
    类介绍：

        这是一个命令模式中调度器，主要功能为控制命令的执行
    """
    

    def __init__(self):
        """
        属性功能：

            初始化属性
        """

        self.__command = None


    def set_command(self,command):
        """
        方法功能：

            定义一个设置命令对象的方法

        参数：
            command (object): 命令对象

        返回：
            无
        """

        self.__command = command

        return self


    def action(self,**kwargs):
        """
        方法功能：

            定义一个执行命令对象的方法
        """

        result = None
        if self.__command is not None:
            result = self.__command.execute(**kwargs)

        return result



####### 具体命令对象 ###########################################################
###############################################################################



class VedaCommandVedaLocalInit(VedaCommand):
    """
    类介绍：

        这是一个veda本地初始化的命令对象
    """


    def execute(self,**kwargs):
        """
        方法功能：

            定义一个命令的具体实现方法
        """

        result_1 = None
        result_1 = self._role.create_veda_workspace(**kwargs)
        result_2 = None
        result_2 = self._role.create_config_file(veda_workspace = result_1)
        result_3 = None
        result_3 = self._role.create_sqlite3_db(veda_workspace = result_1)

        return result_3



class VedaCommandVedapkgCreateWorkspace(VedaCommand):
    """
    类介绍：

        这是一个vedapkg创建工作空间的命令对象
    """    


    def execute(self,**kwargs):
        """
        方法功能：

            定义一个命令的具体实现方法
        """
                
        result = None
        result = self._role.vedapkg_create_workspace(**kwargs)

        return result



class VedaCommandVedapkgAddComponent(VedaCommand):
    """
    类介绍：

        这是一个vedapkg添加组件的命令对象
    """


    def execute(self,**kwargs):
        """
        方法功能：

            定义一个命令的具体实现方法
        """
                
        result = None
        result = self._role.vedapkg_add_component(**kwargs)

        return result



class VedaCommandVedapkgPack(VedaCommand):
    """
    类介绍：

        这是一个vedapkg打包的命令对象
    """


    def execute(self,**kwargs):
        """
        方法功能：

            定义一个命令的具体实现方法
        """
                
        result = None
        result = self._role.vedapkg_pack(**kwargs)

        return result



class VedaCommandVedainfoInit(VedaCommand):
    """
    类介绍：

        这是一个vedainfo初始化的命令对象
    """


    def execute(self,**kwargs):
        """
        方法功能：

            定义一个命令的具体实现方法
        """
                
        result = None
        result = self._role.vedainfo_init(**kwargs)

        return result



class VedaCommandVedainfoRegister(VedaCommand):
    """
    类介绍：

        这是一个vedainfo注册的命令对象
    """


    def execute(self,**kwargs):
        """
        方法功能：

            定义一个命令的具体实现方法
        """
                
        result = None
        result = self._role.vedainfo_register(**kwargs)

        return result



class VedaCommandVedainfoUpdate(VedaCommand):
    """
    类介绍：

        这是一个vedainfo更新信息的命令对象
    """


    def execute(self,**kwargs):
        """
        方法功能：

            定义一个命令的具体实现方法
        """
                
        result = None
        result = self._role.vedainfo_update(**kwargs)

        return result



class VedaCommandVedainfoQuery(VedaCommand):
    """
    类介绍：

        这是一个vedainfo查询信息的命令对象
    """


    def execute(self,**kwargs):
        """
        方法功能：

            定义一个命令的具体实现方法
        """
                
        result = None
        result = self._role.vedainfo_query(**kwargs)

        return result



class VedaCommandVedainfoRegisterRemote(VedaCommand):
    """
    类介绍：

        这是一个vedainfo远端注册的命令对象
    """


    def execute(self,**kwargs):
        """
        方法功能：

            定义一个命令的具体实现方法
        """
                
        result = None
        result = self._role.vedainfo_register_remote(**kwargs)

        return result



class VedaCommandVedainfoQueryRemote(VedaCommand):
    """
    类介绍：

        这是一个vedainfo远端查询的命令对象
    """


    def execute(self,**kwargs):
        """
        方法功能：

            定义一个命令的具体实现方法
        """
                
        result = None
        result = self._role.vedainfo_query_remote(**kwargs)

        return result



class VedaCommandVedainfoUpdateRemote(VedaCommand):
    """
    类介绍：

        这是一个vedainfo远端更新的命令对象
    """


    def execute(self,**kwargs):
        """
        方法功能：

            定义一个命令的具体实现方法
        """
                
        result = None
        result = self._role.vedainfo_update_remote(**kwargs)

        return result



class VedaCommandVedacontrollerPullRemote(VedaCommand):
    """
    类介绍：

        这是一个vedacontroller远端拉取的命令对象
    """


    def execute(self,**kwargs):
        """
        方法功能：

            定义一个命令的具体实现方法
        """
                
        result = None
        result = self._role.vedacontroller_pull_remote(**kwargs)

        return result



class VedaCommandVedacontrollerPushRemote(VedaCommand):
    """
    类介绍：

        这是一个vedacontroller远端推送的命令对象
    """


    def execute(self,**kwargs):
        """
        方法功能：

            定义一个命令的具体实现方法
        """
                
        result = None
        result = self._role.vedacontroller_push_remote(**kwargs)

        return result



class VedaCommandVedaenvAvail(VedaCommand):
    """
    类介绍：

        这是一个vedaenv查询可用模板的命令对象
    """


    def execute(self,**kwargs):
        """
        方法功能：

            定义一个命令的具体实现方法
        """
                
        result = None
        result = self._role.vedaenv_avail(**kwargs)

        return result



class VedaCommandVedaenvList(VedaCommand):
    """
    类介绍：

        这是一个vedaenv查询已加载模板的命令对象
    """


    def execute(self,**kwargs):
        """
        方法功能：

            定义一个命令的具体实现方法
        """
                
        result = None
        result = self._role.vedaenv_list(**kwargs)

        return result



class VedaCommandVedaenvLoad(VedaCommand):
    """
    类介绍：

        这是一个vedaenv传送模板文件的命令对象
    """


    def execute(self,**kwargs):
        """
        方法功能：

            定义一个命令的具体实现方法
        """
                
        result = None
        result = self._role.vedaenv_load(**kwargs)

        return result



class VedaCommandVedaenvAnsible(VedaCommand):
    """
    类介绍：

        这是一个vedaenv运行ansible的命令对象
    """


    def execute(self,**kwargs):
        """
        方法功能：

            定义一个命令的具体实现方法
        """
                
        result = None
        result = self._role.vedaenv_ansible(**kwargs)

        return result
####################################################################################
####################################################################################


