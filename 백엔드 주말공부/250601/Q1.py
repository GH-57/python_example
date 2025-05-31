'''
문제 1: 숫자 맞추기 게임
1부터 100 사이의 랜덤한 숫자를 생성하고, 사용자가 숫자를 입력해서 맞추는 게임을 만드세요. 입력한 숫자가 정답보다 크면 "더 작은 수를 입력하세요", 작으면 "더 큰 수를 입력하세요"라고 힌트를 주고, 맞추면 "정답입니다!"와 함께 시도 횟수를 출력하세요.
'''



import random

def ngame():
    target = random.randint(1, 100)
    attempts = 0

    print("1부터 100사이의 숫자를 맞춰보세요")

    while True:
        try:
            guess = int(input("숫자를 입력하세요: "))
            attempts +=1

            if guess > target:
                print("더 작은 수 입니다!")

            elif guess < target:
                print("더 큰 수 입니다!")

            else:
                print(f"정답! {attempts}번 만에 맞췄습니다!")
                break
        except ValueError:
            print("올바른 숫자를 입력하세요!")

ngame()