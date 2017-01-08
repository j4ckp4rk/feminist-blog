from django.db import models

# Create your models here.

# model 종류 게시글, 댓글, 카테고리, 해시태그

class Article(models.Model):
    #전체 대문자는 바꾸지 않는 항목임을 명시함
    DEVELOPMENT = "dv"
    PERSONAL = "ps"
    #나중에 편하게 항목을 추가하기 위해 튜플 활용
    CATEGORY_CHOICES = (
        (DEVELOPMENT, "developement"),
        (PERSONAL, "personal"),
    )

    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(
        max_length=2
        choices = CATEGORY_CHOICES,
        default = DEVELOPMENT,
    )

class Comment(models.Model):
    #코멘트가 어디에 달려있는 것인지를 확인해야 하기 때문에 foreign key가 필요
    # Article 삭제시 코멘트도 날림
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    comment = models.CharField(max_length=200)

class HashTag(models.Model):
    name = models.CharField(max_length=50)
