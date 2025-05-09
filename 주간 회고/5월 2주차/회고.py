# my_tuple = (1,2,3,4,5)
# print(my_tuple[1:4])

# a = [1,2,3,4,5]
# a.append(6)
# a.remove(2)
# print(a)

# total = 0
# for i in range(1,5):
#     total +=i
# print(total)

# score = 75
# if score >= 90:
#     result = "A"
# elif score >= 80:
#     result = "B"
# elif score >= 70:
#     result = "C"
# else:
#     result = "D"
# print(result)

# text = "Python Programming"
# print(text[7:13])

# student = {"name": "Kim", "age": 20, "grade": "A"}
# student["age"] = 21
# print(student["age"])


# result = 0
# for i in range(3): # 0부터 2까지
#     for j in range(2): # 0부터 1까지
#         result += i + j
# print(result)

# a = 5
# b = 10
# c = 15
# if a > b:
#     print("A")
# elif b > c:
#     print("B")
# elif a + b == c:
#     print("C")
# else:
#     print("D")


# numbers = [2, 4, 6, 8, 10]
# result = []
# for num in numbers:
#     if num > 5:
#         result.append(num // 2) # [3, 4, 5]
# print(result)


# data = {"a": [1, 2, 3], "b": [4, 5, 6]}
# result = 0
# for key in data:
#     for num in data[key]:
#         if num % 2 == 0: # 짝수이면
#             result += num # 2+4+6
# print(result)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = []

# for num in numbers:
#     if num % 2 == 0:
#         even_numbers.append(num)

# print(even_numbers)  # 출력: [2, 4, 6, 8, 10]


# temp = float(input())

# if temp >= 100:
#     print("수증기")
# elif 0<=temp<100:
#     print("물")
# else:
#     print("얼음")


# scores = {"국어": 85, "영어": 90, "수학": 78, "과학": 92}

# scores1 = list(scores.values()) # 국영수과 점수를 리스트로 출력
# print(f"평균은 {sum(scores1[0:4]) / 4}점 입니다.") # 86.25


# text = input()
# text1 = text.replace(" ", "").lower()
# print(text1)

# a = int(input())
# sum = 0

# for i in range(1, a + 1):  # 1부터 입력한 숫자 까지
#     if i % 3 == 0:  # 3의 배수 이면
#         print("제외합니다")
#     elif i % 3 != 0:  # 3의 배수가 아니면
#         sum += i  # 다 더해서
#     print(sum)  # 출력
