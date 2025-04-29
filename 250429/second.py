# and 연산 (논리 곱) 전부 True여야 True성립

## 다른 언어에서는
# a&&b
'''
a = True
b = True

c = a and b 

d = 10 > 5 and 10 < 5 # d = True and False = False
print(d)

# or 연산 (논리 합)
f = 10 >= 10 or False # 앞에 이미 True가 나왔기 때문에 뒷 값에 상관없이 성립
print(f)

f = False and True and True # 0 1 1
print(f)

f2 = (False or True) and True 
print(f2)

# not 연산 (not 은 반대로)

f3 = not ((False or True) and True ) 
print(f3)

a = 10
b = 20

c = a!=b # 다르니? 라고 물어보는 기호 (!=)
c = not a!=b # False
'''
##
'''
a = int(input())
b = int(input())
c = int(input())
'''
### 항은 3개 이상 and, or는 마음대로 연결하여 결과 출력
# a,b,c = input().split()

# d = int(a)
# e = int(b)
# f = int(c)

# print(d>=e and (d!=f or e<f)) 


'''
a = 10

a = a + 10 # == a+=10

a += 10 

a -= 10 # == a = a - 10

# 멤버연산 in(있니?) not in(없니?)
st = "modulabs is good"

sta = "good" in st # "good"이라는 문자가 st에 있니?
sta = "good" not in st # "good"이라는 문자가 st에 없니?

# split

a = "123456-1122335"
c,d = a.split()
print(c,d)
'''
# 정수 3개가 공백을 두고 입력된다. # 1 2 3

# 합과 평균을 공백을 두고 출력한다.
# 평균은 소숫점 이하 셋째 자리 까지 보이게한다.
# (f-string)

a,b,c = input().split()

d = (int(a) + int(b) + int(c))
e = d /3
print(f"{d} {e:.3f}")