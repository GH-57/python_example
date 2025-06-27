# 1. Django 모델에서 외래키(ForeignKey) 관계 설정 시 on_delete=models.CASCADE의 의미는?
# - 참조되는 객체가 삭제될 때 관련된 모든 객체도 함께 삭제

# 2. Django View에서 form.save(commit=False)의 목적은?
# - 모델 인스턴스만 생성하고 아직 DB에 저장하지 않기 위해

# 3. Django 모델 필드에서 choices 옵션의 역할은?
# - 선택 가능한 값들을 미리 정의하여 제한한다.

# 4. Django ListView와 같은 Class Based View의 주요 장점은?
# - 반복적인 코드를 줄이고 일관된 패턴을 제공한다.

# 5. Django에서 makemigrations와 migrate 명령어의 차이는?
# - makemigrations는 마이그레이션 파일 생성, migrate는 실제 DB에 적용

# 6(X). Django의 static 파일과 media 파일의 차이점은?
# - static은 개발자가 작성한 파일, media는 사용자가 업로드한 파일

# 7. Django 템플릿에서 {% csrf_token %}의 목적은?
# - CSRF(Cross-Site Request Forgery) 공격을 방지하기 위해

# 8. CSRF 공격이 무엇인가요?
# - 웹 사이트가 사용자의 의도와는 무관하게 악의적인 요청을 수행하도록 만드는 공격 방법