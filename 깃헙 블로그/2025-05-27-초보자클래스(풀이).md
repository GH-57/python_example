# 파이썬 클래스 문제 풀이 답안 📝

## 문제 1 풀이: 강아지 클래스 🐶

```python
class Dog:
    def __init__(self, name, age):
        self.name = name  # 강아지 이름
        self.age = age    # 강아지 나이
    
    def bark(self):
        print("멍멍!")
    
    def introduce(self):
        print(f"안녕! 내 이름은 {self.name}이고 {self.age}살이야!")

# 사용 예시
my_dog = Dog("뽀삐", 3)
my_dog.bark()        # 출력: 멍멍!
my_dog.introduce()   # 출력: 안녕! 내 이름은 뽀삐이고 3살이야!

# 다른 강아지도 만들어보기
another_dog = Dog("초코", 5)
another_dog.bark()        # 출력: 멍멍!
another_dog.introduce()   # 출력: 안녕! 내 이름은 초코이고 5살이야!
```

### 🔍 해설
- `__init__` 메서드에서 이름과 나이를 받아서 객체의 속성으로 저장
- `self.name`, `self.age`로 객체마다 고유한 데이터 보관
- f-string을 사용해서 문자열에 변수 값을 쉽게 삽입

---

## 문제 2 풀이: 계산기 클래스 🧮

```python
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b

# 사용 예시
calc = Calculator()
print(calc.add(5, 3))       # 출력: 8
print(calc.subtract(10, 4)) # 출력: 6
print(calc.multiply(7, 2))  # 출력: 14

# 연속 계산 예시
result1 = calc.add(10, 5)      # 15
result2 = calc.multiply(result1, 2)  # 30
print(f"최종 결과: {result2}")  # 출력: 최종 결과: 30
```

### 🔍 해설
- 각 메서드는 매개변수를 받아서 계산 후 결과를 `return`
- `__init__` 메서드가 없어도 클래스는 만들 수 있음
- 계산 결과를 변수에 저장해서 다음 계산에 활용 가능

---

## 문제 3 풀이: 자동차 클래스 🚗

```python
class Car:
    def __init__(self, brand, color):
        self.brand = brand   # 브랜드
        self.color = color   # 색깔
        self.speed = 0       # 초기 속도는 0
    
    def start(self):
        print("시동을 걸었습니다!")
    
    def accelerate(self):
        self.speed += 10
        print(f"현재 속도: {self.speed}km/h")
    
    def brake(self):
        self.speed -= 10
        if self.speed < 0:  # 속도가 음수가 되지 않도록
            self.speed = 0
        print(f"현재 속도: {self.speed}km/h")

# 사용 예시
my_car = Car("현대", "빨강")
my_car.start()        # 출력: 시동을 걸었습니다!
my_car.accelerate()   # 출력: 현재 속도: 10km/h
my_car.accelerate()   # 출력: 현재 속도: 20km/h
my_car.brake()        # 출력: 현재 속도: 10km/h
my_car.brake()        # 출력: 현재 속도: 0km/h
my_car.brake()        # 출력: 현재 속도: 0km/h (음수가 되지 않음)

# 자동차 정보 확인
print(f"내 차는 {my_car.color} {my_car.brand} 자동차입니다.")
# 출력: 내 차는 빨강 현대 자동차입니다.
```

### 🔍 해설
- `speed` 속성을 초기값 0으로 설정
- `accelerate()`에서 `+=` 연산자로 속도 증가
- `brake()`에서 속도가 0 아래로 내려가지 않게 조건문 사용
- 객체의 속성값은 언제든지 접근해서 확인 가능

---

## 🎯 추가 도전 과제

### 1. 강아지 클래스 업그레이드
```python
class Dog:
    def __init__(self, name, age, breed="믹스"):
        self.name = name
        self.age = age
        self.breed = breed  # 견종 추가
        self.energy = 100   # 에너지 레벨
    
    def bark(self):
        print("멍멍!")
        self.energy -= 10  # 짖으면 에너지 소모
    
    def play(self):
        if self.energy > 20:
            print(f"{self.name}가 신나게 놀고 있어요!")
            self.energy -= 20
        else:
            print(f"{self.name}가 너무 피곤해요...")
    
    def sleep(self):
        print(f"{self.name}가 잠을 자고 있어요... 💤")
        self.energy = 100  # 에너지 회복

# 사용해보기
puppy = Dog("멍멍이", 1, "골든리트리버")
puppy.play()   # 신나게 놀기
puppy.play()   # 또 놀기
puppy.play()   # 에너지 부족
puppy.sleep()  # 잠자고 에너지 회복
```

### 2. 계산기 클래스 업그레이드
```python
class Calculator:
    def __init__(self):
        self.history = []  # 계산 기록 저장
    
    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def show_history(self):
        print("=== 계산 기록 ===")
        for record in self.history:
            print(record)

# 사용해보기
calc = Calculator()
calc.add(10, 5)
calc.subtract(20, 8)
calc.show_history()
```

## 💡 클래스를 잘 만드는 팁

1. **명확한 이름 사용**: 클래스명은 대문자로 시작, 기능을 잘 표현하는 이름
2. **관련된 데이터와 기능 묶기**: 한 클래스에는 관련된 속성과 메서드만
3. **초기값 설정**: `__init__`에서 필요한 속성들을 적절히 초기화
4. **에러 방지**: 잘못된 값이 들어오지 않도록 조건문 활용
5. **재사용성**: 다양한 상황에서 쓸 수 있게 유연하게 설계

클래스는 현실 세계의 사물이나 개념을 코드로 표현하는 도구예요. 많이 연습해보면서 감각을 익혀보세요! 🚀