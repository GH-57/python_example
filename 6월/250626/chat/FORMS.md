from random import choices

# 모델 폼을 안 썼다면

from django import forms

# 유저로부터 입력받을 폼 필드 구성을
# 아래와 같이 직접 해야만 합니다.
class PuzzleRoomForm(forms.Form):
    image_file = forms.ImageField()
    level = forms.ChoiceField(
        choices=[
            (3, 'Level 3'),
            (4, 'Level 4'),
            (5, 'Level 5'),
        ]
    )

# 그런데, 데이터베이스에 저장되는 컬럼 구성 그대로
# 모델 구성 그대로 입력을 받고자 한다면. 모델폼
class PuzzleRoomForm(forms.ModelForm):
    class Meta:
        model = PuzzleRoom
        fields = ["image_file", "level"]

 ModelForm은 코드를 생성해주는 기능