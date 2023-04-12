from rest_framework import status as http_status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError


def api_success_response(response_data, message="", status=http_status.HTTP_200_OK):
    return Response({"success": True, "message": message, "data": response_data}, status=status)

def api_error_response(error_message, status=http_status.HTTP_400_BAD_REQUEST):
    return Response({"success": False, "message": error_message}, status=status)

def api_raise_validation_error_send_400(error_message):
    raise ValidationError(error_message)

