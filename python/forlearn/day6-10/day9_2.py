class Person(object):
    __slots__ = ('_name', '_age', '_gender')

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
        if self.age <= 16:
            print('%s is playing ttm' %(self._name))
        else:
            print('%s is playing LOL' %(self._name))

def main():
    p1 = Person('jaywhen', 20)
    p1.play()
    p1._gender = 'male'
    
    # AttributeError: 'Person' object has no attribute '_ishandsome'
    # p1._ishandsome = True

if __name__ == '__main__':
    main()

