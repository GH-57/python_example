from django import forms
from chat.models import PuzzleRoom

# form.Form: 입력 HTML Form과의 인터페이스
#   - 입력 폼 HMTL 생성
#   - 유저가 입력한 값에 대해서 유효성 검사
#   - 유효성 검사에 통과한 값들을 정리해서.cleaned_datea 사전으로 제공.
# models.Model: 데이터베이스와의 인터페이스

# forms.ModelForm



# 상속 (Inheritance) 문법
class PuzzleRoomForm(forms.ModelForm):
    class Meta:
        model = PuzzleRoom
        # 지정 모델의 모든 모델 필드 내역을 읽어와서, 폼 필드 구성 하기(자동)
        fields = "__all__"


# if 수정 시에는 레벨만 수정토록 허용하고 싶다.  
class PuzzleRoomEditForm(forms.ModelForm):
    class Meta:
        model = PuzzleRoom
        # 지정 모델의 지정 필드 내역만 읽어와서, 폼 필드 구성허가 (자동)
        # - 유저에게 level 필드만 입력 필드 제공, 값을 변경할 수 있다.
        # - 지정 필드에 대해서만 수정 허용
        fields = ["level"]