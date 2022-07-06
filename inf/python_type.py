#숫자형 데이터 타입
print('---' * 7)
print("숫자형 데이터 타입")
print()

#숫자형 연산
print("숫자형 연산")
print()
print('7 + 11 =', 7 + 11)
print('7 - 16 =', 7 - 11)
print('2 * 45 =', 2 * 45)
print('88 / 8 =', 88 / 8)
print('92 // 13 의 몫은?', 92 // 13)
print('92 % 13 의 나머지은?', 92 % 13)
print('-3의 절대값은?', abs(-3))
print()

#정수, 실수 선언
print("정수, 실수 선언")
print()
int_01 = 1
int_02 = 56
float_01 = 3.64
float_02 = 5.675

print(type(int_01), int_01)
print(type(int_02), int_02)
print(type(float_01), float_01)
print(type(float_02), float_02)
print()

#형 변환
print("형 변환")
print()
print(float(int_02))
print(int(float_01))
print()

#모듈 이용
print("모듈 이용")
print()

import math
from posixpath import split

print(math.pi)
print(math.ceil(6.34))
print()

#문자형 데이터 타입
print('---' * 7)
print("문자형 데이터 타입")
print()

print("문자형 선언")
print()

str_01 = 'Python'
str_02 = "Apple"
str_03 = ''
str_04 = str()

print(type(str_01), len(str_01), str_01)
print(type(str_02), len(str_02), str_02)
print(type(str_03), len(str_03), str_03)
print(type(str_04), len(str_04), str_04)
print()

#이스케이프 문자
print("이스케이프 문자")
print()

print('I\'m your joy')
print('I\'m your joy')
print('I\'m\tgood boy')
print('I\'m star\nvery good boy')
print()

#raw string
print("raw string")
print()

url1 = r'C://PYTHON_04'

print(url1)
print()

#멀티 라인 출력
print("멀티 라인 출력")

multi = \
"""
'apple'
'banana'
'carrot'
"""

print(multi)
print()

#문자형 연산
print("문자형 연산")

ex_01 = 'Water'
ex_02 = 'Paper'
ex_03 = 'A B C D'

print(ex_01 + ex_02)
print(ex_01 * 5)
print("A" in ex_03)
print("E" not in ex_03)
print()

#형 변환
print("형 변환")

num_t = '66'

print(type(num_t), num_t)
print(type(int(num_t)), num_t)
print()

#문자형 함수
print("문자형 함수")

text_01 = 'google'
text_02 = 'naver'
text_03 = 'zum, chrome, telegram'
text_04 = '23 45 67 7'

print(text_01.capitalize())
print(text_01.endswith('r'))
print(text_03.replace('zum', 'kakao'))
print(sorted(text_04))
print(text_04.split(" "))
print(sorted(text_04.split(" ")))
print()

#문자열 반복문
print("문자열 반복문")

for i in text_03:
    print(i)

print()

#슬라이싱
print("슬라이싱")

s1 = 'cream'
s2 = 'toner'
s3 = 'maskpack'
s4 = 'hellopython'

print(s1[0:3])
print(s1[2:6])
print(s3[4:len(s3)])
print(s3[:len(s3)-1])
print(s4[3:-5])
print()

#아스키 코드
print("아스키 코드")

a = 'j'

print(ord(a))
print(chr(85))





