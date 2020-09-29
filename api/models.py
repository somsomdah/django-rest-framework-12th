from django.db import models
from django.contrib.auth.models import User
# manage.py makemigrations --name filename appname


class Lecture(models.Model):
    # related_name - objects와 같음 => all(), create() 등 사용 가능
    # pk는 string 보다 integer로 하는게 용량 상 좋음
    # 첫번째 인자로 verbose_name -> 어드민 사이트에서 변수 이름 대신 사용
    professor = models.ForeignKey('Professor', on_delete=models.CASCADE, related_name='lectures', verbose_name='담당교수')
    code = models.CharField('학정번호', max_length=30)
    faculty = models.CharField('학부대학', max_length=30)
    department = models.CharField('전공', max_length=30)
    semester = models.CharField('학기', max_length=30)
    grade = models.IntegerField('학년')
    name = models.CharField('교과목명', max_length=30)
    credit = models.IntegerField('학점')
    classroom = models.CharField('강의실', max_length=50)
    time = models.CharField('강의시간', max_length=50)

    def __str__(self):
        return "{}, {}".format(self.name, self.professor.name)


class Professor(models.Model):
    # null=True면 blank=True여야 함
    name = models.CharField('이름', max_length=30)
    department = models.CharField('소속', max_length=30, null=True, blank=True)
    office = models.CharField('연구실', max_length=30, null=True, blank=True)
    phone = models.CharField('연락처', max_length=30, null=True, blank=True)
    email = models.EmailField('이메일', null=True, blank=True)

    def __str__(self):
        return "{}, {}".format(self.name, self.department)


class Rank(models.Model):
    lecture = models.ForeignKey('Lecture', on_delete=models.CASCADE, related_name='ranks', verbose_name='과목')
    mileage = models.IntegerField('마일리지')
    is_major = models.BooleanField('전공 여부')
    is_included = models.BooleanField('전공자 정원 포함 여부')
    grade = models.IntegerField('학년')
    success = models.BooleanField('수강 여부')


class Result(models.Model):
    lecture = models.OneToOneField('Lecture', on_delete=models.CASCADE, verbose_name='과목')
    quota = models.IntegerField('정원')
    participants = models.IntegerField('참여 인원')
    major_quota = models.IntegerField('전공자 정원')
    include_second_major = models.BooleanField('복수전공 포함 여부')
    max_mileage = models.IntegerField('최대 마일리지')


class Profile(models.Model):
    MAJOR_CHOICES = [
        ('국어국문학과', '국어국문학과'), ('중어중문학과', '중어중문학과'), ('영어영문학과', '영어영문학과'),
        ('독어독문학과', '독어독문학과'), ('불어불문학과', '불어불문학과'), ('노어노문학과', '노어노문학과'), ('사학과', '사학과'),
        ('철학과', '철학과'), ('문헌정보학과', '문헌정보학과'), ('심리학과', '심리학과'), ('경제학과', '경제학과'),
        ('응용통계학과', '응용통계학과'), ('경영학과', '경영학과'), ('수학과', '수학과'), ('물리학과', '물리학과'),
        ('화학과', '화학과'), ('지구시스템학과', '지구시스템학과'), ('천문우주학과', '천문우주학과'), ('대기과학과', '대기과학과'),
        ('화공생명공학과', '화공생명공학과'), ('전기전자공학과', '전기전자공학과'), ('건축공학과', '건축공학과'),
        ('도시공학과', '도시공학과'), ('사회환경시스템공학과', '사회환경시스템공학과'), ('기계공학과', '기계공학과'),
        ('신소재공학과', '신소재공학과'), ('산업공학과', '산업공학과'), ('컴퓨터과학과', '컴퓨터과학과'),
        ('글로벌융합공학과', '글로벌융합공학과'), ('시스템생물학과', '시스템생물학과'), ('생화학과', '생화학과'),
        ('생명공학과', '생명공학과'), ('신학과', '신학과'), ('정치외교학과', '정치외교학과'), ('행정학과', '행정학과'),
        ('사회복지학과', '사회복지학과'), ('사회학과', '사회학과'), ('문화인류학과', '문화인류학과'),
        ('언론홍보영상학과', '언론홍보영상학과'), ('교회음악과', '교회음악과'), ('성악과', '성악과'), ('피아노과', '피아노과'),
        ('관현악과', '관현악과'), ('작곡과', '작곡과'), ('의류환경학과', '의류환경학과'), ('식품영양학과', '식품영양학과'),
        ('실내건축학과', '실내건축학과'), ('아동가족학과', '아동가족학과'), ('생활디자인학과', '생활디자인학과'),
        ('교육학과', '교육학과'), ('체육교육학과', '체육교육학과'), ('스포츠응용산업학과', '스포츠응용산업학과'),
        ('간호학과', '간호학과'), ('의예과', '의예과'), ('치의예과', '치의예과'), ('약학과', '약학과'), ('국제학과', '국제학과'),
        ('글로벌인재학과', '글로벌인재학과')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    lectures = models.ManyToManyField(Lecture, related_name='users')
    student_id = models.IntegerField('학번', unique=True)
    major = models.CharField('전공', max_length=30, choices=MAJOR_CHOICES)
    second_major = models.CharField('복수전공', max_length=30, null=True, blank=True, choices=MAJOR_CHOICES)
    grade = models.IntegerField('학년')
    created_at = models.DateTimeField('가입일시', auto_now_add=True)
    updated_at = models.DateTimeField('변경일시', auto_now=True)

# created_at = DateTimeField('생성일시', auto_now_add=True) -> default=timezone.now랑 같음
# updated_at = DateTimeField('변경일시', auto_now=True)
