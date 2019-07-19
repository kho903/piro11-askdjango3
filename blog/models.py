import re
from django.db import models
from django.forms import ValidationError

#Create your models here.
# class Article(models.Model):
#     title=models.CharField(max_length=30, verbose_name='제목')
#     contents=models.TextField(verbose_name="내용")
#
#     def __str__(self):
#         return self.title


def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')


class Post(models.Model):
    STATUS_CHOICES=(
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn'),
    )


    author= models.CharField(max_length=20)
    title = models.CharField(max_length=100, verbose_name='제목',
        help_text="제목을 입력해주세요. 최대 100자 내외"
    # choices=(
    #     ('제목1', '제목1 레이블'), #('저장될 값','UI에 보여질 레이블')
    #     ('제목2', '제목2 레이블'),
    #     ('제목3', '제목3 레이블'),
    # )
    ) #길이 제한이 있는 문자열
    content = models.TextField(verbose_name="내용") #길이 제한이 없는 문자열
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50,
                              blank=True,
                              validators=[lnglat_validator],
                              help_text='경도/위도 포맷으로 입력')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
