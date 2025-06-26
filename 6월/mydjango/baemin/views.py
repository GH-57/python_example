from django.contrib import messages
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

    # 정렬(sort) : 정렬 기준으로 2개 이상 두 수 있다
    # 각 정렬은 오름차순, 내림차순을 지정가능
    # 가급적 기준 정렬은 1개만 지정하기를 권장
    #  - 데이터가 적으면 (몇천개) 아무 상관없다
    #  - 데이터베이스 정렬을 요청받으면, 정렬을 모두 한 후에 정렬된 목록을 응답한다.
    #    정렬 기준이 여러개면, 여러번 하면 그만큼 시간이 오래 걸린다
    #  - 대개 정렬은 1개 기준이면 충분

    # 전체(모든 Shop) 리뷰 데이터를 가져올 준비.
    review_qs = Review.objects.all()
    # 특정 shop의 리뷰 데이터를 가져올 준비 (가져올 범위가 좁혀집니다.)
    review_qs = review_qs.filter(shop=shop)

    # 정렬을 지정하지 않아도 출력은 되는데? 지정하지 않으면 오름차순? -> X
    #  - 저장된 순서대로 조회될 뿐이다. (마치 오름차순처럼 보일 뿐)
    #  - 조회할 때마다 다른 순서로 조회가 될 수도 있다.

    # 정렬을 지정하면, 항상 일관된 순서로 조회가 된다
    # review_qs = review_qs.order_by("-id") # id 필드 역순 (내림차순)
    # review_qs = review_qs.order_by("id")  # id 필드 역순 (오름차순)


    return render(
        request,
        template_name="baemin/shop_detail.html",
        context={"shop": shop, "review_list": review_qs},
    )


# TODO: baemin/shop_detail.html 템플릿을 만들어보기.

from .forms import ReviewForm

def review_new(request, shop_pk):
    shop = Shop.objects.get(pk=shop_pk) # form 시작할 때, 지정 pk의 Shop의 존재 유무 확인
    if request.method == "GET":
        form = ReviewForm()

    else:
        form = ReviewForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            unsaved_review: Comment = form.save(commit=False)
            unsaved_review.shop = Shop.objects.get(id=shop_pk) ## 
            unsaved_review.save()

            # 한국어를 쓰는 사람을 대상으로만 하는 서비스니까, 메시지는 한국어로 쓴다
            # 만약 영어 등 다국어를 지원해야한다면, 메시지를 쓰는 방법이 조금 달라요.
            messages.success(request, "고객님의 리뷰에 감사드립니다. ;)")

            shop_url = f"/baemin/{shop_pk}/"
            return redirect(shop_url)


    return render(
        request,
        template_name="baemin/review_form.html",
        context={"form": form},
    )