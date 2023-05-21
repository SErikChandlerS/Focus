from rest_framework.fields import BooleanField, CharField, DecimalField, ListField, DictField
from rest_framework.serializers import Serializer


class _DeliveryTypeSerializer(Serializer):
    is_dynamic_cost_calculation = BooleanField()
    is_auto_cost_calculation = BooleanField()
    is_auto_net_cost_calculation = BooleanField()
    is_cost_depends_on_region_and_weight_and_sum = BooleanField()
    is_cost_depends_on_date_time = BooleanField()
    name = CharField(max_length=128)
    code = CharField(max_length=128)
    active = BooleanField()
    default_cost = DecimalField(max_digits=10, decimal_places=2)
    default_net_cost = DecimalField(max_digits=10, decimal_places=2)
    description = CharField(max_length=128, required=False)
    payment_types = ListField(child=CharField())
    integration_code = CharField(max_length=128, required=False)
    delivery_services: ListField(child=CharField())
    default_for_crm = BooleanField()
    vat_rate = CharField(max_length=128, required=False)
    default_tariff_code = CharField(max_length=128, required=False)
    default_tariff_type = CharField(max_length=128, required=False)
    default_tariff_name = CharField(max_length=128, required=False)


class DeliveryTypesResponseSerializer(Serializer):
    delivery_types = DictField(child=_DeliveryTypeSerializer())
