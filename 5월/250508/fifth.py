# 튜플
##(값을 변경 할 수 X)
a = (1, 2, 3, "good")
b = [1, 2, 3]
print(type(a))  # <class 'tuple'>

print(a[3])  # 인덱싱 가능

b = a[0:2]  # 슬라이싱 가능
print(b)

# a[3] = "good" # TypeError: 'tuple' object does not support item assignment

numbers = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3)

print(numbers.count(5))  # 2
print(numbers.index(5))  # 4 제일 처음에 있는 인덱스를 찾음.

bc = (1,[12,3,4])
bc[1][0] = "good"
print(bc[1])
