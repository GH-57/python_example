'''
문제 3: 중복 제거하고 정렬하기
숫자들이 담긴 리스트에서 중복된 숫자들을 제거하고, 남은 숫자들을 오름차순으로 정렬한 후 짝수와 홀수를 따로 분리해서 딕셔너리 형태로 반환하는 함수를 작성하세요.
예: [3, 1, 4, 1, 5, 9, 2, 6, 5] → {'even': [2, 4, 6], 'odd': [1, 3, 5, 9]}
'''


def num_process(numbers):
    _sorted = sorted(set(numbers))


    even_num = [num for num in _sorted if num % 2 == 0]
    odd_num = [num for num in _sorted if num % 2 == 1]

    return {'even': even_num, 'odd': odd_num}




print("문제 3 결과:")
test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
result = num_process(test_list)
print(f"입력: {test_list}")
print(f"출력: {result}")