def foo():
    print('hi')
    pass


def bar():
    pass    # 当你没有想好函数的内容是可以用 pass 填充，使程序可以正常运行

# foo()
# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
if __name__ == '__main__':
    print('call foo()')
    foo()
    print('call bar()')
    bar()
