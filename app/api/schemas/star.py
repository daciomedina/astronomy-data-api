from pydantic import BaseModel


class StarResponse(BaseModel):
    id: str
    name: str
    distance_light_years: float
    apparent_magnitude: float
    spectral_type: str
