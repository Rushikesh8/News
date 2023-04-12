from rest_framework.views import APIView
from typing import Tuple,Union
from .helpers import api_raise_validation_error_send_400


class BaseView(APIView):

    def validate_field_in_params(self, input_data: dict, fields: list) -> Tuple[bool, Union[str, dict]]:
        """
        Validates if all required fields are present in the request parameters
        """
        missing_fields = []
        for field in fields:
            try:
                input_data[field]
            except KeyError:
                missing_fields.append(field)
        if missing_fields:
            is_or_are = 'are' if len(missing_fields) > 1 else 'is'
            field_string = ", ".join(missing_fields)
            api_raise_validation_error_send_400(f'Field/s {field_string} {is_or_are} missing in the request!')
        return input_data
