from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from server.apps.main.api.v1.serializers.delivery_types import DeliveryTypesResponseSerializer
from server.apps.main.logic.models.retail_crm.responses import DeliveryTypesResponse


@api_view(['GET'])
def get_delivery_types(request: Request) -> Response:
    delivery_types = DeliveryTypesResponse(**settings.RETAIL_CRM_CLIENT.delivery_types().get_response())
    return Response(
        DeliveryTypesResponseSerializer(instance={'delivery_types': delivery_types.dict()['delivery_types']}).data,
        status=HTTP_200_OK,
    )
