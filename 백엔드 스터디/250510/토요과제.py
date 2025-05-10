
# 1번
"""
a = int(input())
b = int(input())
print(a+b)
"""

# 2번
"""
a = input()
b = a[::-1]
print(b)
"""

# 3번
"""
a = int(input())
if a % 2 == 0: # 짝수이면
    print('Even')
else: #홀수이면
    print('Odd')
"""

# 4번
"""
a = [1, 2, 3, 4, 5]
b = sum(a) // 5  # /는 실수형, //는 정수형으로 출력
print(b)
"""

# 5번
"""
a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]
c = list(set(a) & set(b))  # 셋으로 바꿔서 교집합 구한 후, 리스트로 전환
print(c)
"""

# 6번
'''
a = (1, [2, 3], 4)
a[1][1] = 100
print(a)
'''