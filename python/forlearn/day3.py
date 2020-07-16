"""

容器：可包含其它对象的对象；主要的容器有：序列（列表、元组）、映射（字典）、集合（set）
序列：列表、元组、字符串
序列可包含序列
元组无法修改
列表：所有元素都在方括号内，用 , 隔开：
['hello', 21, 'nerd']
-------------------------
集合：内无重复元素，元素在花括号内，元素排列无序

"""

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

## 序列相乘
print(alist * 3) # ['allen', 3, 'allen', 3, 'allen', 3]
sequence = [None] * 10
print(sequence)

## 成员资格检查
print(1 in numbers, '1' in numbers) # TRUE False
print(max(numbers), len(numbers), min(numbers))

aset = {'foo', 'bar'}
print(aset)

atuple = (1,2,3,'hello')
print(atuple)

## 列表
ablist = list('connan')
print(ablist)

stra = ''.join(ablist) ## 列表转字符串
print(stra)

## 列表可修改
newnum = [1,2,3]
newnum[0] = 2
print(newnum)

## 列表删除
names = ['Alice', 'Beth', 'Cecil', 'Dee-Dee']
del names[0]
print(names)

## 切片赋值
hipython = list('Perl')
hipython[1:] = list('ython')
print(hipython) # python

xnum = [1,5]
xnum[1:1] = [2,3,4]
print(xnum) # 1,2,3,4,5

xnum[1:4] = []
print(xnum) # 1,5

## 列表方法

lst = [1,2]
lst.append(3)
print(lst)

lst.clear()
print(lst) # []

## = ，只是将另一个名字关联到列表，a = b， b修改后，a也修改
abadname = list('bad')
bbadname = abadname
print(bbadname)

bbadname[0] = 'a'
print(abadname)

## copy
a = [1,2,3]
b = a.copy()
b[0] = 0
print(a, b)

## count
says = ['to', 'be', 'to']
print(says.count('to'))

## extend , 使用一个列表来扩展另一个列表
exa = [1,2]
exb = [3,4,5]
exa.extend(exb)
print(exa)

## index， 在列表中查找指定值第一次出现的索引
knights = ['we', 'are', 'the', 'we']
print(knights.index('we'))

## insert
nums = [1,2,3,4]
nums.insert(2, "hello!")
print(nums)

## pop
x = [1,2,3]
print(x.pop())
print(x)
print(x.pop(0), x)

## remove 删除指定值的第一个元素
y = [1,2,3,1]
y.remove(1)
print(y)

## reverse
z = [1,2,3]
z.reverse()
print(z)

## sort
gama = [1,3,4,2,98,7]
gama.sort()
print(gama)
