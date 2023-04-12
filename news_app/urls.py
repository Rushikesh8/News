from django.urls import path
from news_app.views import NewsAPIView
app_name = "news_app"
urlpatterns = [
    path('news/',NewsAPIView.as_view(),name="news")
]