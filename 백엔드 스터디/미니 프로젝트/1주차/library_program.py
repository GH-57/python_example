## claude로 짜본 도서관 목록
# 설명할수 있어야 한다.

def menu():
    """
    사용자에게 도서관 시스템 메뉴를 출력하고, 선택한 메뉴 번호를 반환하는 함수
    
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
    
    # 사용자의 메뉴 선택을 입력받음
    try:
        choice = int(input("원하는 메뉴를 선택하세요 (0-10): "))
        # 메뉴 범위 확인 (0부터 10까지만 유효)
        if 0 <= choice <= 10:
            return choice
        else:
            print("오류: 0부터 10까지의 숫자만 입력해주세요.")
            return -1
    except ValueError:
        # 숫자가 아닌 값을 입력한 경우
        print("오류: 숫자만 입력해주세요.")
        return -1


def main():
    """
    도서관 프로그램의 메인 함수로, 전체적인 프로그램 흐름을 제어합니다.
    사용자가 종료를 선택할 때까지 메뉴를 반복해서 출력하고 해당 기능을 실행합니다.
    """
    # 프로그램 시작 메시지 출력
    print("\n도서관 관리 시스템에 오신 것을 환영합니다!")
    
    while True:
        # 메뉴 출력 및 사용자 선택 받기
        choice = menu()
        
        # 메뉴 선택에 따른 기능 실행
        if choice == 0:
            print("\n프로그램을 종료합니다. 이용해 주셔서 감사합니다.")
            break  # 반복문 종료
        
        elif choice == 1:
            print("\n도서 목록을 출력합니다...")
            # view_books() 함수 호출 - 다른 팀원이 구현할 부분
            
        elif choice == 2:
            print("\n대출 중인 도서 목록을 출력합니다...")
            # view_borrowed_books() 함수 호출 - 다른 팀원이 구현할 부분
            
        elif choice == 3:
            print("\n새로운 책을 추가합니다...")
            # add_book() 함수 호출 - 다른 팀원이 구현할 부분
            
        elif choice == 4:
            print("\n책을 삭제합니다...")
            # delete_book() 함수 호출 - 다른 팀원이 구현할 부분
            
        elif choice == 5:
            print("\n책을 대여합니다...")
            # borrow_book() 함수 호출 - 다른 팀원이 구현할 부분
            
        elif choice == 6:
            print("\n책을 반납합니다...")
            # return_book() 함수 호출 - 다른 팀원이 구현할 부분
            
        elif choice == 7:
            print("\n대여 기간을 연장합니다...")
            # extend_rental() 함수 호출 - 다른 팀원이 구현할 부분
            
        elif choice == 8:
            print("\n원하는 도서를 신청합니다...")
            # request_book() 함수 호출 - 다른 팀원이 구현할 부분
            
        elif choice == 9:
            print("\n내 대출 목록을 출력합니다...")
            # view_my_rentals() 함수 호출 - 다른 팀원이 구현할 부분
            
        elif choice == 10:
            print("\n책을 검색합니다...")
            # search_book() 함수 호출 - 다른 팀원이 구현할 부분
            
        # 사용자가 잘못된 입력을 한 경우(-1이 반환된 경우)에는 아무 작업도 하지 않음
        # 다음 반복에서 다시 메뉴가 표시됨
            
        # 작업 완료 후 계속하기 위한 대기
        input("\n계속하려면 Enter 키를 누르세요...")


# 프로그램 시작점
if __name__ == "__main__":
    main()
