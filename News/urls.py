
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/news_app/',include("news_app.urls",namespace="news_app")),
    path('api/accounts/',include("accounts.urls",namespace="accounts")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
