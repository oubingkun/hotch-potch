# encoding: utf-8
import allure
import pytest
import requests
from utils.read_files import *

test_data = get_xls()

@allure.feature('postman')
@allure.story('postman-api')
@pytest.mark.parametrize('timestamp,target,expected',test_data)
def test_timestamp(timestamp,target,expected,env):
    """
    用例描述：测试不同的timestamp和target
    """
    #从yml配置文件获取url
    url = env_config['host']['url']
    payload = {'timestamp':timestamp,'target':target}
    r = requests.get(url,params=payload)
    print(r.url)
    result = r.json()
    assert str(result['before'])==expected
