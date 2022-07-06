#파이썬 함수

print('---' * 7)
print("파이썬 함수")
print()

#선언
def first_func1(w):
    print("Hello", w)

word = "Goodboy"

first_func1(word)

def first_func2(w):
    value = "Hello, " + str(w)
    return value

x = first_func2('Goodboy2')

print(x)
print()

print("다중 반환")
print()

def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3

a, b, c = func_mul(10)

print(a, b, c)
print()

def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1, y2, y3)

q = func_mul2(2)

print(q)
print(list(q))
print()

def func_mul3(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1, y2, y3]

q1 = func_mul3(5)

print(q1)
print(tuple(q1))
print()

print("*args, **kwargs")
print()
print('*args')

def args_func(*args):
    for i, v in enumerate(args):
        print("Result : {}".format(i), v)
    print('-----')

args_func('Lee')
args_func('Lee', 'won')

print('**kwargs')
def args_func1(**kwargs):
    for v in kwargs.keys():
        print('{}'.format(v), kwargs[v])
    print('-----')

args_func1(name = 'Lee')
args_func1(name = 'Lee', name2 = 'won')   
print()

print("전체 혼합")
print()

def ex(args_1, args_2, *args, **kwargs):
    print(args_1, args_2, args, kwargs)

ex(10, 20, 'Lee', 'Won', age1 = 20, age2 = 30, age3 = 40)
print()

print("중첩 함수")
print()

def nested_func(num):
    def func_in_func(num):
        print(num)
    print("In func")
    func_in_func(num + 100)

nested_func(100)
print()

print("람다식 함수")
def mul_func(x, y):
    return x * y

print(mul_func(50, 3))
print()

lambda_func = lambda x, y: x * y
print(lambda_func(50, 3))

def func_final(x, y, func):
    print(x * y * func(100, 50))

func_final(10, 20, lambda_func)




