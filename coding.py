#숫자형 데이터 타입
print('---' * 7)
print("숫자형 데이터 타입")

print('---int형---')
print(type(4), 4)
print(type(0), 0)
print(type(-4), -4)
print()

print('---float형---')
print(type(3.456), 3.456)
print(type(10/3), 10/3)
print()

print('---math 모듈---')

import math

print("제곱근", int(math.sqrt(4)))
print("제곱", int(math.pow(4,2)))
print()

print('---random 모듈---')

import random

print(random.random())
print()

#문자형 데이터 타입
print('---' * 7)
print("문자형 데이터 타입")

str1 = 'apple'
str2 = "banana"
str3 = '''carrot'''
str4 = """donut"""

print(type(str1), str1)
print(type(str2), str2)
print(type(str3), str3)
print(type(str4), str4)
print()

print('---문자형 연산---')
print("문자형 덧셈 :", str2 + str3)
print("문자형 곱셈 :", str2 * 3)
print("문자형 길이 :", str4, len(str4))
print()

print('---단어 변경---')

name = 'Won'

text = 'Hi,'+name.replace('Won', 'Sun')

print(text)
print()

#리스트형 데이터 타입
print('---' * 7)
print("리스트형 데이터 타입")

friend = [17, 34, 30, 26]

print('원소 갯수 :', len(friend))
print("가장 작은 값 :", min(friend))
print("가장 큰 값 :", max(friend))
print("합계 :", sum(friend))
print()

print('---통계 모듈---')

import statistics

print("평균값 :", statistics.mean(friend))
print(statistics.median_high(friend))
print(statistics.median_low(friend))
print()

print('---랜덤 모듈---')

import random

print("당신의 선택은? :",random.choice(friend))
print()

#변수, 입력과출력
print('---' * 7)
print("변수")

Age = '17'

message1 = 'how old are you? I\'m ' +Age+' years old'

print(message1)
print()
print("입력과출력")

Age_input = input('Your Age? :')

message2 = 'how old are you? I\'m ' +Age_input+' years old'

print(message2)
print()

#pandas 외부모듈
print('---' * 7)
print("pandas 모듈")

import pandas

read = pandas.read_csv('100BT.csv')

print(read)
print(read.head(2))
print(read.tail(2))



