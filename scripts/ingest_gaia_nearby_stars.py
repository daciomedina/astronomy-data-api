import json
from pathlib import Path

from astroquery.gaia import Gaia


OUTPUT_FILE = Path("data/gaia_nearby_stars.json")


QUERY = """
SELECT TOP 20
    source_id,
    ra,
    dec,
    parallax,
    phot_g_mean_mag,
    bp_rp
FROM gaiadr3.gaia_source
WHERE parallax IS NOT NULL
AND parallax > 0
AND phot_g_mean_mag IS NOT NULL
ORDER BY parallax DESC
"""


def parallax_to_light_years(parallax_mas: float) -> float:
    distance_parsecs = 1000 / parallax_mas
    return distance_parsecs * 3.26156


def main() -> None:
    job = Gaia.launch_job_async(QUERY)
    results = job.get_results()

    stars = []

    for row in results:
        parallax = float(row["parallax"])

        stars.append(
            {
                "source_id": str(row["source_id"]),
                "ra": float(row["ra"]),
                "dec": float(row["dec"]),
                "parallax": parallax,
                "distance_light_years": round(
                    parallax_to_light_years(parallax),
                    2,
                ),
                "phot_g_mean_mag": float(row["phot_g_mean_mag"]),
                "bp_rp": None if row["bp_rp"] is None else float(row["bp_rp"]),
            }
        )

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with OUTPUT_FILE.open("w", encoding="utf-8") as file:
        json.dump(stars, file, indent=2)

    print(f"Saved {len(stars)} stars to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()