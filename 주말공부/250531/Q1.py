# 파이썬 클래스 문제 (중하 난이도)

## 문제 1: 은행 계좌 클래스

'''
**문제 설명:**
`BankAccount` 클래스를 만들어보세요.

**요구사항:**
1. 생성자에서 계좌 소유자 이름(`owner`)과 초기 잔액(`balance`, 기본값 0)을 받습니다
2. 다음 메서드들을 구현하세요:
   - `deposit(amount)`: 입금 (양수만 허용, 음수면 "입금액은 양수여야 합니다" 출력)
   - `withdraw(amount)`: 출금 (잔액 부족시 "잔액이 부족합니다" 출력)
   - `get_balance()`: 현재 잔액 반환
   - `get_owner()`: 계좌 소유자 이름 반환
3. 잔액은 직접 접근할 수 없도록 private 속성으로 만드세요
'''


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # private 속성
    
    def deposit(self, amount):
        if amount <= 0:
            print("입금액은 양수여야 합니다")
            return
        self.__balance += amount
    
    def withdraw(self, amount):
        if amount > self.__balance:
            print("잔액이 부족합니다")
            return
        self.__balance -= amount
    
    def get_balance(self):
        return self.__balance
    
    def get_owner(self):
        return self.owner





# **예시 사용법:**

# 계좌 생성
account = BankAccount("김철수", 1000)

# 입금
account.deposit(500)
print(account.get_balance())  # 1500

# 출금
account.withdraw(200)
print(account.get_balance())  # 1300

# 잘못된 입금 시도
account.deposit(-100)  # "입금액은 양수여야 합니다" 출력

# 잔액 부족 출금 시도
account.withdraw(2000)  # "잔액이 부족합니다" 출력




