from django.shortcuts import render
import random
from .models import Article

# Create your views here.


def index(request):
    return render(request, 'index.html')


def dinner(request, name):
    menus = [{"name": '족발', "price": 30000}, {"name": '햄버거', "price": 5000}, {
        "name": '치킨', "price": 20000}, {"name": '초밥', "price": 15000}]
    pick = random.choice(menus)  # 랜덤으로 딕셔너리 목록을 골라줌
    articles = Article.objects.all()
    context = {
        'pick': pick,
        'name': name,
        'menus': menus,
        'articles': articles,
    }
    return render(request, 'dinner.html', context)


def review(request):
    return render(request, 'review.html')


def create_review(request):
    content = request.POST.get('content')
    print(request.POST)
    context = {
        'content': content,
    }
    return render(request, 'review_result.html', context)
