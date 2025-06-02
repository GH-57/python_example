"""
도서관 관리 시스템
- 로그인/회원가입 기능
- 도서 관리(보기, 추가, 삭제)
- 도서 대여/반납/연장
- 도서 검색 및 메뉴 인터페이스
"""

# 전역 변수 선언
current_user = ["abc123"]  # 현재 로그인한 사용자 정보 (리스트 형태로 관리)
books = [
    {"title": "원피스", "rented_by": "대여가능"},  # 책 목록 (대여 가능한 책)
    {"title": "aa", "rented_by": None}  # 대여 가능한 책 (None은 대여 가능 상태를 의미)
]


class UserSystem:
    """사용자 계정 관리 클래스: 회원 가입, 로그인, 로그아웃 기능 제공"""
    
    def __init__(self):
        """사용자 시스템 초기화 - 사용자 정보를 저장할 딕셔너리 생성"""
        self.users = {}  # 사용자 정보를 저장하는 딕셔너리 {아이디: 비밀번호}

    def signup(self):
        """
        회원가입 기능
        - 사용자에게 아이디와 비밀번호를 입력받아 계정 생성
        - 중복된 아이디는 생성 불가
        """
        while True:
            username = input("아이디를 입력하세요: ")
            if username in self.users:
                print("❗ 이미 존재하는 아이디입니다.")
            else:
                break
        password = input("비밀번호를 입력하세요: ")
        self.users[username] = password
        print(f"🎉 {username}님, 회원가입이 완료되었습니다!")
        return username

    def login(self):
        """
        로그인 기능
        - 사용자에게 아이디와 비밀번호를 입력받아 인증
        - 성공 시 사용자 아이디 반환, 실패 시 None 반환
        """
        username = input("아이디를 입력하세요: ")
        password = input("비밀번호를 입력하세요: ")
        if username in self.users and self.users[username] == password:
            print(f"✅ {username}님, 로그인 성공!✅")
            return username
        else:
            print("❌ 아이디 또는 비밀번호가 올바르지 않습니다.❌")
            return None


class Library:
    """도서관 관리 클래스: 도서 목록 조회, 대여/반납, 로그아웃 기능"""
    
    def __init__(self):
        """도서관 시스템 초기화"""
        self.books = []  # 도서 목록
        self.current_user = None  # 현재 로그인한 사용자
        
    def logout(self, current_user):
        """
        로그아웃 기능
        - 사용자에게 로그아웃 여부 확인 후 처리
        - 로그아웃 성공 시 True, 취소 시 False 반환
        """
        confirm = input("로그아웃 하시겠습니까? [1.네 / 2.아니요] ")

        if confirm == "1":
            print("로그아웃 되었습니다.")
            current_user.clear()  # 현재 사용자 정보 초기화
            return True
        elif confirm == "2":  # 올바른 선택지 번호로 수정
            print("로그아웃이 취소되었습니다.")
            return False
        else:
            print("잘못된 입력입니다. 1 또는 2를 입력해주세요.")  # 안내 메시지 수정
            return False

    def show_books(self):
        """
        도서 목록 표시 기능
        - 모든 도서의 제목과 대여 상태를 출력
        """
        for num, book in enumerate(books, 1):
            print(f"{num}. {book['title']} / {book['rented_by']}")

    def extend_books(self):
        """
        도서 대여 연장 기능
        - 현재 로그인한 사용자가 대여한 책의 대여 기간 연장
        - 연장할 책을 선택받아 처리
        """
        if self.current_user is None:  # 로그인 정보가 없을 때
            print("로그인 후 이용해주세요.")
            return

        # 로그인 유저의 대여한 책 조회
        users_books = [
            (i, book) for i, book in enumerate(self.books)
            if book["rented_by"] == self.current_user
        ]

        # 대여 중인 책이 없을 때
        if not users_books:
            print("대여 중인 책이 없습니다.")
            return
        
        # 대여 중인 책이 있을 때, 목록으로 출력
        print("[대여 중인 책 목록]")
        for i, book in users_books:
            print(f"{i}. {book['title']}")

        # 연장할 책 번호 입력받기
        try:
            book_index = int(input("연장할 책 번호를 입력하세요: "))
        except ValueError:  # 숫자가 아닌 문자를 입력했을 때, 오류로 걸러냄
            print("숫자를 입력해주세요.")
            return
        
        # 유효한 책 번호 검사 
        if book_index < 0 or book_index >= len(self.books):
            print("존재하지 않는 책 번호입니다.")
            return
        
        # 로그인한 유저가 대여한 책인지 확인
        if self.books[book_index]["rented_by"] != self.current_user:
            print("대여한 책이 아닙니다.")
            return
        
        # 모든 조건을 만족할 때
        print(f"{self.books[book_index]['title']} 연장 완료")

    def search_books(self):
        """
        도서 검색 기능
        - 키워드를 입력받아 제목에 해당 키워드가 포함된 도서 검색
        - 검색 결과의 도서 제목과 대여 상태 출력
        """
        if self.current_user is None:  # 로그인 유저 값이 None일 때
            print("로그인 후 이용해주세요.")
            return

        if not self.books:  # 등록된 도서가 없을 때
            print("도서 목록이 비어있습니다.")
            return
        
        keyword = input("검색할 책 제목 또는 키워드를 입력하세요: ").lower()  # 소문자 변환(영어책)
        found = False  # 검색 결과가 하나라도 있으면 True로 바뀜

        print("[검색 결과]")
        for i, book in enumerate(self.books):  # 책 목록을 확인하며 제목에 키워드가 있는지 확인
            if keyword in book["title"].lower():  # 제목에 키워드가 있으면
                status = "대여 가능" if book["rented_by"] is None else f"대여중({book['rented_by']})"  # status 값이 None이면 "대여 가능", 아니면 "대여중(빌린사람)"
                print(f"{i}. {book['title']} - {status}")  # 책 번호. 제목 - 대여 가능 여부
                found = True  # 책이 검색 되었으니 True

        if not found:
            print("검색된 책이 없습니다.")  # 반복문으로 책 목록을 돌고, 일치하는 키워드가 없으면 메세지 출력


class BookManager:
    """도서 관리 클래스: 도서 추가, 삭제 기능"""
    
    def __init__(self):
        """도서 관리자 초기화"""
        self.books = {}  # 도서 정보 저장 딕셔너리 {제목: 번호}

    def add_book(self):
        """
        도서 추가 기능
        - 제목과 번호를 입력받아 도서 목록에 추가
        """
        book_title = input("책 제목을 입력해주세요: ")
        book_number = input("책 번호를 입력해주세요: ")
        self.books[book_title] = book_number
        print(f"'{book_title}' 도서가 등록되었습니다.")

    def delete_book(self):
        """
        도서 삭제 기능
        - 책 번호를 입력받아 해당 도서 삭제
        - 존재하지 않는 번호 입력 시 오류 메시지 출력
        """
        title_to_delete = None
        book_number = input("책 번호를 입력해주세요: ")

        # 입력받은 번호와 일치하는 책 찾기
        for title, number in self.books.items():
            if book_number == number:
                title_to_delete = title 
                break 

        # 해당 번호의 책이 있으면 삭제
        if title_to_delete in self.books:
            self.books.pop(title_to_delete)
            print("도서가 삭제되었습니다.")
        else:
            print("존재하지 않는 책 번호입니다.")


class Book:
    """개별 도서 클래스: 도서 속성과 대여/반납 기능"""
    
    def __init__(self, book_id, title):
        """
        도서 객체 초기화
        
        Args:
            book_id (str): 도서 ID
            title (str): 도서 제목
        """
        self.book_id = book_id
        self.title = title
        self.rented_by = None  # 대여자(User 객체)
    
    def rent_book(self, user):
        """
        도서 대여 기능
        
        Args:
            user: 대여하려는 사용자 객체
        """
        if self.rented_by is None:  # rented_by가 None일 때 대여가능
            self.rented_by = user  # 대여자 등록
            print(f"{self.title}책이 {user.name}님께 대여되었습니다.")
        else:
            print("대여 중")

    def return_book(self, user):
        """
        도서 반납 기능
        
        Args:
            user: 반납하려는 사용자 객체
        """
        if self.rented_by == user:  # rented_by가 사용자일 때만 반납가능
            self.rented_by = None  # 반납 처리
            print(f"{self.title} 책이 반납되었습니다.")
        else:
            print("반납할 수 없습니다. 이 책은 당신이 대여한 것이 아닙니다.")


def menu():
    """
    사용자에게 도서관 시스템 메뉴를 출력하고 
    선택한 메뉴 번호를 반환하는 함수
    
    Returns:
        int: 사용자가 선택한 메뉴 번호 (오류 발생 시 -1 반환)
    """
    print("\n" + "=" * 40)
    print(" " * 10 + "[도서관 시스템 메뉴]")
    print("=" * 40)
    print("1. 도서 목록 보기")
    print("2. 대출 중인 도서 목록 보기")
    print("3. 책 추가하기")
    print("4. 책 삭제하기")
    print("5. 책 대여하기")
    print("6. 책 반납하기")
    print("7. 대여 연장하기")
    print("8. 원하는 도서 신청하기")
    print("9. 내 대출 목록 보기")
    print("10. 책 검색하기")
    print("0. 로그아웃 또는 종료")
    print("=" * 40)
    
    # 사용자의 메뉴 선택을 입력받음 (if문과 isdigit 메서드 활용)
    user_input = input("원하는 메뉴를 선택하세요 (0-10): ")
    if user_input.isdigit():
        choice = int(user_input)
        if 0 <= choice <= 10:  # 0~10 숫자 골랐을 때
            return choice
        else:  # 그 이외의 숫자 골랐을 때
            print("오류: 0부터 10까지의 숫자만 입력해주세요.")
            return -1
    else:  # 숫자 이외의 문자를 입력했을 때
        print("오류: 숫자만 입력해주세요.")
        return -1


def main():
    """
    메인 함수: 프로그램의 실행 흐름을 제어
    - 메뉴를 반복하여 출력하고 
    - 사용자가 종료할 때까지 프로그램을 실행
    """
    # 프로그램 시작 메시지 출력
    print("도서관 관리 시스템에 오신 것을 환영합니다!")
    
    # 시스템 객체 초기화
    user_system = UserSystem()
    library = Library()
    book_manager = BookManager()
    
    while True:
        choice = menu()  # 메뉴출력 및 선택 받기

        # 메뉴 선택에 따른 실행
        if choice == 0:
            print("\n프로그램을 종료합니다. 이용해 주셔서 감사합니다 :)")
            break  # 로그아웃 하면 반복문 종료

        elif choice == 1:
            print("\n도서 목록을 불러오는 중입니다...")
            library.show_books()
        
        elif choice == 2:
            print("\n대출 중인 도서 목록을 불러오는 중입니다...")
            # 대출 중인 도서만 필터링하여 보여줄 수 있는 기능 추가 필요
            # 아직 구현되지 않은 기능

        elif choice == 3:
            print("\n새로운 책을 추가합니다...")
            book_manager.add_book()

        elif choice == 4:
            print("\n책을 삭제합니다...")
            book_manager.delete_book()

        elif choice == 5:
            print("\n책을 대여합니다...")
            # 책 대여 기능은 Book 클래스에 있지만 실제 연결 로직 필요
            # 아직 구현되지 않은 기능

        elif choice == 6:
            print("\n책을 반납합니다...")
            # 책 반납 기능은 Book 클래스에 있지만 실제 연결 로직 필요
            # 아직 구현되지 않은 기능

        elif choice == 7:
            print("\n대여 기간을 연장합니다...")
            library.extend_books()

        elif choice == 8:
            print("\n도서 신청을 불러옵니다...")
            # 도서 신청 기능 아직 구현되지 않음

        elif choice == 9:
            print("\n내 대출 목록을 불러옵니다...")
            # 내 대출 목록 기능 아직 구현되지 않음

        elif choice == 10:
            print("\n책을 검색합니다...")
            library.search_books()

        else:
            print("\n올바른 메뉴를 선택 해주세요")

        input("\n계속하려면 Enter키를 누르세요...")


# 프로그램 실행
if __name__ == "__main__":
    main()
