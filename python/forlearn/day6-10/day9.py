class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s is studying %s' %(self.name, course_name))
    

class Test:
    def __init__(self, foo):
        self.__foo = foo
    def __bar(self):
        print(self.__foo)
        print('__bar')



if __name__ == '__main__':
    st1 = Student('jaywhen', 20)
    st1.study('how to be more handsome')

    t1 = Test('hi')
    # t1._bar()

    # print(t1.__foo)
    # 虽然在属性名前加上__后会使属性变成私有
    # 不过依然可以访问
    t1._Test__bar()
    print(t1._Test__foo)

