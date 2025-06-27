from django import forms
from .models import Comment

# forms.Form
#  - GET 요청 : 지정된 필드 구성으로 유저에게 입력폼 HTML 생성/응답
#  - POST 요청 : 지정된 필드 구성으로 유저로부터 제출(submit)받은 값들에 대한
#               유효성 검사를 수행
                # -> valid : 유효성 검사에 통과한 값들을 dict 타입으로 제공받고, 다른 주소로 이동
                # -> invalid : 유저에게 다시 오류 내역이 포함된 HTML 생성/응답

# Form:모델처럼 유저로부터 입력받을 값에 대한 필드 구성을 하나하나 구성해야 한다
# class CommentForm(forms.Form):
#     content = forms.CharField()

# ModelForm
#  - 지정 모델의 지정 필드들의 정보를 읽어와서
#    폼 필드 구성을 자동으로 수행해준다.
#  - 모델 구성이 바뀌면, 알아서 폼 필드 구성도 변경된다.(서버 재시작)
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # 전체 필드 지정할때에는 []를 쓰지 X
        # fields = "__all__"

        # 유저로부터 입력받을 필드만 명시.
        fields = ["content"] 