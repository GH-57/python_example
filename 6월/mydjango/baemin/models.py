from django.db import models

# 1측
class Shop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # photo = models.FileField() # 모든 파일 포맹 저장 가능
    photo = models.ImageField() # 이미지만 받는다
    address = models.CharField(max_length=200, blank=True) # 주소 필드 추가
    phone_number = models.CharField(max_length=20, blank=True) # 전화번호 필드 추가
    opening_time = models.TimeField(blank=True, null=True) # 영업 시작 시간 필드 추가
    closing_time = models.TimeField(blank=True, null=True) # 영업 종료 시간 필드 추가


# N측에 1에 대한 외래키 필드를 추가
class Review(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    content = models.TextField()
    # rating = models.IntegerField # 음수/양수 다 담을 수 있다.
    # rating = models.PositiveIntegerField # 양수만 담을 수 있다. 담을 수 있는 양수의 범위 2배 커짐
    rating = models.PositiveSmallIntegerField()

    # 1 bit => 0과 1을 표현 => 값을 2가지 표현 가능
    # 2 bit => 2 ** 2 => 4가지 표현 가능
    # 3 bit => 8가지
    # 4 bit => 16, 5 => 32, 6 => 64, 7 => 128, 8 => 256가지 숫자 표현 가능
    # 1 byte <= 8 bit

    # 일반적인 숫자 변수는 4바이트 