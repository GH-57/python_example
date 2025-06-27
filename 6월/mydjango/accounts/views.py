from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup(request):
    if request.method == "GET":
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save() # 회원가입 완료! 지정 유저 레코드 DB에 저장
            # 회원가입을 했으니, 로그인 페이지로 이동하는 것이 자연스럽다.
            return redirect("/accounts/login/") # 아직 미구현
        
    return render(request, "accounts/signup_form.html", {
        "form": form,
        })
