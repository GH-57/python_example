## 문제 2: 학생 성적 관리 클래스
'''
**문제 설명:**
`Student` 클래스를 만들어 학생의 성적을 관리해보세요.

**요구사항:**
1. 생성자에서 학생 이름(`name`)과 학번(`student_id`)을 받습니다
2. 성적은 딕셔너리로 관리합니다 (과목명: 점수)
3. 다음 메서드들을 구현하세요:
    - `add_grade(subject, score)`: 과목별 성적 추가 (0~100 범위 체크)
    - `get_grade(subject)`: 특정 과목 성적 반환 (없으면 "해당 과목이 없습니다" 출력)
    - `get_average()`: 전체 평균 점수 반환 (소수점 2자리까지)
    - `get_info()`: 학생 정보 출력 (이름, 학번, 모든 과목과 성적, 평균)
4. 점수는 0~100 범위만 허용하며, 범위 밖이면 "점수는 0~100 사이여야 합니다" 출력
'''

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {}
        
        
    def add_grade(self, subject, score):
        if score <0 or score >100:
            print("점수는 0~100 사이여야 합니다")
            return
        self.grades[subject] = score


    def get_grade(self, subject):
        if subject not in self.grades:
            print("해당 과목이 없습니다")
            return None
        return self.grades[subject]


    def get_average(self):
        if not self.grades:  # 성적이 없는 경우
            return 0.0
        total = sum(self.grades.values())
        average = total / len(self.grades)
        return round(average, 2)
    
    def get_info(self):
        print(f"학생명: {self.name}")
        print(f"학번: {self.student_id}")
        
        if self.grades:
            grade_str = ", ".join([f"{subject}({score})" for subject, score in self.grades.items()])
            print(f"성적: {grade_str}")
            print(f"평균: {self.get_average()}")
        else:
            print("등록된 성적이 없습니다")

# **예시 사용법:**

# 학생 생성
student = Student("이영희", "2024001")

# 성적 추가
student.add_grade("수학", 85)
student.add_grade("영어", 92)
student.add_grade("과학", 78)

# 특정 과목 성적 조회
print(student.get_grade("수학"))  # 85

# 평균 계산
print(student.get_average())  # 85.00

# 학생 정보 출력
student.get_info()
# 출력 예시:
# 학생명: 이영희
# 학번: 2024001
# 성적: 수학(85), 영어(92), 과학(78)
# 평균: 85.00

# 잘못된 점수 입력
student.add_grade("국어", 105)  # "점수는 0~100 사이여야 합니다" 출력



'''
## 힌트
- **문제 1**: private 속성은 언더스코어(`_`) 또는 더블 언더스코어(`__`)를 사용하세요
- **문제 2**: 평균 계산시 성적이 없는 경우도 고려해보세요 (0으로 반환하거나 적절한 메시지 출력)
'''