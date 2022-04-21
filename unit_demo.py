'''
unittest测试框架应用
1.类名继承unitest.TestCase
2.测试用例：所有测试用例，都是以函数的形式存在，函数的名称必须以test开头
'''
import unittest

# 如何真正意义上应用UnitTest框架：必须在类名继承unitest.TestCase
class UnitDemo(unittest.TestCase):
    # 前置条件
    # 后置条件
    # 测试用例：所有测试用例，都是以函数的形式存在，函数的名称必须以test开头
    def test_01(self):
        print("这是测试1")

    def test_2(self):
        print("这是另一个测试")



# 要运行测试用例

if __name__ == '__main__':
    # UnitTest执行测试用例的行为
    unittest.main()
