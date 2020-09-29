# django-rest-framework-12th
##2주차 스터디 
### 서비스 설명
쇼핑몰 서비스 만들기

### 모델 설명
*유저 모델: 

Customer: 고객(회원과 관련된 정보 포함)  / PK: User 모델의 id(IntegerField)

*서비스 관련 모델:  

Product: 상품/ PK: id(CharField)

Order: 주문/ PK: order_number(IntegerField)

Cart: 장바구니/ PK: Customer의 id

Reviews: 리뷰/ PK: id(BigAutoField)

QnA: 문의/ PK: id(BigAutoField)

Answer: 답변 / PK: id(BigAutoField)

<모델 간 관계>

![img](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/8c157250-f1b4-4c2b-a418-879cc497e262/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20200926%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20200926T083622Z&X-Amz-Expires=86400&X-Amz-Signature=9e8d41c5665da24c32c40fa17a9a4a50dff754935b21fb82e3532fe13e68ae0f&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

### ORM 적용해보기
1.데이터베이스에 Reviews 모델 객체 3개 생성

순서: User 모델 객체 2개 생성 → Customer 모델 객체 2개 생성 → Product 모델 객체 2개 생성 → Reviews 모델 객체 3개 생성

![img](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/13a9858d-c729-4bda-8bea-cb9021ac2d7c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20200926%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20200926T083306Z&X-Amz-Expires=86400&X-Amz-Signature=f4e78f6d9fd8e485864de8781e520f202b6ee0d2e82ee6c005326b785ff37f08&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

```python
from api.models import Customer
c1 = Customer(user=u1, name = "sewon", addr = "Gwangjin-gu", membership = "Gold")
c2 = Customer(user=u2, name = "Snoopy", addr = "Gwangjin-gu", membership = "Gold")

```

![img](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/6c83a6e2-803a-4ada-9ec3-33bde7fbb991/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20200926%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20200926T083416Z&X-Amz-Expires=86400&X-Amz-Signature=0a1c44610433ec7e1b2106704784ce0bea5d0c1aacae1f6642245f0fb046ae5c&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)



```python
from api.models import Product
p1 = Product(id="a", type = "shirts", price = 5000, color = "black", size="L")
p2 = Product(id = "aa", type = "shirts" price = 5500, color = "white", size="M")
```

![img](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/cb7a5f45-5084-4d95-9b67-c2ac2b7b0198/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20200926%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20200926T083521Z&X-Amz-Expires=86400&X-Amz-Signature=a6f345eb3840d5c80c61c0aeba1fb1c0ce247b69cdc87b094568543fe0e3428d&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

```python
from api.models import Reviews
Reviews.objects.create(rating = 4.3, content = "this is good!", customer = c1, product = p1)
Reviews.objects.create(rating = 5.0, content = "this is perfect!", customer = c1, product = p2)
Reviews.objects.create(rating = 5.0, content = "I like it!", customer = c2, product = p2)
```

2.삽입한 객체들 쿼리셋으로 조회하기

![img](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/314a3417-f8fd-4152-9e8e-9b0f1e09fc8f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20200926%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20200926T084835Z&X-Amz-Expires=86400&X-Amz-Signature=83ae95d0b55210c5ba95fbf3dc0fa411ebae43f8b08c553f017b5413a81c0de0&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)



3.filter 함수 사용하기

![img](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/c59b7327-18b2-463f-85cb-6414c42e5043/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20200926%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20200926T085157Z&X-Amz-Expires=86400&X-Amz-Signature=f2976280a6258d91b18dee16f1ba996da8fcec4235a1cc865532ad7822708ce0&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22) 



### 간단한 회고 
구상한 서비스에 필요한 모델들을 직접 구상하는 것이 낯설었고, 모델 관의 정확한 관계, PK와 FK를 정확히 지정하는 것이 중요하다는 것을 깨달았다. 

