import pytest

def setup_module():
    print("==========开始----》这是个setup_module方法")

def teardown_module():
    print("==========末尾----》这是个teardown_module方法")

def setup_function():
    print("==========》这是个setup_funciton方法")

def teardown_function():
    print("==========》这是个teardown_funciton方法")

    print("============================分割线==============================")

def test_a():
    print("test_a执行的用例，在类的外面也可以执行")

class TestDemo1():

    def test_one(self):
        print("开始执行test_one方法")
        x = 'this'
        assert 'h' in x
        # pytest.assume('x' not in x)
        # pytest.assume(1 == 2)
        # pytest.assume('h' in x)

    def test_two(self):
        print("开始执行test_two方法")
        x = 'hello'
        assert 'e' in x

    def test_three(self):
        print("开始执行test_three方法")
        a = 'hello'
        b = 'hello world'
        assert a in b


if __name__ == '__main__':
    # pytest.main("-v -x TestDemo")
    # 上下两种写法一样，下面是以列表的形式放进去的
    # pytest.main(['-v','-x','TestDemo'])
#     默认执行整个用例，不加参数也可以
    pytest.main()  #类的外面也可以进行执行用例

# class TestDemo2():
#
# 	def test_a(self):
# 		print("开始执行test_a方法")
# 		x = 'this'
# 		assert 'h' in x
#
#
# 	def test_b(self):
# 		print("开始执行test_b方法")
# 		x = 'hello'
# 		assert 'e' in x
#
# 	def test_c(self):
# 		print("开始执行test_c方法")
# 		a = 'hello'
# 		b = 'hello world'
# 		assert a not in b
