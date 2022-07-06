#리스트형 데이터 타입
from os import remove


print('---' * 7)
print("리스트형 데이터 타입")
print()

li_01 = ['python']
li_02 = list()
li_03 = [1, 3, 5, 7, 9]
li_04 = [2, 4, 6, 'two', 'four', 'six']
li_05 = [11, 13, 15, ['A', 'B', 'C']]
li_06 = [56, True, 3.14, 'text']
print()

print("인덱싱")
print()
print(li_03[3] + li_03[4])
print((list(li_04[3])))
print()

print("슬라이싱")
print()

print(li_04[2:5])
print(li_04[2:-2])
print(li_05[-1][0:2])
print()

print("리스트 연산")
print()
print(li_01 * 3)
print(li_03 + li_04)
print(str(li_04[0]) + li_04[3])
print()

print("값 비교와 id")
print()
print('값 비교')
x = [3, 5, 6, 7, 9]
temp = x
print(x == x[0:3] + x[-2:])
print()
print('id')
print(id(temp))
print(id(x))
print()

print("리스트 수정")
print()

list_01 = ['zero', 'one', 'two']

list_01[1:2] = ['three']
print(list_01)
list_01[2] = ['four']
print(list_01)
print()

print("리스트 삭제")
print()

list_02 = ['tvn', 'sbs', 'kbs', 'jtbc']

list_02[1:2] = []
print(list_02)

del list_02[1]
print(list_02)

list_02.remove('tvn')
print(list_02)
print()

print("리스트 함수")
print()
list_02.append('mbc')
print(list_02)

list_02.extend(['ebs'])
print(list_02)

list_02.sort()
print(list_02)

list_02.reverse()
print(list_02)

print(list_02.index('ebs'))

list_02.insert(1, 'mbn')
print(list_02)

print(list_02.count('mbn'))
print()

print("pop 이용")
print()

print(list_02.pop())
print(list_02)
print(list_02.pop())
print(list_02)


while list_02:
    test = list_02.pop()
    print(test)


print('---' * 7)
print("튜플형 데이터 타입")
print()

tu_01 = (1, 3, 5)
tu_02 = (4,)
tu_03 = (2, 4, 6, ('a', 'b', 'c'))

print(tu_01, type(tu_01))
print(tu_02, type(tu_02))
print(tu_03, type(tu_03))
print()

print("인덱싱")
print()
print(tu_03[-1])
print(tu_01[2])
print(tu_03[-1][1])
print()

print("슬라이싱")
print()

print(tu_03[-1][0:3])
print(tu_01[1:2])
print(tu_01[1])
print()

print("튜플 연산")
print()
print(tu_01 + tu_02)
print(tu_02 * 3)
print()

print("튜플 함수")
print()
print(tu_01.index(3))

print(tu_01.count(2))
print(tu_01.count(3))
print()

print("팩킹&언팩킹")
print()

t1 = ('one', 'two', 'three')
t2 = (3,)
x1, x2, x3 = t1
x4, x5, x6 = 4, 5, 6

print('팩킹')
print(x1, x2, x3)
print(x4, x5, x6)
print()
print('언팩킹')
print(t1)
print(t2) 
