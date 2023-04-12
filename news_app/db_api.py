from news_app.models import News
from django.db.models import QuerySet

def create_news(*args,**kwargs) -> News:
    return News.objects.create(*args,**kwargs)

def filter_news(*args,**kwargs) -> QuerySet:
    return News.objects.filter(*args,**kwargs)

def get_news(*args,**kwargs) -> News:
    return News.objects.get(*args,**kwargs)