'''
문제
당신은 작은 도서관의 책 관리 시스템을 개발하고 있습니다.
다음 단계에 따라 리스트를 활용한 책 관리 시스템을 구현해보세요.

# 1단계: 초기 도서 목록 생성하기
-books 리스트에 다음 5권의 책을 추가하세요: "파이썬 기초", "데이터 과학 입문",
 "알고리즘의 이해", "머신러닝 실전", "파이썬 기초"
-books 리스트를 출력하세요.

# 2단계: 책 목록 관리하기
-목록에서 "파이썬 기초"가 몇 권 있는지 확인하세요.
-"웹 개발의 시작"이라는 책을 목록 끝에 추가하세요.
-"데이터베이스 설계"라는 책을 3번째 위치에 삽입하세요.
-새로운 책 리스트 new_books를 만들고 ["인공지능 개론", "클라우드 컴퓨팅"]을
포함시킨 후, books 리스트에 추가하세요. # extend 활용!!
-수정된 books 리스트를 출력하세요.

# 3단계: 책 제거 및 관리하기
-목록에서 첫 번째로 등장하는 "파이썬 기초"를 제거하세요.
-리스트의 마지막 책을 빼내어 변수 last_book에 저장하고, 이 책(last_book)을 출력하세요.
-책 목록을 알파벳 순으로 정렬하세요.
-정렬된 목록을 역순으로 뒤집으세요.
-수정된 books 리스트를 출력하세요.

# 4단계: 도서 목록 분석하기
-슬라이싱을 사용하여 books 리스트의 처음 3권을 top_books라는 새 리스트에 저장하세요.
-books 리스트에서 2번째부터 5번째까지의 책들을 역순으로 reversed_selection이라는 새 리스트에 저장하세요.
-top_books와 reversed_selection을 출력하세요.
-books 리스트를 완전히 비우고 출력하세요.
'''

# 1단계
books = [
    "파이썬 기초",
    "데이터 과학 입문",
    "알고리즘의 이해",
    "머신러닝 실전",
    "파이썬 기초",
]
print(books)


# 2단계
a = books.count("파이썬 기초")
print(f"파이썬 기초가 {a}권 있습니다.")

books.append("웹 개발의 시작")
print(f"책 추가후: {books}")

books.insert(2, "데이터베이스 설계")
print(f"책 삽입 후: {books}")

new_books = ["인공지는 개론", "클라우드 컴퓨팅"]
b = new_books.copy()
books.extend(new_books) ## append와 다르다 (잊지 X)
print(f"여러책 추가 후: {books}")


# 3단계
books.remove("파이썬 기초")
print(f"파이썬 기초 제거 후: {books}")

last_book = books.pop()
print(f"빼낸 마지막 책: {last_book}")
print(f"책 빼낸 후: {books}")

sorted(books, reverse=False)
print(f"역순 정렬 후: {books}")


# 4단계
top_books = books[0:3] # books[:3] 도 가능
print(f"처음 3권: {top_books}")

reversed_selection = list(reversed(books[1:5]))
# books[1:5][::-1]
print(f"2~5번째 책 역순: {reversed_selection}")

books.clear()
print(f"리스트 비운 후: {books}")
