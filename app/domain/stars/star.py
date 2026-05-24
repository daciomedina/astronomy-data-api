from dataclasses import dataclass


@dataclass(frozen=True)
class Star:
    id: str
    name: str
    distance_light_years: float
    apparent_magnitude: float
    spectral_type: str