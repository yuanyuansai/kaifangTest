import requests
import json
from util.operation_json import OperationJson

class OperationHeader:
    def __init__(self,response):
        self.response = json.loads(response)
    def get_response_url(self):
        '''
        获取登录返回的token的url
        :return:
        '''
        url = self.response['data']['url'][0]
        return url
    def get_cookie(self):
        '''
        获取cookie的jar文件
        :return:
        '''
        url = self.get_response_url()+"&callback=jQuery21008240514814031887_1508666806688&_=1508666806689"
        cookie = requests.get(url).cookies
        return cookie
    def write_cookie(self):
        cookie = requests.utils.dict_from_cookiejar(self.get_cookie())
        op_json = OperationJson()
        op_json.write_data(cookie)

if __name__ == '__main__':
    url = "https://api-dev.1911edu.com/AdultApi/v4_4/StudyCard/hasUnExchangeStudyCard"
    data = {
        "channel": "AppStore",
        "device_model": "iphone XS Max",
        "phone": "18231040441",
        "sms_code": ""
    }
    res = json.dumps(requests.get(url).json())
    op_header = OperationHeader(res)
    op_header.write_cookie()