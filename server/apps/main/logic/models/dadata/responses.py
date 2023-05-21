from pydantic import BaseModel


class CleanAddressResponse(BaseModel):
    source: str
    result: str
    postal_code: str
    country: str
    region: str
    city_area: str
    city_district: str
    street: str
    house: str
    geo_lat: str
    geo_lon: str
    qc_geo: int

