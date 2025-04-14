import functools

def myde(func):
    @functools.wraps(func)#防止原函数的元信息被替换
    def mywr():
        """
        这是装饰器mywr
        """
        print("前置功能！")
        n=int(input("请输入参数n:"))
        func(n)
        print("后置功能！")
    return mywr


@myde
def hello(n:int)->str:
    """这是hello函数
    """
    if n==1:
        print("hello!")
    elif n==2:
        print("world!")
    else:
        print("hello world!")
    
    return "ok"


if __name__=="__main__":
    hello()
    print(f"hello 函数的元信息：\n函数名{hello.__name__}\t参数信息{hello.__annotations__}\t文档信息:{hello.__doc__}")
