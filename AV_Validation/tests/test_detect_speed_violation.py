import csv
from pathlib import Path
def test_detect_speed_violation():
    file_path = (
        Path(__file__).resolve().parent.parent
        / "data"
        / "vehicle_telemetry.csv"
    )

    with open(file_path, newline="") as file:
        reader = csv.DictReader(file)

        violations = [
            row for row in reader
            if float(row["speed_mph"]) > float(row["speed_limit_mph"])

        ]
    assert len(violations) == 1
    assert violations[0]["timestamp"] == "10:00:02"
    assert float(violations[0]["speed_mph"]) == 48
    assert float(violations[0]["speed_limit_mph"]) == 45