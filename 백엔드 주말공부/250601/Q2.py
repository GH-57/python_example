'''
문제 2: 단어 뒤집기
문자열을 입력받아서 각 단어는 그대로 두되, 단어 내의 문자들만 뒤집는 함수를 작성하세요. 예를 들어 "Hello World Python"이 입력되면 "olleH dlroW nohtyP"가 출력되어야 합니다.
'''



def reverwords(text):
    words = text.split()
    reverwords = [word[::-1] for word in words]
    return ' '.join(reverwords)

print("문제 2 결과:")
test_text = "hello Word"
result = reverwords(test_text)
print(f"입력: {test_text}")
print(f"출력: {result}")