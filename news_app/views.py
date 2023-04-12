from rest_framework import permissions
from news_app.base_view import BaseView
from news_app.helpers import api_success_response,api_error_response
from news_app.db_api import create_news,get_all_news
from datetime import datetime
from django.utils.timezone import get_current_timezone,make_aware
from news_app.pagination import paginated_response
from django.db.models import Q
from news_app.serilaizers import NewsSerializer
from django.utils import timezone

class NewsAPIView(BaseView):
    permission_classes = (permissions.AllowAny,)

    def get(self,request):
        _param_dict = request.GET
        news_queryset = get_all_news()
        if "search" in _param_dict:
            news_queryset = news_queryset.filter(Q(name__icontains=_param_dict["search"])
                                                |Q(author__icontains=_param_dict["search"]))
        news_queryset = news_queryset.order_by("-created")
        response = paginated_response(news_queryset,request,NewsSerializer)
        return api_success_response(response_data=response)

    def post(self,request):
        mandatory_fields = ["name","description","date","author","source","image"]
        self.validate_field_in_params(request.data,mandatory_fields)
        news_data = dict()
        for field in mandatory_fields:
            news_data.update({field:request.data.get(field)})
        # news_data.update({
        # # "date": make_aware(datetime.strptime(news_data["date"],"%d/%m/%Y"))
        # "date":pytz.utc.localize(datetime.strptime(news_data["date"],"%d/%m/%Y"))
        # })
        try:
            create_news(**news_data)
        except Exception as e:
            return api_error_response(error_message=str(e))

        return api_success_response(response_data={},message="News Created Succesfully")
