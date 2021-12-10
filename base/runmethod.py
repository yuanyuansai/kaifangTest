import requests

class RunMethod:

    def send_get(self,url,cookies=None,headers=None):

        res = requests.get(url,cookies=cookies,headers=headers,verify=False)
        return res

    def send_post(self,url,data=None,cookies=None,headers=None):

        res = requests.post(url,data=data,cookies=cookies,headers=headers,verify=False)
        return res

    def run_main(self,url,method,data=None,cookies=None,headers=None):

        requests.packages.urllib3.disable_warnings()
        res = None


        if method == 'GET':
            res = self.send_get(url,cookies,headers)
        else:
            res = self.send_post(url,data=data,cookies=cookies,headers=headers)

        #响应的捕捉异常
        res1=None
        try:
            res1=res.json()
        except Exception as e:
            print("这是异常")
            print(e)
            print("这是异常")

        return res1
if __name__ == '__main__':
    url = "https://newapi-test.1911edu.com/api/auth/login_by_password"
    cookies = None
    headers = {
        "device-model": "1",
        "client-type": "1",
        "content-type": "application/x-www-form-urlencoded"
    }
    method = "POST"

    import json
    r = requests.post(url, data='account=15117961941&password=2569D419BFEA999FF13FD1F7F4498B89&role_type=1', cookies=cookies, headers=headers, verify=False).json()
    print(r)
    print(r['data']['token'])

