##연습장
# A,B = map(int,input().split())
# if A>B:
#     print(">")
# elif A<B:
#     print("<")
# else:
#     print("==")



## if문 연습
# a = 10
# b = 21

# if a > 10:
#     print("good")
# elif b == 20:
#     print("20입니다.")
# elif a == 10:
#     print("10입니다.")
# else:
#     print("이도저도 아니다.")
    
'''
split()활용

a,b 변수를 활용,
키, 몸무게를 입력받는다.

키와 몸무게를 나눈 나머지를 출력한다.

조건문을 활용해서 

키(a)가 130 이상이면 a, 150이상이면 b, 
170이상이면 c 180 이상이면 d를 출력하세요

'''
# #1
# a,b = input().split()
# a,b = (int(a),int(b))
# ## a,b = map(int,input().split())
# print(a % b)

# #2
# if 130<=a<150:
#     print("a")
# elif 150<=a<170:
#     print("b")
# elif 170<=a<180:
#     print("c")
# elif 180<=a:
#     print("d")

## 해설 
### <중요!> 큰 숫자부터 검증해야 한다!!
# if a>=180:
#     print("d")
# elif a>=170:
#     print("c")
# elif a>=150:
#     print("b")
# elif a>=130:
#     print("a")
# else:
#     print("키가 130 이하입니다")
'''
#문제
시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 
60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
'''

# a = int(input())

# if 90<=a:
#     print("A")
# elif 80<=a:
#     print("B")
# elif 70<=a:
#     print("C")
# elif 60<=a:
#     print("D")
# else:
#     print("F")

## 해설
# # 논리적으로 -> 첫번째로 걸러야 할 것은 무엇이냐 
# score = int(input())

# if score >= 90:
#     print("A")
# elif score >=80:
#     print("B")
# elif score >=70:
#     print("C")
# elif score >=60:
#     print("D")
# else:
#     print("F")


## and or 연산활용
# a = 10
# b = 20

# if a == 10 and b == 20:
#     print("good")
# else:
#     print("no")

'''
#문제
a,b,c를 입력받는다.
a가 100이고 b 200이상이면 "a"를 출력
b가 1이면 "b"를 출력
이도저도 아니면 c를 출력
'''

# a,b,c = input().split()
# a,b,c = int(a),int(b),int(c)

# if a == 100 and b >=200:
#     print("a")
# elif b == 1:
#     print("b")
# else:
#     print("c")

#백준 주사위 세게
'''
a,b,c = input().split()
a,b,c = int(a),int(b),int(c)

if a == b == c: # 같은 눈 3개
    print(10000 + a*1000 )
elif a==b or a==c: # 같은눈 2개 / a==b or a==c 
    print(1000 + a*100)
elif b==c: # 같은 눈 2개/ b==c
    print(1000 + b*100)
else:# 다 다를 때
    print(max(a, b, c)*100)
'''

## 해설 (max 안쓰고)
# a,b,c = input().split()
# a,b,c = int(a),int(b),int(c)

# if a == b == c:
#     price = 10000 + a * 1000
# elif a == c:
#     price = 1000 + a * 100
# elif b == c:
#     price = 1000 + b * 100

# else:
#     price = 0 # 0으로 초기화 해주는
# # 모두 다른 값일 때 최댓값 찾기
# if a != b and b!=c and a!=c:
#     temp = a
#     if b > temp:
#         temp = b
#     if c > temp:
#         temp = c
#     price = temp * 100

# print(f"상금: {price}원")        



