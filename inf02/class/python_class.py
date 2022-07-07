#파이썬 클래스

from distutils.log import info
import secrets


print('---' * 7)
print("파이썬 클래스")
print()

print("선언")
print()

class dog1:
    secies = 'firstdog'

    def __init__(self, name, age):
        self.name = name
        self.age = age

print(dog1)

a = dog1('star', 17)
b = dog1('goodboy', 100)

print(a.__dict__)
print(b.__dict__)

print("{} is {} years old".format(a.name, a.age))
print("{} is {} years old".format(b.name, b.age))
print()

if a.secies == 'firstdog':
    print('{} is {} years old'.format(dog1.secies, a.age))

print('---' * 7)
print("self 이해")
print()

class self:
    def func1():
        print("func1 called")
    def func2(self):
        print("func2 called")

f = self()

print(id(f))

f.func2()
self.func1()

print('---' * 7)
print("class 변수& 인스턴스 변수")
print()
class warehouse:
    stock_num = 0

    def __init__(self, name):
        self.name = name
        warehouse.stock_num += 1
    def __del__(self):
        warehouse.stock_num -= 1

w1 = warehouse('kim')
w2 = warehouse('won')

print(w1.name)
print(w2.name)
print(w1.__dict__)
print(w2.__dict__)
print(warehouse.__dict__)

print(warehouse.stock_num)
del w1
print(warehouse.stock_num)


print('---' * 7)
print("class 예제3")
print()

class dog2:
    secies = 'firstdog'

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        return '{} is {} years old'.format(self.name, self.age)

    def sound(self, sound):
        return '{} says {}'.format(self.name, sound)    


cu1 = dog2('star', 17)
cu2 = dog2('goodboy', 100)

print(cu1.info())
print(cu2.sound("wal! wal!"))
