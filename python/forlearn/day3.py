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

aset = {'foo', 'bar'}
print(aset)

atuple = (1,2,3,'hello')
print(atuple)
