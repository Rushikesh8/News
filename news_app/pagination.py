from rest_framework import pagination

class CustomPagination(pagination.PageNumberPagination):
    page_size = 100
    page_size_query_param = "page_size"
    max_page_size = 1000

    def get_paginated_response(self, data):
        return {
            'links':{
                'next':self.get_next_link(),
                'previous':self.get_previous_link()
            },
            'count':self.page.paginator.count,
            'results':data
        }

def paginated_response(queryset,request,serializer_class):
    paginated_instance = CustomPagination()
    paginated_queyset = paginated_instance.paginate_queryset(queryset,request)
    serialized_data = serializer_class(paginated_queyset,many=True).data
    data = paginated_instance.get_paginated_response(serialized_data)
    return data