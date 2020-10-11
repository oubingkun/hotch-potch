#coding=utf-8
import pytest
import allure
import yaml
import os

@pytest.fixture(scope="session",autouse=True)
def env_config(request):
    """
    读取yaml文件
    :param request:
    :return:
    """
    project_name = 'Interface_Test'
    rootPath  = get_root_path(project_name)
    config_path = os.path.abspath(rootPath + 'config\\env.yml') #路径
    with open(config_path) as f:
        env_config = yaml.load(f)   #读取config配置文件路径
    return env_config

def get_root_path(project_name):
    current_path = os.path.abspath(os.path.dirname(_file_))
    rootPath = current_path[:current_path.find(project_name + "\\") + len(project_name + "\\")]
    return rootPath