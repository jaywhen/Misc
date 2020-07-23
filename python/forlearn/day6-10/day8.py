## 数组、列表、元组、集合、字典
import os
import time
import sys

def main():
    content = '迪迦奥特曼变身! ...'
    while True:
        os.system('cls') # Windows
        print(content)
        time.sleep(0.5)
        content = content[1:] + content[0]
        print(content)

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
        yield a

def test():
    things = ['hi', 'bye', 'love', 'lone']
    bornth = ('head', 'body', 'handsome')
    print(things, bornth)

    print('\n')
    bornth_list = list(bornth)
    things_tuple = tuple(things)
    print(bornth_list, things_tuple)


if __name__ == '__main__':
    # a,b = 10, 5
    # print(f'{a} * {b} = {a * b}')
    list1 = ['one','two','three','four','five']
    for key, val in enumerate(list1):
        print(key, val)
    
    f = [x for x in range(1, 11)]
    print(f)

    f1 = [x+y for x in '1234' for y in 'ABCD']
    print(f1)

    f2 = [x**2 for x in range(1,101)]
    print(sys.getsizeof(f2))
    print(f2)

    print('\n')
    f3 = (x**2 for x in range(1,101))
    print(sys.getsizeof(f3))
    print(f3)
    for val in f3:
        print(val)

    print(os.system('cls'))
    for value in fib(20):
        print(value)
    
    test()



    # main()