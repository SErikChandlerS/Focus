from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from server.apps.main.logic.models.dadata.responses import CleanAddressResponse
from server.apps.main.api.v1.serializers.clean_city import CleanAddressSerializer, CleanAddressRequestSerializer


@api_view(['POST'])
def post_clean_city(request : Request) -> Response:
    serializer = CleanAddressRequestSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        result = CleanAddressResponse(**settings.DADATA.clean('address', request.data))
        return Response(CleanAddressSerializer(result).data, HTTP_200_OK)

