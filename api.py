import logging
from typing import Literal
import requests

from pydantic import BaseModel, Field, field_serializer

from requests import Response
from requests.exceptions import RequestException

logger = logging.getLogger("brew")
logger.setLevel(logging.DEBUG)

class BrewAPI:
    def __init__(self):
        self.base_path = "https://api.openbrewerydb.org/v1/breweries/"

    def __call__(self, path: str) -> Response:
        url = self.base_path + path.lstrip("/")

        try:
            response = requests.get(url)
        except RequestException as e:
            logger.info("Call failed with message: %s", e)
            raise

        return response


class BreweryInfo(BaseModel):
    """Define base class for brewery info (returned by API)
    NB: may need to make some more of these optional"""
    id: str
    name: str
    brewery_type: str
    address_1: str | None = None
    address_2: str | None = None
    address_3: str | None = None
    city: str
    state_province: str
    postal_code: str
    country: str
    longitude: float | None = None
    latitude: float | None = None
    phone: str | None = None
    website_url: str | None = None
    state: str
    street: str | None = None


BreweryType = Literal["micro", "nano", "regional", "brewpub", "large", "planning", "bar", "contract", "proprietor", "closed"]


class BreweryParams(BaseModel):
    """Define base class for brewery API call params"""
    per_page: int | None = None
    by_city: str | None = None
    by_country: str | None = None
    by_dist: tuple[float, float] | None = Field(None, description="Latitude and longitude")
    by_ids: list[str] | None = Field(None, description="List of brewery IDs")
    by_name: str | None = None
    by_state: str | None = None
    by_postal: str | None = None
    by_type: BreweryType | None = None

    @field_serializer("by_dist", when_used="always")
    def serialize_by_dist(self, by_dist):
        if by_dist is None: 
            return None
        return f"{by_dist[0]},{by_dist[1]}"
    
    @field_serializer("by_ids", when_used="always")
    def serialize_by_ids(self, by_ids):
        if by_ids is None:
            return None
        return ",".join(by_ids)


class GetSingleBrewery(BrewAPI):
    def __call__(self, brewery_id: str) -> BreweryInfo:
        response = super().__call__(path=brewery_id)
        response_json = response.json()

        return BreweryInfo.model_validate(response_json)

class GetBreweryList(BrewAPI):
    def __call__(self, **kwargs) -> list[BreweryInfo]:
        params = BreweryParams.model_validate(kwargs)  # if this passes, kwargs are valid params
        param_dict = params.model_dump(exclude_unset=True)
        path = "?" + "&".join([f"{k}={v}" for k, v in param_dict.items()])

        response = super().__call__(path=path)
        response_json = response.json()

        return [BreweryInfo.model_validate(x) for x in response_json]
