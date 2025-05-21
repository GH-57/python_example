import json # json파일 읽기 및 쓰기
import os # 파일 존재 여부 확인
from datetime import datetime, timedelta # 날짜 비교 및 처리


class HistoryManager:
    '''
    * 거래내역 조회 기능을 관리하는 클래스
    -입출금 및 이체 내역 확인
    -날짜별 필터링
    -최근 5건 내역 조회 
    -CSV 형식으로 내보내기 기능
    '''
        # 파일 경로 설정
    def __init__(self, history_file="history.json",             export_file="export_history.json"):
        """
        HistoryManager 클래스 초기화
        
        Args: #아규먼츠
            history_file (str): 거래 내역이 저장된 JSON 파일 경로
            export_file (str): 내보내기할 CSV 파일 경로
        """
        self.history_file = history_file
        self.export_file = export_file
        
        # 파일이 없을 경우 빈 JSON 파일 생성
        if not os.path.exists(self.history_file): # file이 없다면..
            with open(self.history_file, 'w', encoding='utf-8') as f:
                json.dump({}, f, ensure_ascii=False, indent=4)


    def _load_history(self):
        pass
        # 거래내역 파일 로드


    def get_recent_history(self, account_no, count=5):
        pass

    def serch_by_date(self, account_no, start_date, end_date):
        pass

    def export_csv(self, account_no):
        pass