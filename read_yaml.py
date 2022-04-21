# 获取yaml文件
import yaml

file_list = open("./test.yaml","r",encoding="utf-8")
file_dict = open("./test1.yaml","r",encoding="utf-8")
value_list = yaml.load(stream= file_list, loader=yaml.FullLoader)
value_dict = yaml.load(stream= file_dict, loader=yaml.FullLoader)
print(value_list)
print(file_dict)