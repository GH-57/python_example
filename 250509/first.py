# 리스트 인가? 튜플인가? 기준점을 가지고 있어야 한다
# 복습

a = (1, 10, 1, 2, 3)  # 튜플은 중복을 허용 한다

# 슬라이싱
b = a[2:5]  # (1,2,3)
c = a[1]
# 기능
a.count(1)  # 2
d = a.index(1)  # 0


# 셋 (set) 자료구조
# set은 중복을 허용하지 않는다!! + set은 순서가 보장되지 않는다!!
a = {1, 2, 3, 1}  
print(a)  # {1,2,3}
print(len(a))  # 3

# 형변환  list -> set

a = [1, 1, 1, 2, 2, 3]
b = set(a)  # 리스트를 셋으로
print(b)
c = list(b)  # 그 셋을 다시 리스트로
print(c)

a = {1, 2, 3}  # 셋은 인덱싱이 X
# print(a[0]) # TypeError: 'set' object is not subscriptable
'''
d = {"a", 1, 2, 3, 1, "a"}
print(d)

e = list(d)
print(e) 
# 중복이 제거되는데 문자의 위치가 계속 바뀐다.
'''
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"합집합: {set1 | set2}") # 합집합 기호: "|"
print(f"교집합: {set1 & set2}") # 교집합 기호: "&"
print(f"차집합: {set1 - set2}") # 차집합 기호: "-"
print(f"차집합: {set2 - set1}") ## 기준은 왼쪽값!

# set 수정 (add, remove)
fruits = {'apple', 'banana', 'cherry'}

fruits.add('orange') # append가 아닌 add를 쓴다
print(fruits)

fruits.remove('apple')
print(fruits)
# fruits.remove('apple') # KeyError: 'apple' 
# 없는 값을 지울 수 없다!

print(f"대칭 차집합: {set1.symmetric_difference(set2)}")
print(f"set1이 set2의 부분집합인가? {set1.issubset(set2)}")

