from django.shortcuts import render
from .models import Article, Comment, HashTag
# Create your views here.

def index(request):
    # 일단 def 되어있는데 리턴이 없으면 에러가 남. 그래서 임시로 pass 적용
    # pass
    article_list = Article.objects.all()
    hashtag_list = HashTag.objects.all()
    ctx={
        "article_list" : article_list,
        "hashtag_list" : hashtag_list
    }
    return render(request, "index.html", ctx)


def detail(request):
    # 일단 def 되어있는데 리턴이 없으면 에러가 남. 그래서 임시로 pass 적용
    pass

# def about(request):
#     # 일단 def 되어있는데 리턴이 없으면 에러가 남. 그래서 임시로 pass 적용
#     pass
