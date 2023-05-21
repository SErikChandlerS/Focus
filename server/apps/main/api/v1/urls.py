from django.urls import path

from server.apps.main.api.v1.views.clean_city import post_clean_city
from server.apps.main.api.v1.views.delivery_types import get_delivery_types
from  server.apps.main.api.v1.views.order_types import get_order_types

app_name = 'api_v1_urls'

urlpatterns = [
    path('delivery-types/', get_delivery_types, name='get_delivery_types'),
    path('order-types/', get_order_types, name='get_order_types'),
    path('clean-city/', post_clean_city, name='post_clean_city')
]
