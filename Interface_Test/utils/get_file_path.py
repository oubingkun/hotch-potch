#coding=utf-8
"""
@author:oubingkun
@file:get_file_path.py
@time:2020-10
@desc:获取文件路径
"""
import os

project_name = "Interface_Test"

def get_root_path():
    """
    获取根路径
    :param Project_name
    :return:
    """
    currentPath = os.path.abspath(os.path.dirname(_file_))
    rootPath = currentPath[:currentPath.find(project_name+"\\") + len(project_name+"\\")]
    return rootPath

if __name__ == '__main__':
    print(get_root_path())