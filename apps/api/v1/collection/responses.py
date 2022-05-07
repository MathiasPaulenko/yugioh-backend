from rest_framework.response import Response
from rest_framework import status

INVALID_TYPE = Response(
    {'detail': 'invalid card type.'},
    status=status.HTTP_400_BAD_REQUEST
)

GENERAL_ERROR = Response(
    {'detail': 'an unexpected error has occurred'},
    status=status.HTTP_500_INTERNAL_SERVER_ERROR
)
