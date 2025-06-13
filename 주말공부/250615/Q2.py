# 텍스트 파일 업로드해서 단어 개수 세는 API
from fastapi import FastAPI, UploadFile, File, HTTPException
from collections import Counter
import re

app = FastAPI()

# 구현할 엔드포인트:
# POST /analyze-text
# - 텍스트 파일 업로드 받기
# - 파일 내용을 읽어서 단어 개수 세기
# - 가장 많이 나온 단어 TOP 5 리턴
# 응답 예시: {
#   "total_words": 100,
#   "unique_words": 50,
#   "top_words": [["the", 10], ["and", 8], ["is", 6], ["a", 5], ["to", 4]]
# }

async def analyze_text_file(file: UploadFile = File(...)):
    # 여기에 코드 작성
    pass

# 힌트: 
# - await file.read() 로 파일 내용 읽기
# - re.findall(r'\w+', text.lower()) 로 단어 추출
# - Counter 사용해서 개수 세기