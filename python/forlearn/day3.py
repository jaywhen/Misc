## 容器：可包含其它对象的对象；主要的容器有：序列（列表、元组）、映射（字典）、集合（set）
## 序列：列表、元组、字符串
## 序列可包含序列
## 元组无法修改
## 列表：所有元素都在方括号内，用 , 隔开：
## ['hello', 21, 'nerd']
## -------------------------
## 集合：内无重复元素，元素在花括号内，元素排列无序

alist = ['allen', 3]
anlist = ['jordan', 23]
nba_star = [alist, anlist]
print(nba_star)

## 通用的序列操作: index
print(alist[0][0], "|", alist[-1])

## 切片: numbers[第一个元素的索引，最后一个元素的索引+1, 步长（可省略，省略为1）]
## 即，第一个索引在切片内，第二个索引不在切片内
numbers = [1,2,3,4,5,6]
print(numbers[0:3], numbers[3:-1])
print(numbers[:], numbers[-3:], numbers[:3])

## 切片的步长，步长如果为负数，则代表从右往左数
print(numbers[0:4:2]) # 1,3
print(numbers[::2],numbers[::-1])

## 序列相加
print("alist+numbers is: ", alist+numbers)


aset = {'foo', 'bar'}
print(aset)

atuple = (1,2,3,'hello')
print(atuple)

