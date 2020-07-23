class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age
    
    def play(self):
        print('%s 在愉快的玩耍。' % self._name)

    def watch_mv(self):
        if self._age >= 18:
            print('%s 可以看限制级的mv了' % self._name)
        else:
            print('%s 不能看限制级的mv' % self._name)

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade
    @property
    def grade(self):
        return self._grade
    
    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print('%s的%s正在学习%s.' % (self._grade, self._name, course))

class Teacher(Person):
    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title
    
    def teach(self, course):
        print('%s%s正在教授%s.' % (self._title, self._name, course))


def main():
    stu = Student('jaywhen', 20, '18级')
    stu.study('python')
    stu.watch_mv()

    t = Teacher('nobady', 100, '砖家')
    t.teach('Python')
    t.watch_mv()

if __name__ == '__main__':
    main()

    



