'''
unittest测试框架应用
1.类名继承unitest.TestCase
2.测试用例：所有测试用例，都是以函数的形式存在，函数的名称必须以test开头
3.用例加载顺序：UnitTest中有默认的用例加载顺序：0-9，A-Z，a-z（函数名）
4.所有的前置后置都有等级存在：class级别，methond级别，前置后置有且仅有一个
  method级别前置后置：
      与用例关联，每一条用例运行前都会执行前置，运行后会执行后置
  class级别前置后置：
      1）必须定义装饰器@classmethod

'''
import unittest


# 如何真正意义上应用UnitTest框架：必须在类名继承unitest.TestCase
class UnitDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("class 前置条件")

    @classmethod
    def tearDownClass(cls) -> None:
        print("class 后置条件")

    # 前置条件：method级别[函数名固定]
    def setUp(self) -> None:
        print("前置条件")

    # 后置条件：method级别【函数名固定】
    def tearDown(self) -> None:
        print("后置条件")

    # 测试用例：所有测试用例，都是以函数的形式存在，函数的名称必须以test开头
    def test_01(self):
        print("这是测试1")

    def test_02(self):
        print("这是另一个测试")
        self.assertEqual("123","1234",msg = "断言失败")


# 要运行测试用例

if __name__ == '__main__':
    # UnitTest执行测试用例的行为
    unittest.main()
