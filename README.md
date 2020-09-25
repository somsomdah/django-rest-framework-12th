# django-rest-framework-12th
 
## 2주차 과제

### 서비스 설명
- 수강편람 - 수업 정보, 수강신청 결과 제공
- 마일리지 컷 - 과목명, 담당 교수를 입력하면 사용자 정보에 기록된 전공과 학년을 기준으로 최근 3개년 마일리지 컷 제공

### 모델 설명
```python
class Lecture(models.Model):
    professor = models.ForeignKey('Professor', on_delete=models.CASCADE, related_name='lectures')
    lecture_id = models.CharField(max_length=30, primary_key=True)
    faculty = models.CharField(max_length=30)
    department = models.CharField(max_length=30)
    semester = models.CharField(max_length=30)
    grade = models.IntegerField()
    name = models.CharField(max_length=30)
    credit = models.IntegerField()
    classroom = models.CharField(max_length=50)
    time = models.CharField(max_length=50)

    def __str__(self):
        return self.name
```
```python
class Professor(models.Model):
    name = models.CharField(max_length=30)
    department = models.CharField(max_length=30, null=True)
    office = models.CharField(max_length=30, null=True)
    phone = models.CharField(max_length=30, null=True)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.name
```
```python
class Mileage(models.Model):
    lecture = models.ForeignKey('Lecture', on_delete=models.CASCADE, related_name='mileages')
    mileage = models.IntegerField()
    is_major = models.CharField(max_length=10)
    grade = models.IntegerField()
    success = models.CharField(max_length=10)
```
```python
class Result(models.Model):
    lecture = models.OneToOneField('Lecture', on_delete=models.CASCADE, primary_key=True)
    quota = models.IntegerField()
    major_quota = models.IntegerField()
    participants = models.IntegerField()
    max_mileage = models.IntegerField()
```
```python
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.IntegerField(primary_key=True)
    major = models.CharField(max_length=30)
    second_major = models.CharField(max_length=30, null=True)
    grade = models.IntegerField()
```

### ORM 적용해보기
1. 데이터베이스에 해당 모델 객체 3개 넣기
```python
>>> from api.models import Lecture, Professor

>>> q = Professor(name="이인권", department="공과대학 컴퓨터과학과", office="제4공학관 D719", phone="02-2123-5713", email="iklee@yonsei.ac.kr")
>>> q.save()
>>> w = Professor(name="안형찬", department="공과대학 컴퓨터과학과")
>>> w.save()
>>> a = Lecture(lecture_id="CSI2102-02", faculty="공과대학", department="컴퓨터과학전공", semester="2020-2", grade="1", name="객체지향프로그래밍", credit="3", classroom="동영상컨텐츠/실시간온라인", time="화8,9/목9")
>>> a.professor = q
>>> a.save()
>>> b = Lecture(lecture_id="CSI3108-01", faculty="공과대학", department="컴퓨터과학전공", semester="2020-2", grade="3", name="알고리즘분석", credit="3", classroom="공D504", time="수2/금5,6")
>>> b.professor = w
>>> b.save()
>>> w.lectures.create(lecture_id="CSI2103-02", faculty="공과대학", department="컴퓨터과학전공", semester="2020-1", grade="3", name="자료구조", credit="3", classroom="공D504", time="화4/목6,7")
```
2. 삽입한 객체들을 쿼리셋으로 조회해보기
```python
>>> Lecture.objects.all()
<QuerySet [<Lecture: 객체지향프로그래밍, 이인권>, <Lecture: 자료구조, 안형찬>, <Lecture: 알고리즘분석, 안형찬>]>
>>> Professor.objects.all()
<QuerySet [<Professor: 이인권, 공과대학 컴퓨터과학과>, <Professor: 안형찬, 공과대학 컴퓨터과학과>]>
>>> b = Professor.objects.get(name="안형찬")
>>> b.lectures.all()
<QuerySet [<Lecture: 자료구조, 안형찬>, <Lecture: 알고리즘분석, 안형찬>]>
```
3. filter 함수 사용해보기
```python
>>> Lecture.objects.filter(semester="2020-2")
<QuerySet [<Lecture: 객체지향프로그래밍, 이인권>, <Lecture: 알고리즘분석, 안형찬>]>
```

### 간단한 회고 
실제로 내가 필요로 하는 서비스를 만드는 것이라 흥미롭게 진행할 수 있었다.   
실제 데이터를 삽입하면서 내가 설정한 조건에 맞지 않는 데이터가 존재하여 모델을 수정하고 migration을 계속 추가하여 초기 설계를 신경써서 해야겠다는 생각을 했다.   
중간중간 커밋하자.. 
