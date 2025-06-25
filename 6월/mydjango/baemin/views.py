from django.shortcuts import render, redirect
from .models import Shop, Review
from blog.forms import CommentForm
from blog.models import Comment

# 최신의 가게 목록 페이지를 보여줄 것이다
# - 최신의 데이터는 DB안에 있다, 그러니 매번 DB 조회를 할 것이다
def shop_list(request):
    # DB에서 baemin_shop 테이블의 모든 레코드를 조회할 준비
    # (아직 모든 데이터를 가져오지 않았다.)
    qs = Shop.objects.all() # QuerySet

    return render(request,
                  template_name="baemin/shop_list.html",
                  context={
                    "shop_list": qs,
                  })


# TODO: baemin/shop_list.html 템플릿을 만들어보기, 하얀배경도 ok. chatgpt OK

def shop_detail(request, pk):
    # DB에서 조회했습니다.
    shop = Shop.objects.get(pk=pk) # 이 필드명 지정이 좀 더 정확한 네이밍.
    # shop = Shop.objects.get(id=pk)  # 위와 동일한 동작

    # 전체(모든 Shop) 리뷰 데이터를 가져올 준비.
    review_qs = Review.objects.all()
    # 특정 shop의 리뷰 데이터를 가져올 준비 (가져올 범위가 좁혀집니다.)
    review_qs = review_qs.filter(shop=shop)

    return render(
        request,
        template_name="baemin/shop_detail.html",
        context={"shop": shop, "review_list": review_qs},
    )


# TODO: baemin/shop_detail.html 템플릿을 만들어보기.

from .forms import ReviewForm

def review_new(request, shop_pk):
    if request.method == "GET":
        form = ReviewForm()

    else:
        form = ReviewForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            unsaved_review: Comment = form.save(commit=False)
            unsaved_review.shop = Shop.objects.get(id=shop_pk) ## 
            unsaved_review.save()

            shop_url = f"/baemin/{shop_pk}/"
            return redirect(shop_url)



        # TODO: ...

    return render(
        request,
        template_name="baemin/review_form.html",
        context={"form": form},
    )