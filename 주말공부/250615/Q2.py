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


@app.post("/analyze-text")
async def analyze_text_file(file: UploadFile = File(...)):
    # 여기에 코드 작성
    if not file.content_type.startswith('text/'):
        raise HTTPException(status_code=400, detail="텍스트 파일만 업로드 가능합니다")
    
    try:
        # 파일 내용 읽기
        content = await file.read()
        text = content.decode('utf-8')
        
        # 단어 추출 (영문 기준)
        words = re.findall(r'\w+', text.lower())
        
        # 단어 개수 세기
        word_counts = Counter(words)
        
        # 통계 계산
        total_words = len(words)
        unique_words = len(word_counts)
        top_words = word_counts.most_common(5)
        
        return {
            "filename": file.filename,
            "total_words": total_words,
            "unique_words": unique_words,
            "top_words": top_words
        }
        
    except UnicodeDecodeError:
        raise HTTPException(status_code=400, detail="파일을 읽을 수 없습니다. UTF-8 인코딩 파일을 업로드해주세요")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"파일 처리 중 오류가 발생했습니다: {str(e)}")


# 힌트: 
# - await file.read() 로 파일 내용 읽기
# - re.findall(r'\w+', text.lower()) 로 단어 추출
# - Counter 사용해서 개수 세기

