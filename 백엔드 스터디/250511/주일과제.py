# 1번
"""
ID = input()
Password = input()

if ID == ("admin" or "user") and Password == "1234":
    print("로그인 성공")
else:
    print("로그인 실패")
"""

# 2번
"""
Password = input()

if len(Password) >= 8 and ((Password.find("!") != -1 or Password.find("#") != -1)):
    print("유효한 비밀번호")
else:
    print("유효하지 않음")
"""

# 3번
"""
N = int(input())
j = " "
for i in range(N):
    j += "*"
    print(j)
"""

# 4번
"""
num = {"10의 자리":30, "100의 자리":400, "1의자리":5}
my_value = num.values()
my_list = list(my_value)
my_list.sort(reverse=True)
print(my_list)
"""

# 4번 모범답안
'''
a = {"a": 3, "b": 1, "c": 2}
b = sorted(a.items(), key=lambda x: x[1], reverse=True)
print(b)
'''

# 5번
'''
for i in range(2, 10): # 2부터 9까지
    for j in range(1,10): # 1부터 9까지
        print(f"{i} * {j} = {i*j}")
'''