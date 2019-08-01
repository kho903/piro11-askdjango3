import re
from django.conf import settings
from django.db import models
from django.forms import ValidationError
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail


#Create your models here.
# class Article(models.Model):
#     title=models.CharField(max_length=30, verbose_name='제목')
#     contents=models.TextField(verbose_name="내용")
#
#     def __str__(self):
#         return self.title
from django.urls import reverse


def lnglat_validator(value):
    if not re.match(r'^(\d+\.?\d*),(\d+\.?\d*)$', value):
        raise ValidationError('Invalid type')


class Post(models.Model):
    STATUS_CHOICES=(
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='+', on_delete=models.CASCADE)

    title = models.CharField(max_length=100, verbose_name='제목',
        help_text="제목을 입력해주세요. 최대 100자 내외"
    )
    content = models.TextField(verbose_name="내용") #길이 제한이 없는 문자열
    photo = ProcessedImageField(blank=True, upload_to='blog/post/%Y/%m/%d',
                processors=[Thumbnail(300, 300)],
                            format='JPEG',
                            options={'quality': 60})

    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50,
                              blank=True,
                              validators=[lnglat_validator],
                              help_text='경도/위도 포맷으로 입력')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    tag_set = models.ManyToManyField('Tag',blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.id])


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,)
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name=models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name