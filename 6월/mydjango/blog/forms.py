from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # 전체 필드 지정할때에는 []를 쓰지 X
        fields = "__all__"