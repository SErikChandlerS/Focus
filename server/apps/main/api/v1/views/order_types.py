from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from server.apps.main.api.v1.serializers.order_types import OrderTypesResponseSerializer
from server.apps.main.logic.models.retail_crm.responses import OrderTypesResponse


@api_view(['GET'])
def get_order_types(request: Request) -> Response:
    order_types = OrderTypesResponse(**settings.RETAIL_CRM_CLIENT.order_types().get_response())
    return Response(
        OrderTypesResponseSerializer(instance={'order_types': order_types.dict()['order_types']}).data,
        status=HTTP_200_OK,
    )
