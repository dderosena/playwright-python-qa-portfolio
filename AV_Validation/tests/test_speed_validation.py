import csv
from pathlib import Path
def test_vehicle_speed_within_limit():
    file_path = (
        Path(__file__).resolve().parent.parent
        / "data"
        / "vehicle_telemetry_compliant.csv"
    )

    with open(file_path, newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            speed = float(row["speed_mph"])
            speed_limit = float(row["speed_limit_mph"])

            assert speed <= speed_limit
