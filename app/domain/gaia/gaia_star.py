from dataclasses import dataclass


@dataclass(frozen=True)
class GaiaStar:
    source_id: str
    ra: float
    dec: float
    parallax: float
    distance_light_years: float
    phot_g_mean_mag: float
    bp_rp: float | None