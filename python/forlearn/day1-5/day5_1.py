print('hello, world!')
# print("你好,世界！")
print('你好', '世界')
print('hello', 'world', sep=', ', end='!\n')
print('goodbye, world', end='!\n')
print('another goodbye\n')

x = int(input('Please input a number: '))
if x > 1:
    y = 100
elif x < 1:
    y = 200
else:
    y = 10000
print('y is: ', y)

print(type(x))  # <class 'int'>
