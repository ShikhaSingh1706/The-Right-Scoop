from rest_framework.response import Response
from rest_framework import status as drf_status

 
class APIResponse:
    """centeralized class for all API response"""

    @staticmethod
    def success(data=None, message="Success", status_code=drf_status.HTTP_200_OK):
        return Response({
            "status":True,
            "message":message,
            "data":data

        },
status=status_code
)
    
@staticmethod
def error(message="Error", errors=None, status_code=drf_status.HTTP_400_BAD_REQUEST):
    return Response(
    {
        "status":False,
        "message":message,
        "error":errors
    },
    status=status_code
)
