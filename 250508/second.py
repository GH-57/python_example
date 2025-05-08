# a = [1,2,3,1,1,2,3,4,5,"good"]

# a[0]=3

# print(a)

# a[3] = "aaaa"

# print(a)

# a[3][1] = "g" # agaa을 의도한것 but Error
# # 문자열의 특정 값을 새로운 값으로 대채할 수 없다
# # 하려면 새로운 문자열을 대입하라
# # 리스트는 중복을 허용한다..!!

# li = []
# # 데이터 추가
# li.append(1)
# li.append(2)
# li.append([1,2,3])
# print(li)
# # [1,2,[1,2,3]]
# li[2].append("good")
# print(li)

# # 데이터 삭제 (리스트 안에 있는 데이터만 삭제)
# li.clear()
# print(li)

# # 데이터 복제
# b = [1,2,3]
# c = b.copy()

# c. append(2)
# print(b)
# print(c)

"""
1. 빈 리스트를 만든다.
2. append를 사용하여 이중 리스트를 만든다.
3. 출력한다.
4. 리스트의 데이터를 다 지운다.
5. 출력한다.
6. copy를 이용한다.
7. 카피를 활용한 리스트에 append를 사용하여 출력한다.
"""

# li = []
# li.append(["good","hello"])
# print(li)

# li.clear()
# print(li)

# li2 = li.copy()
# li2.append("like")
# print(li)
# print(li2)

# # # count
# a = [1, 2, 3, "okay", 1, 1, 1]
# print(a.count(1))  # 4

# b = [1, 2, 3, [1, 2, 3, 1]]
# print(b.count(1))  # 1
# # 3이 나오게 하려면?
# print(b[2])
# print(b[3][2])
# print(b.count(1) + b[3].count(1))
# # b[3]을 파이썬이 추측할 수 없어서 .해도 나오지 않는다

# # extend
# a = [1, 2, 3, 4]
# b = [5,6,7,8]
# # [1,2,3,4,5,6,7,8]
# a. extend(b)
# print(a)
# c = "good"
# b.extend(c)
# print(b)

# a = ["good", "okay"]
# # b = a.index("aaaa") # ValueError: 'aaaa' is not in list
# # print(b)
# ## list는 find를 지원하지 않는다.
# c = a.index("okay")
# print(c)



