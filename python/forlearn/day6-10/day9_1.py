class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # getter
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    # setter
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self.age <= 16:
            print('playing Talking Tom Cat')
        else:
            print('playing LOL')

if __name__ == '__main__':
    p1 = Person('jaywhen', 20)
    p1.play()

    p1.age = 12
    p1.play()

    # p1.name = 'shell'  # AttributeError: can't set attribute
