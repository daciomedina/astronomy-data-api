import json
import time
from pathlib import Path

import astropy.units as u
from astropy.coordinates import SkyCoord
from astroquery.simbad import Simbad


INPUT_FILE = Path("data/gaia_nearby_stars.json")
OUTPUT_FILE = Path("data/gaia_nearby_stars_enriched.json")


def find_simbad_name(ra: float, dec: float) -> str | None:
    coordinates = SkyCoord(ra=ra * u.degree, dec=dec * u.degree, frame="icrs")

    result = Simbad.query_region(
    coordinates,
    radius=60 * u.arcsec,
)

    if result is None or len(result) == 0:
        return None

    return str(result[0]["main_id"])


def main() -> None:
    with INPUT_FILE.open("r", encoding="utf-8") as file:
        stars = json.load(file)

    enriched_stars = []

    for star in stars:
        name = find_simbad_name(
            ra=star["ra"],
            dec=star["dec"],
        )

        enriched_stars.append(
            {
                **star,
                "name": name,
            }
        )

        time.sleep(0.3)

    with OUTPUT_FILE.open("w", encoding="utf-8") as file:
        json.dump(enriched_stars, file, indent=2)

    print(f"Saved {len(enriched_stars)} enriched stars to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()