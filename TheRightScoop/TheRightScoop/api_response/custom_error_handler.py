from rest_framework.views import exception_handler
from .custom_response_handler import APIResponse


def custom_exception_handler(exc,context):
    response=exception_handler(exc,context)

    if response is not None:
        return APIResponse.error(
            message="Something went wrong",
            errors=response.data,
            status_code=response.status_code
        )
    return response