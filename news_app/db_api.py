from news_app.models import News
from django.db.models import QuerySet

def create_news(*args,**kwargs) -> News:
    return News.objects.create(*args,**kwargs)

def get_all_news() -> QuerySet:
    return News.objects.all()