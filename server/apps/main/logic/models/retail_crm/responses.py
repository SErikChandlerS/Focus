from decimal import Decimal
from typing import Any, Optional

from pydantic import BaseModel, Field


class _DeliveryType(BaseModel):
    is_dynamic_cost_calculation: bool = Field(alias='isDynamicCostCalculation')
    is_auto_cost_calculation: bool = Field(alias='isAutoCostCalculation')
    is_auto_net_cost_calculation: bool = Field(alias='isAutoNetCostCalculation')
    is_cost_depends_on_region_and_weight_and_sum: bool = Field(alias='isCostDependsOnRegionAndWeightAndSum')
    is_cost_depends_on_date_time: bool = Field(alias='isCostDependsOnDateTime')
    name: str
    code: str
    active: bool
    default_cost: Decimal = Field(alias='defaultCost')
    default_net_cost: Decimal = Field(alias='defaultNetCost')
    description: Optional[str]
    payment_types: list[str] = Field(alias='paymentTypes')
    integration_code: Optional[str] = Field(alias='integrationCode')
    delivery_services: list[str] = Field(alias='deliveryServices')  # TODO Fix type hinting
    default_for_crm: bool = Field(alias='defaultForCrm')
    vat_rate: Optional[str] = Field(alias='vatRate')
    default_tariff_code: Optional[str] = Field(alias='defaultTariffCode')
    default_tariff_type: Optional[str] = Field(alias='defaultTariffType')
    default_tariff_name: Optional[str] = Field(alias='defaultTariffName')


class DeliveryTypesResponse(BaseModel):
    success: bool
    delivery_types: dict[str, _DeliveryType] = Field(alias='deliveryTypes')


class _OrderType(BaseModel):
    name: str
    code: str
    active: bool
    default_for_crm: Optional[bool] = Field(alias='defaultForCrm')
    default_for_api: Optional[bool] = Field(alias='defaultForApi')
    ordering: Optional[int]

class OrderTypesResponse(BaseModel):
    success: bool
    order_types: dict[str, _OrderType] = Field(alias='orderTypes')
