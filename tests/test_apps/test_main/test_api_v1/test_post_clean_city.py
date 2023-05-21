import json
from unittest.mock import patch, MagicMock

from rest_framework.reverse import reverse
from rest_framework.status import HTTP_200_OK
from rest_framework.test import APIClient

@patch(
    'server.apps.main.api.v1.views.clean_city.settings.DADATA.clean',
    MagicMock(return_value=json.load(open('tests/assets/dadata/clean_city.json'))),
    clean.assert_called_once_with('address', 'москва сухонская 11'),

)
def test_post_clean_city(api_client: APIClient):
    response = api_client.post(reverse('api_v1_urls:post_clean_city'), data={'address' : 'москва сухонская 11'})

    assert response.status_code == HTTP_200_OK
