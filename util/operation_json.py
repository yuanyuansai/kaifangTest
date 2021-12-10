#coding:utf-8
import json
class OperationJson:
    def __init__(self,file_path = None):
        if file_path == None:
            self.file_path = '../dataconfig/header'
        else:
            self.file_path = file_path
        self.data = self.read_file()


    #读文件内容
    def read_file(self):
        with open(self.file_path) as fp:
            data=fp.read()
            return data

    #读取json文件
    def read_data(self):
        with open(self.file_path) as fp:
            data = json.load(fp)
            return data

    #根据关键字获取数据
    def get_data(self,id):
        print(type(self.data))
        print(self.data[id])
        return self.data[id]

    #写json
    def write_data(self,data):
        with open('../dataconfig/cookies.json','w') as fp:
            fp.write(json.dumps(data))

if __name__ == '__main__':
    opjson = OperationJson()
    print(opjson.get_data())