import json
import datetime


class HistoryManager:
    '''
    거래내역 조회 기능을 관리하는 클래스
    -입출금 및 이체 내역 확인
    -날짜별 필터링
    -최근 5건 내역 조회 
    -CSV 형식으로 내보내기 기능
    '''
    def __init__(self, ):
    pass

    def get_all_history(self, account_no):
        pass

    def get_recent_history(self, account_no, count=5):
        pass

    def serch_by_date(self, account_no, start_date, end_date):
        pass

    def export_csv(self, account_no):
        pass