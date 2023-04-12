from rest_framework.serializers import ModelSerializer
from news_app.models import News

class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        exclude = ["user"]