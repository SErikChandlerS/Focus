from rest_framework.fields import BooleanField, CharField, DecimalField, ListField, DictField, IntegerField
from rest_framework.serializers import Serializer

class _OrderTypeSerializer(Serializer):
    name = CharField(max_length=128)
    code = CharField(max_length=128)
    active = BooleanField()
    default_for_crm = BooleanField(required=False)
    default_for_api = BooleanField(required=False)
    ordering = IntegerField(required=False)

class OrderTypesResponseSerializer(Serializer):
    order_types = DictField(child=_OrderTypeSerializer())
