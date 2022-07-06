#딕셔너리형 데이터 타입

print('---' * 7)
print("딕셔너리형 데이터 타입")
print()

dict_01 = {'name': 'won', 'phone': '01077775555', 'grade': 'A'}
dict_02 = {1 : 'one'}
dict_03 = {'phone': [1, 2, 3, 4]}
dict_04 = {
    'name':'won',
    'phone': '01077775555',
    'grade': 'A'}
dict_05 = dict(
    name ='won',
    phone = '01077775555',
    grade = 'A'
)

print(dict_01, type(dict_01))
print(dict_02, type(dict_02))
print(dict_03, type(dict_03))
print(dict_04, type(dict_04))
print(dict_05, type(dict_05))
print()

print("출력")
print()
print(dict_01['name'])
print(dict_01.get('name'))
print(dict_01.get('ok'))

print()

print("추가 및 수정")
print()
dict_02['age'] = 3
print(dict_02)

dict_01['name'] = 'sun'
print(dict_01)

dict_05.update(Age = '13')
print(dict_05)
print()

print("딕셔너리 함수")
print()
print(dict_04.keys())
print(dict_04.values())
print(dict_04.items())

print()

print("pop")
print()
print(dict_04.pop('name'))
print(dict_04)
print()

print("popitems")
print()
print(dict_05.popitem())
print(dict_05)
print(dict_05.popitem())
print(dict_05)

print()

print("in 연산자")
print()

print('phone' in dict_01)
print('name' not in dict_04)

#집합형 데이터 타입

print('---' * 7)
print("집합형 데이터 타입")
print()
set_01 = set()
set_02 = set([1, 2, 3, 4])
set_03 = set([2, 4, 'text', 'con'])
set_04 = {'foo', 'bar', 'qux'}

print(type(set_01), set_01)
print(type(set_02), set_02)
print(type(set_03), set_03)
print(type(set_04), set_04)
print()
print("형 변환")

print(list(set_03))
print(tuple(set_03))
print()

print("집합 자료형")
s1 = {1, 2, 3, 4, 5, 6}
s2 = {5, 6, 7, 8, 9}
s3 = {1, 2, 3}

print('교집합', s1 & s2)
print('교집합 함수', s1.intersection(s2))
print('합집합', s1 | s2)
print('합집합 함수', s1.union(s2))
print('차집합', s1 - s3)
print('차집합 함수', s1.difference(s3))
print()

print("부분 집합")

print(s3.issubset(s1))
print(s1.issuperset(s3))
print()

print("중복 원소")
print(s2.isdisjoint(s3))
print()

print("집합 추가&제거")

s1.add('test')
print(s1)
s1.add('9')
print(s1)

s2.remove(6)
print(s2)
s2.discard(13)
print(s2)



