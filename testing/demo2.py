
# all里面引入的东西先去找all里面的，其他的变量等不对外暴露，只暴露all里面引入的
__all__=['hello']
hello="我是被demo调用的demo2里面的hello，需要在demo里面demo2.上这个被定义的hello"
def f():
    print("demo2.py  f()被demo调用")
class Demo2:
    pass