
# 일급 함수 (first class function)를 지원하는 언어: 파이썬, 자바스크립트 등
#  - 함수를 변수처럼 동적으로 생성할 수 있고, 인자로 넘길 수 있고, 반환값으로 받을 수 있다

def make_function():
    # 지역변수 (local variable)
    base = 10 # 매 make_function 호출 시마다, 생성

    # 함수를 동적으로 생성.
    # func = lambda number: number + base

    def func(number):
        return number + base

    return func


ret1 = make_function()
print(ret1(1))

ret2 = make_function()
ret3 = make_function()
