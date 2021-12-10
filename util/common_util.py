#coding:utf-8
import json
import operator
class CommonUtil:
    def is_contain(self,str_one,str_two):
        '''
        判断一个字符串是否在另一个字符串中
        str_one:查找字符串
        str_two:被查找的字符串
        '''
        flag = None
        print(str_one)
        print(str_two)


        if isinstance(str_one,str):
            str_one = str_one.encode('unicode-escape').decode('string_escape')
        return operator.eq(str_one,str_two)
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag
    def is_equal_dict(self,dict_one,dict_two):
        '''
        判断两个字典是否相等
        '''
        print("dict_one",dict_one)
        print("dict_two",dict_two)
        print(type(dict_one))
        print(type(dict_two))
        if isinstance(dict_one,dict):
            dict_one = json.loads(dict_one)
        if isinstance(dict_two,dict):
            dict_two = json.loads(dict_two)
        return operator.eq(dict_one,dict_two)

