from rest_framework.fields import BooleanField, CharField, DecimalField, ListField, DictField, IntegerField
from rest_framework.serializers import Serializer

class CleanAddressSerializer(Serializer):
    source = CharField(max_length=1024)
    result = CharField(max_length=1024)
    postal_code = CharField(max_length=1024)
    country = CharField(max_length=1024)
    region = CharField(max_length=1024)
    city_area = CharField(max_length=1024)
    city_district = CharField(max_length=1024)
    street = CharField(max_length=1024)
    house = CharField(max_length=128)
    geo_lat = CharField(max_length=128)
    geo_lon = CharField(max_length=128)
    qc_geo = IntegerField()

class CleanAddressRequestSerializer(Serializer):
    address = CharField(max_length=1024)

