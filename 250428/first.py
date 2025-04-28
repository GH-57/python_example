
# 정수
a = 10
b = 20
c= 0
d = -40
print(type(a),type(b),type(c),type(d))
print(int(9.333)) # 정수형 int

# 실수 
number1 = 3.12
number2 = -0.12
print(type(number1),type(number2))
print(float(3)) # 실수형 float

## 무한대
x = float("inf") # 양의 무한대
y = float("-inf") # 음의 무한대

# 문자열
str1 = "adcd"
str2 = 'abcd'

str3 = '''
오늘은 4월 28일 입니다.

5월이 멀지 않았네요.
5월에는 내 생일!
''' # str에 ''' 담으면 문자열로 인식한다
str4 = '오늘은 4월 28일입니다.\n\n5월이 멀지 않았네요'

print(type(str3))
print(str3)
print(str4)

#문자열 이어붙이기

str6 = "modu"
str7 = "labs"

print(str6+str7)
str8 = str6+str7 

print(str8)

# 개인정보 출력해보기
## 1. 성, 이름 변수를 따로 만들어서 +로 합친 후 출력
## 2. 주민등록번호도 1번과 같이
## 3. 이메일 {아이디} {@} {네이버, 구글}

## 1.
name1 = "Kim"
name2 = "modu"
print(name1+name2)

## 2.
name3 = "220222"
name4 = "3731119"
print(name3+"-"+name4)

##3.
name5 = "abced11"
name6 = "naver.com"
print(name5+"@"+name6)

#문자열 반복하기
str10 = str1 * 10

test2 = "30" 

print(str10)
# print(str1 * test2) (x) test2가 문자열이기 때문에 오류남
# print(str10+"입니다",+"어쩌고저쩌고")
# 오늘은 4월 28일입니다.
a = "5"
b = "7"
#기본방식
print("오늘은"+a+"월"+b+"일입니다")

# f""(f-string) 굉장히 많이 사용한다!!! 문자열은{}로 표기기
# 문자열 안에 변수를 사용할 수 있게 해준다
print(f"오늘은 {a}월{b}일입니다.")

print(f"{a}월{b}일은 내 생일 입니다.")

# 문자열 인덱싱 []로 한다

s = "life is good"
print(s[0]) 
print(s[3])
print(s[-1])

## print(s[300]) IndexError: string index out of range
## 주민등록번호가 13자리
## print(s[13]) (Error)

# 문자열 슬라이싱 #[start:stop:step] (stop은 원하는 수보다 1높게!!)

print(s[0:3]) # s[0:3:1] step 생략가능
print(s[0:4:2])

# 다양한 슬라이싱 방법
s = 'weniv CEO licat'
print(1, s[0:5]) 
print(2, s[6:]) # stop생략 == 끝까지
print(3, s[:]) 
print(4, s[::-1]) 
print(5, s[::2])

# 테스트
## ip address = 172.100.200.100
'''
1. ip address문자열을 슬라이싱 기법을 활용해 변수에 담아 출력
2. a,b,c,d 라는 변수에 슬라이싱 기법을 통해 .을 기준으로 각각 담는다
3. f-string을 활용해서 172100200100 이 나오게 하기
'''
#1.
s = "ip address = 172.100.200.100"
print(s[0:10])
## address = s[0:10]

#2.
a = s[13:16]
b = s[17:20]
c = s[21:24]
d = s[25:]
print(a,b,c,d)
# a,b,c,d = s[13:16],s[17:20],s[21:24],s[25:28] 더 간단히 가능


#3.
print(f"{a}{b}{c}{d}")

# 입력을 받는다
