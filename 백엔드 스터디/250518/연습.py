'''
문제: 학생 성적 관리 클래스 구현하기

아래 요구사항에 맞는 Student 클래스를 구현하세요:

1. 학생의 이름(name), 학번(student_id), 성적 리스트(scores)를 저장할 수 있어야 합니다.
2. 성적을 추가하는 메서드(add_score)를 구현하세요.
3. 평균 성적을 계산하는 메서드(get_average)를 구현하세요.
4. 학생 정보를 문자열로 반환하는 메서드(__str__)를 구현하세요.

예상 실행 결과:
학생 정보: 이름: 홍길동, 학번: 20231234, 평균 성적: 85.0
'''
'''
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.stutent_id = student_id
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def get_average(self):
        if not self.scores:
            return 0 
        return sum(self.scores) / len(self.scores)
    
    def __str__(self):
        return f"이름: {self.name}, 학번: {self.stutent_id}, 평균 성적: {self.get_average()}"
    


if __name__ == "__main__":
    student = Student("홍길동", "20231234")

    student.add_score(90)
    student.add_score(80)
    student.add_score(85)

    print(f"학생정보: {student}")
'''

#==========================================================


# 문제: 애완동물 관리 시스템
# 아래 코드를 완성하여 간단한 애완동물 관리 시스템을 만들어보세요.
# Pet 클래스와 주요 메서드의 일부가 비어있습니다. 주석을 참고하여 완성해주세요.

class Pet:
    def __init__(self, name, animal_type, age):
        """
        애완동물 객체 초기화
        name: 애완동물 이름
        animal_type: 동물 종류 (강아지, 고양이 등)
        age: 나이
        """
        # TODO: 여기에 초기화 코드를 작성하세요.
        # 이름, 종류, 나이를 저장하고, 
        # 행복 지수(happiness)와 배고픔 지수(hunger)를 각각 50으로 초기화하세요.
        self.name = name
        self.animal_type = animal_type
        self.age = age
        self.happiness = 50  # 행복 지수 (0~100)
        self.hunger = 50     # 배고픔 지수 (0~100)
    
    def feed(self):
        """애완동물에게 먹이를 줍니다"""
        # TODO: 이 메서드를 완성하세요.
        # 1. 애완동물이 이미 배부른 상태(배고픔 지수가 10 이하)라면
        #    "{이름}은(는) 이미 배불러요!" 메시지를 반환하세요.
        # 2. 그렇지 않다면, 배고픔 지수를 20 감소시키고 행복 지수를 10 증가시키세요.
        # 3. 배고픔은 0보다 작아질 수 없고, 행복 지수는 100을 초과할 수 없습니다.
        # 4. "{이름}에게 먹이를 주었습니다. 배고픔: {배고픔 지수}, 행복: {행복 지수}" 메시지를 반환하세요.
        
        if self.hunger <= 10:
            return f"{self.name}은(는) 이미 배불러요!"
        
        self.hunger -= 20
        self.happiness += 10

        self.hunger = max(0, self.hunger)
        self.happiness = min(100, self.happiness)

        return f"{self.name}에게 먹이를 주었습니다. 배고픔: {self.hunger}, 행복: {self.happiness}"
    
    def play(self):
        """애완동물과 놀아줍니다"""
        # TODO: 이 메서드를 완성하세요.
        # 1. 애완동물이 너무 배고픈 상태(배고픔 지수가 80 이상)라면
        #    "{이름}은(는) 너무 배고파서 놀 수 없어요!" 메시지를 반환하세요.
        # 2. 그렇지 않다면, 행복 지수를 20 증가시키고 배고픔 지수를 10 증가시키세요.
        # 3. 행복 지수와 배고픔 지수는 100을 초과할 수 없습니다.
        # 4. "{이름}와(과) 놀아주었습니다. 배고픔: {배고픔 지수}, 행복: {행복 지수}" 메시지를 반환하세요.
        
        if self.hunger >= 80:
            return f"{self.name}은(는) 너무 배고파서 놀 수 없어요!"
        
        self.happiness += 20  # 행복 증가
        self.hunger += 10     # 배고픔 증가
        
        # 최대값 제한
        self.happiness = min(100, self.happiness)
        self.hunger = min(100, self.hunger)
        
        return f"{self.name}와(과) 놀아주었습니다. 배고픔: {self.hunger}, 행복: {self.happiness}"
    
    def get_status(self):
        """애완동물의 상태를 반환합니다"""
        # TODO: 이 메서드를 완성하세요.
        # 1. 행복 지수에 따라 기분 상태(mood)를 결정하세요:
        #    - 80 이상: "매우 행복함"
        #    - 50 이상: "행복함"
        #    - 20 이상: "지루함"
        #    - 20 미만: "슬픔"
        # 2. 배고픔 지수에 따라 배고픔 상태(hunger_status)를 결정하세요:
        #    - 80 이상: "매우 배고픔"
        #    - 50 이상: "배고픔"
        #    - 20 이상: "약간 배고픔"
        #    - 20 미만: "배부름"
        # 3. "{이름}({종류}, {나이}세) - 상태: {기분 상태}, 배고픔: {배고픔 상태}" 형식의 문자열을 반환하세요.
        
        if self.happiness >= 80:
            mood = "매우 행복함"
        elif self.happiness >= 50:
            mood = "행복함"
        elif self.happiness >= 20:
            mood = "지루함"
        else:
            mood = 슬픔

        if self.hunger >= 80:
            hunger_status = "매우 배고픔"
        elif self.hunger >= 50:
            hunger_status = "배고픔"
        elif self.hunger >= 20:
            hunger_status = "약간 배고픔"
        else:
            hunger_status = "배부름"
            
        return f"{self.name}({self.animal_type}, {self.age}세) - 상태: {mood}, 배고픔: {hunger_status}"


# 테스트 코드 - 수정하지 마세요!
if __name__ == "__main__":
    # 애완동물 생성
    my_dog = Pet("멍멍이", "강아지", 3)
    my_cat = Pet("야옹이", "고양이", 2)
    
    # 상태 확인
    print("== 초기 상태 ==")
    print(my_dog.get_status())
    print(my_cat.get_status())
    
    # 강아지와 상호작용
    print("\n== 강아지와 상호작용 ==")
    print(my_dog.feed())  # 먹이 주기
    print(my_dog.play())  # 놀아주기
    print(my_dog.play())  # 한 번 더 놀아주기
    
    # 고양이와 상호작용
    print("\n== 고양이와 상호작용 ==")
    print(my_cat.play())  # 놀아주기
    print(my_cat.play())  # 한 번 더 놀아주기
    print(my_cat.play())  # 또 놀아주기 (배고픔 증가)
    
    # 최종 상태 확인
    print("\n== 최종 상태 ==")
    print(my_dog.get_status())
    print(my_cat.get_status())
    
    # 배고픈 고양이에게 먹이 주기
    print("\n== 배고픈 고양이 먹이 주기 ==")
    print(my_cat.feed())
    print(my_cat.get_status())

"""
예상 출력 결과:
== 초기 상태 ==
멍멍이(강아지, 3세) - 상태: 행복함, 배고픔: 배고픔
야옹이(고양이, 2세) - 상태: 행복함, 배고픔: 배고픔

== 강아지와 상호작용 ==
멍멍이에게 먹이를 주었습니다. 배고픔: 30, 행복: 60
멍멍이와(과) 놀아주었습니다. 배고픔: 40, 행복: 80
멍멍이와(과) 놀아주었습니다. 배고픔: 50, 행복: 100

== 고양이와 상호작용 ==
야옹이와(과) 놀아주었습니다. 배고픔: 60, 행복: 70
야옹이와(과) 놀아주었습니다. 배고픔: 70, 행복: 90
야옹이와(과) 놀아주었습니다. 배고픔: 80, 행복: 100

== 최종 상태 ==
멍멍이(강아지, 3세) - 상태: 매우 행복함, 배고픔: 배고픔
야옹이(고양이, 2세) - 상태: 매우 행복함, 배고픔: 매우 배고픔

== 배고픈 고양이 먹이 주기 ==
야옹이에게 먹이를 주었습니다. 배고픔: 60, 행복: 100
야옹이(고양이, 2세) - 상태: 매우 행복함, 배고픔: 배고픔
"""