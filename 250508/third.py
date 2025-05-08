# # insert(삽입)
# a = [1, 2, 3, 4, 5]

# # insert(인덱스{위치}, 값)
# a.insert(0, 0)  # 0번째 위치에 0을 삽입
# print(a)  # [0,1,2,3,4,5]
# ## append와 insert 차이 숙지:
# ## insert는 인덱스 값이 바뀌게 된다.

# # pop() 제일 끝에 있는 값 추출
# # 리스트 값이 비어있으면 IndexError: pop from empty list
# b = a.pop()
# print(a)
# # 미연에 방지하려면?
# if len(a) >= 1:  # a라는 리스트 내부의 데이터 갯수가 1개 이상이면
#     a.pop()
# else:
#     print("리스트가 비어있습니다")

# # remove(값) # 왼쪽부터 딱 하나 지운다
# # remove도 인덱스 값이 바뀌게 된다
# c = [1, 2, 3, 1, 1]
# c.remove(1)  # [2,3,1,1]
# print(c)
# c.remove(1)  # [2,3,1]
# # c.remove(50) #ValueError: list.remove(x): x not in list


# """
# 1. 기존에 데이터가 있는 리스트를 만든다.
# 2. insert를 활용해서 데이터를 넣는다.
# 3. pop을 사용하여 꺼낸 데이터를 출력한다.
# 4. remove를 사용하여 특정 데이터를 제거해본다.
# """
# li = ["사과", "배", "딸기", "망고"]
# li.insert(0, "바나나")
# print(li)  # ["바나나","사과","배","딸기","망고"]

# a = li.pop()
# print(a)  # 망고

# li.remove("딸기")
# print(li)  # ["바나나","사과","배"]

# # reverse vs reversed
# ## reverse는 변수에 담아도 값이 없다
# a = [1, 2, 3, 4, 5]
# a.reverse() # [5,4,3,2,1]
# print(a)
# b = a.reverse()
# print(b) # None

# #reversed는 원본을 훼손하지 않는다.
# a = [1, 2, 3, 4, 5]
# b = list(reversed(a)) # 파이썬에서 제공하는 기능 (함수)
# print(a)
# print(b)
# c = a[::-1]

# # sort vs sorted (오름차순 정렬)
# a = [5, 4, 3, 2, 1]

# # a.sort() # 원본데이터 자체를 변경
# b = list(sorted(a))  # 원본데이터 복사후 정렬 ->리스트 타입으로 변경
# print(a)
# print(b)
# c = [1, 2, 3, 4, 5]
# # sorted(리스트,reverse=bool)
# sorted(c, reverse=False)  # sorted(a)
# d = list(sorted(c, reverse=True))  # 내림차순 정렬
# print(d)

