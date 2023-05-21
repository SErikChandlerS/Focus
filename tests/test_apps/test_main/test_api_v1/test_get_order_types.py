import json
from unittest.mock import patch, MagicMock

from rest_framework.reverse import reverse
from rest_framework.status import HTTP_200_OK
from rest_framework.test import APIClient
from retailcrm.response import Response


@patch(
    'server.apps.main.api.v1.views.order_types.settings.RETAIL_CRM_CLIENT.order_types',
    MagicMock(return_value=Response(HTTP_200_OK, json.load(open('tests/assets/retail_crm/order_types.json')))),
)
def test_get_order_types_success(api_client: APIClient):
    response = api_client.get(reverse('api_v1_urls:get_order_types'))

    assert response.status_code == HTTP_200_OK
    assert len(response.json()['order_types']) == 30

