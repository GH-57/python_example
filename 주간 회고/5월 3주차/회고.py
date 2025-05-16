# def asd():
#     pass

# print(asd())

# data = [10, 20, 30, 40]
# result = list(filter(lambda x:x >20,data))
# print(result)

# def outer(x):
#     def inner(y):
#         return x + y
#     return inner

# closure = outer(10)
# result = closure(5)
# print(result)

# data = [10, 20, 30, 40, 50]

# a = list(map(lambda x:x*3+2,data))
# print(a)



'''
class Student:
    def __init__(self, name, student_id):
        # 학생 이름과 학번을 저장하는 속성을 만드세요
        # 성적을 저장할 빈 딕셔너리도 만드세요 (교과목 이름: 점수)
        self.name = name
        self.student_id = student_id
        self.scores = {}
   
    def add_score(self, subject, score):
        # 특정 과목의 성적을 추가하거나 수정하는 메서드를 만드세요
        ## 딕셔너리에 과목명을 키로, 점수를 값으로 저장
        self.scores[subject] = score
   
    def get_average(self):
        # 전체 과목의 평균 점수를 계산하는 메서드를 만드세요
        # 과목이 없으면 0을 반환하세요
        if not self.scores: # 성적이 비면 0 반환
            return 0
        
        total_score = sum(self.scores.values()) 
        # 점수 딕셔너리에 벨류값(점수) 다 더하기
        return total_score / len(self.scores)

   
    def get_highest_subject(self):
        # 가장 점수가 높은 과목과 그 점수를 반환하는 메서드를 만드세요
        # 반환 형식: (과목명, 점수)
        # 과목이 없으면 ("없음", 0)을 반환하세요
        if not self.scores: # 성적이 비면 
            return ("없음", 0)
        
        best_subject = max(self.scores, key=self.scores.get)
        return (best_subject, self.scores[best_subject])
   
    def show_scores(self):
        # 모든 과목과 점수, 그리고 평균 점수를 출력하는 메서드를 만드세요
        ##왜 for문으로 가능한지 모르겠고
        for subject, score in self.scores.items():
            print(f"{subject}: {score}점")

        print(f"평균점수: {self.get_average()}점")


# 테스트 코드
student = Student("라이캣", "20250101")

student.add_score("수학", 85)
student.add_score("영어", 92)
student.add_score("과학", 78)

# 출력
print(f"학생 이름: {student.name}")  # 출력: 학생 이름: 라이캣
print(f"학번: {student.student_id}")  # 출력: 학번: 20250101
print(f"평균 점수: {student.get_average()}")  # 출력: 평균 점수: 85.0

best_subject, best_score = student.get_highest_subject()
print(f"최고 점수 과목: {best_subject}, 점수: {best_score}")  # 출력: 최고 점수 과목: 영어, 점수: 92

student.show_scores()
# (실행 시 출력 예시)
# 수학: 85점
# 영어: 92점
# 과학: 78점
# 평균 점수: 85.0점
'''