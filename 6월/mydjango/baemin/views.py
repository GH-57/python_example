from django.contrib import messages
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Shop, Review
from .forms import ReviewForm

# 클래스를 통해서 새로운 뷰 함수를 생성
shop_list = ListView.as_view(
    model = Shop,
    paginate_by = 5,
)


# 최신의 가게 목록 페이지를 보여줄 것이다
# - 최신의 데이터는 DB안에 있다, 그러니 매번 DB 조회를 할 것이다
# def shop_list(request):
#     # DB에서 baemin_shop 테이블의 모든 레코드를 조회할 준비
#     # (아직 모든 데이터를 가져오지 않았다.)
#     qs = Shop.objects.all() # QuerySet
#     # qs = qs.order_by('-id') # 매번 정렬을 지정할 수도 있지만.

#     # page = 2
#     page = int(request.GET.get("page", 1)) # 쿼리스트링 값은 기본적으로 문자열 타입
#     paginate_by = 5 # 1페이지를 몇 개씩 끊을 것인가?

#     # qs = qs[0:5] # 1페이지: 처음 5개 (리스트/문자열의 슬라이싱 문법과 동일)
#     # qs = qs[5:10] # 2페이지
#     # qs = qs[10:15] # 3페이지

#     start_index = (page - 1) * paginate_by
#     end_index = page * paginate_by
#     qs = qs[start_index: end_index]


#     return render(request,
#                 template_name="baemin/shop_list.html",
#                 context={
#                     "shop_list": qs,
#                 })


# TODO: baemin/shop_list.html 템플릿을 만들어보기, 하얀배경도 ok. chatgpt OK

def shop_detail(request, pk):
    # DB에서 조회했습니다.
    # shop = Shop.objects.get(pk=pk) # 이 필드명 지정이 좀 더 정확한 네이밍.
    # shop = Shop.objects.get(id=pk)  # 위와 동일한 동작
    shop = get_object_or_404(Shop, pk=pk)

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



def review_new(request, shop_pk):
    # shop = Shop.objects.get(pk=shop_pk) 
    ## form 시작할 때, 지정 pk의 Shop의 존재 유무 확인
    shop = get_object_or_404(Shop, pk=shop_pk)
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

def review_edit(request, shop_pk, pk):
    # 모델클래스 .object => Model Manager
    # .all
    # .get
    # .filter
    # .exclude
    # .order_by

    # 지정 조건의 레코드가 DB에 없을 때 Review.DoesNotExist 예외가 발생
    # try:
    #     review = Review.objects.get(pk=pk) # 지정 조건의 레코드가 DB가 1개 있어야 한다
    # except Review.DoesNotExist:
    #     raise Http404
    
    ## 위 코드와 같은 기능 
    review = get_object_or_404(Review, pk=pk)

    if request.method == "GET":
        form = ReviewForm(instance=review)

    else:
        form = ReviewForm(instance=review, data=request.POST, files=request.FILES)
        if form.is_valid():
            # 리뷰 수정시에는 ReviewForm 클래스 안에서 정의된 필드에 대해서만 저장되어도 O
            form.save()
            messages.success(request, "리뷰가 수정되었습니다. ;)")

            shop_url = f"/baemin/{shop_pk}/"
            return redirect(shop_url)


    return render(
        request,
        template_name="baemin/review_form.html",
        context={"form": form},
    )


# 장고 스타일의 삭제 방식
#  1) GET 요청: 삭제를 요청했을 때 -> 확인 과정을 거친다. (정말 삭제하시겠습니까?)
#  2) POST 요청: 삭제 확인 (confirm) -> 삭제를 합니다.
def review_delete(request: HttpRequest, shop_pk, pk) -> HttpResponse:
    if request.method == "GET":
        return render(request, 
                      "baemin/review_confirm_delete.html")
    
    review = get_object_or_404(Review, pk=pk)
    review.delete() # DB에서 호출 즉시 삭제된다.

    messages.success(request, "지정 리뷰를 삭제했습니다.")

    shop_url = f"/baemin/{shop_pk}/"
    return redirect(shop_url)
        

    # TODO: shop detail 페이지에 직접 리뷰 쓰기 폼 노출하기
    # TODO: 페이지 전환없이 리뷰 삭제 해보기. (JS 버전 vs htmx 버전)