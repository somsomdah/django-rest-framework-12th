from django.db import models
from django.contrib.auth.models import User

# [제약조건]
# 1. 1:1과 1:n의 관계 포함
# 2. 각 모델에 필드 최소 3개 이상 포함
# 3. 서비스 관련 모델 3개 이상 + 유저 모델 1개 구현 (단, 유저는 필수 아님)

#유저 모델
#새로운 모델 생성해서 기존의 User Model과 OneToOne 으로 연결하는 방식
class Customer(models.Model) :
    #User 모델의 username 필드를 Customer의 PK로 사용하려면 어떻게 해야하지?
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)#User 모델의 PK 값을 자동 저장해주나..?
    name = models.CharField(max_length=50)
    addr = models.CharField(max_length=50)#얼만큼 줘야 할까..?
    membership = models.CharField(max_length=10)
    #적립금..?

#서비스 관련 모델1) 상품
#모든 항목 not NULL
class Product(models.Model) :
    id = models.CharField(max_length=100, primary_key=True)#PK 지정, integerfield로 할까..? autofield 쓰려고
    type = models.CharField(max_length=25)
    price = models.IntegerField()#필수 옵션 없나..?
    color = models.CharField(max_length=10)
    size = models.CharField(max_length=3)
    #+적립금..?

#서비스 관련 모델2) 주문 (유저모델과 1을 연결할 mapping table), N:M 관계 아직 못함..
class Order(models.Model) :
    order_number = models.IntegerField(primary_key=True)#PK 지정
    order_quantity = models.IntegerField()
    order_addr = models.CharField(max_length=50)
    date_of_order = models.DateTimeField(auto_now=False)#저장될 때마다 자동으로 필드에 현재 시간 설정, 이게 맞나..?
    #+FK :고객ID
    #+FK :상품ID

#서비스 관련 모델3) 장바구니 (유저 모델과 1:1 관계)
class Cart(models.Model) :
    total_quantity = models.IntegerField()
    total_payment = models.IntegerField()
    #+고객ID: PK 이자 FK
    customer = models.OneToOneField(Customer, primary_key=True, on_delete=models.CASCADE)

#서비스 관련 모델4) 상품 리뷰
class Reviews(models.Model) :
    id = models.BigAutoField(primary_key=True)#PK 지정
    rating = models.DecimalField(max_digits=2, decimal_places=1)#숫자 최대 자릿수 2, 소수점 1자리 수까지 저장
    content = models.TextField()
    #+고객ID : FK
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    #+상품ID : FK
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)#review_id 값 반환

#서비스 관련 모델5) 상품 문의
class QnA(models.Model) :
    id = models.BigAutoField(primary_key=True)#PK 지정
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_of_QnA = models.DateTimeField(auto_now=False)
    #+고객ID: FK
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    #+상품ID: FK
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

#서비스 관련 모델6) 문의 답변
class Answer(models.Model) :
    id = models.BigAutoField(primary_key=True)#PK 지정
    writer = models.CharField(max_length=5, default="Admin")#default 값 = 관리자로 지정
    date_of_ans = models.DateTimeField(auto_now=False)
    title = models.CharField(max_length=100)
    content = models.TextField()
    #+QnAID : FK
    qna = models.ForeignKey('QnA', on_delete=models.CASCADE)

