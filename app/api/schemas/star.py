from pydantic import BaseModel, ConfigDict


class StarResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    name: str
    distance_light_years: float
    apparent_magnitude: float
    spectral_type: str
