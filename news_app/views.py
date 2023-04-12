from utils.base_view import BaseView
from utils.helpers import api_success_response,api_error_response,update_db_object
from news_app.db_api import create_news,filter_news,get_news
from utils.pagination import paginated_response
from django.db.models import Q
from news_app.serilaizers import NewsSerializer
from django.core.exceptions import ObjectDoesNotExist

class NewsAPIView(BaseView):
    # permission_classes = (permissions.AllowAny,)

    def get(self,request):
        _param_dict = request.GET
        news_queryset = filter_news(user=request.user)
        if "search" in _param_dict:
            news_queryset = news_queryset.filter(Q(name__icontains=_param_dict["search"])
                                                |Q(author__icontains=_param_dict["search"]))
        news_queryset = news_queryset.order_by("-created")
        response = paginated_response(news_queryset,request,NewsSerializer)
        return api_success_response(response_data=response)

    def post(self,request):
        mandatory_fields = ["name","description","date","author","source","image"]
        self.validate_field_in_params(request.data,mandatory_fields)
        news_data = {"user":request.user}
        for field in mandatory_fields:
            news_data.update({field:request.data.get(field)})
        try:
            create_news(**news_data)
        except Exception as e:
            return api_error_response(error_message=str(e))

        return api_success_response(response_data={},message="News Created Succesfully")

class IndividualNewsView(BaseView):

    def patch(self,request,news_id):

        try:
            news_instance = get_news(id=int(news_id))
        except ObjectDoesNotExist:
            return api_error_response(error_message=f"News Instance for ID {news_id} does not exist")

        request_data = request.data

        try:
            update_db_object(news_instance,request_data)
        except Exception as e:
            return api_error_response(error_message=str(e))

        return api_success_response(response_data={},message=f"News Updated Succesfully")

    def delete(self,request,news_id):

        try:
            news_instance = get_news(id=int(news_id))
        except ObjectDoesNotExist:
            return api_error_response(error_message=f"News Instance for ID {news_id} does not exist")

        try:
            news_instance.delete()
        except Exception as e:
            return api_error_response(error_message=str(e))

        return api_success_response(response_data={},message=f"News Deleted Succesfully")