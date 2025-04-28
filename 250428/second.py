## 입력 구현
# a = input("아무거나 입력해주세요.") # 파이썬에서 input은 숫자입력해도, 무조건 "문자"이다
# s = a
# str1 = a

## 입력을 몇가지 변수에 담아서 1
# f-string, 문자 붙이기, 문자반복하기 등 여러 기술을 활용해 출력하세요.


# print(f"{a}는 오늘 점심을 먹었다")
# print(str1 * 3)
# print(a,s[0:3])

## 형변환
# print(type(a))
# b = int(a) # 문자를 숫자로
# print(type(b))

# a = 1 

# print(type(str(a)))


## 문자열 고유 기능
# s = 'weniv CEO licat'
# print(s.lower()) #소문자 변환
# print(s.upper()) #대문자 변환

## find: 없으면 -1
## index: 없으면 Error

# s = 'weniv CEO licat'
# print(s.find("weniv"))
# print(s.find("licat"))

# print(s.index("weniv"))
# print(s.index("licat"))

# print(s.count("i"))

# s2 = s.replace("CEO","CTO")
# print(s2)

# s3 = "weniv-corp"

# s4,s5 = s3.split("-") # split ~기준으로 쪼개기
# print(s4,s5)

'''
입력이 들어온다. 키 몸무게 성별 나이 이름
예시 180 60 남 25 김아무개
이것을 공백을 기준으로 쪼개어 각 변수에 담아 출력한다.
이름을 f-string통해 세번 반복해서 출력한다.
'''
# s10 = input()
# a,b,c,d,e = s10.split()
# print(f"{a} {b} {c} {d} {e}")
# print("키:"f"{a}")
# print("몸무게:"f"{b}")
# print("성별:"f"{c}")
# print("나이:"f"{d}")
# print("이름:"f"{e}")

# print(f"{e*3}")

s20 = ["modu", "labs","good"] # list 형태 aka바구니

print("".join(s20))

name = 'licat'
age = 29

print('제 이름은 {}이고, 나이는 {}살입니다.'.format(name, age))
print(f'제 이름은{name}이고, 나이는{age}살입니다') #더 편하게 가능

print("Hello\nWorld!") # Hello와 World! 사이에 줄바꿈이 일어납니다.
print("Hello\tWorld!") # Hello와 World! 사이에 탭 간격이 생깁니다.
print("She said, \"Hello World!\"") # 큰따옴표 내부에 문자열을 출력합니다.
print('She said, \'Hello World!\'') # 작은따옴표 내부에 문자열을 출력합니다.
print("Backslash: \\") # 백슬래시를 출력합니다.


# bool 타입
### True = 1취금
### False = 0취급
a = 10 > 3
b = True
c = False 
print(type(a))
print(type(a))
print(a)
## bool 타입 형변환
a = 1
b = 0
c = -1
d = "okay"
f = ""

print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(f))

print(a==b)

x = None
print(x)
