from utils.base_view import BaseView
from utils.helpers import api_success_response,api_error_response,update_db_object
from news_app.db_api import create_news,filter_news,get_news
from utils.pagination import paginated_response
from django.db.models import Q
from news_app.serilaizers import NewsSerializer
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
from django.utils.timezone import make_aware

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
        self.validate_image_content_type(request.data['image'])

        news_data = {"user":request.user}

        for field in mandatory_fields:
            if field == "date":
                try:
                    date_obj = make_aware(datetime.strptime(request.data["date"],"%d/%m/%Y"))
                except ValueError:
                    return api_error_response(error_message=f"Field date is in Invalid Format. Valid Format - DD/MM/YYYY")
                news_data.update({"date": date_obj})   
            else:
                news_data.update({field:request.data.get(field)})
    
        try:
            create_news(**news_data)
        except Exception as e:
            return api_error_response(error_message=str(e))

        return api_success_response(response_data={},message="News Created Succesfully")

class IndividualNewsView(BaseView):

    def patch(self,request,news_id):

        try:
            news_instance = get_news(user=request.user,id=int(news_id))
        except ObjectDoesNotExist:
            return api_error_response(error_message=f"News Instance for ID {news_id} does not exist for requested user")

        request_data = request.data

        if 'image' in request_data:
            self.validate_image_content_type(request_data['image'])

        if "date" in request_data:
            try:
                date_obj = make_aware(datetime.strptime(request_data["date"],"%d/%m/%Y"))
                request_data["date"] = date_obj
            except ValueError:
                return api_error_response(error_message=f"Field date is in Invalid Format. Valid Format - DD/MM/YYYY")
    
        update_db_object(news_instance,request_data)
 

        return api_success_response(response_data={},message=f"News Updated Succesfully")

    def delete(self,request,news_id):

        try:
            news_instance = get_news(user=request.user,id=int(news_id))
        except ObjectDoesNotExist:
            return api_error_response(error_message=f"News Instance for ID {news_id} does not exist for requested user")

        try:
            news_instance.delete()
        except Exception as e:
            return api_error_response(error_message=str(e))

        return api_success_response(response_data={},message=f"News Deleted Succesfully")