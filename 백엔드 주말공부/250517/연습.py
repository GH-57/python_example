# Claude 클래스 문제 풀어보기
'''
문제: 간단한 학생 정보 관리 클래스 만들기
다음 요구사항에 맞는 Student 클래스를 작성하세요:

1. 학생의 이름, 나이, 점수를 저장할 수 있는 클래스를 만드세요.
2. 학생 정보를 출력하는 메서드를 추가하세요.
3. 점수를 업데이트하는 메서드를 추가하세요.
4. 학생이 합격했는지 확인하는 메서드를 추가하세요. (점수가 60점 이상이면 합격)
'''

class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


    def student_inform(self):
        print(f"이름: {self.name}, 나이: {self.age}, 점수: {self.score}")

    def update_score(self, new_score):
        print(f"{self.name}학생 점수가 {self.score}에서 {new_score}로 업뎃 됨")
        self.score = new_score

    def pass_(self):
        if self.score >= 60:
            print(f"{self.name}학생은 합격입니다.")
        else:
            print(f"{self.name}학생은 불합격입니다.")




if __name__ == "__main__":

    student1 = Student("홍길동", 20, 85)
    
    # 학생 정보 출력
    student1.student_inform()
    
    # 점수 업데이트 (85 → 90)
    student1.update_score(90)
    
    # 합격 여부 확인
    student1.pass_()