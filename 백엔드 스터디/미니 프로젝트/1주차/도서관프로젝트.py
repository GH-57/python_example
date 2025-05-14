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
        if 0 <= choice <= 10: # 0~10 숫자 골랐을 때
            return choice
        else: # 그 이외의 숫자 골랐을 때
            print("오류: 0부터 10까지의 숫자만 입력해주세요.")
        return 0 # -1은 아무 일도 일어나지 않게 하는 것
    else: # 숫자 이외의 문자 골랐을 때
        print("오류: 숫자만 입력해주세요.")
    return 0




def main():
    '''
    메뉴를 반복하여 출력하고 
    사용자가 종료할 때까지 프로그램을 실행합니다
    
    '''
    # 프로그램 시작 메시지 출력
    print("도서관 관리 시스템에 오신 것을 환영합니다!")
    
    while True:
        choice = menu()

menu()