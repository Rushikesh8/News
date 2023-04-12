from django.urls import path
from news_app.views import NewsAPIView,IndividualNewsView
app_name = "news_app"
urlpatterns = [
    path('news/',NewsAPIView.as_view(),name="news"),
    path('news/<int:news_id>',IndividualNewsView.as_view(),name="individual-news")
]