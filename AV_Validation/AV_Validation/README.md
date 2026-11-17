# Vehicle Speed Validation Case Study

A personal Python and pytest project using synthetic vehicle telemetry to demonstrate speed-requirement checks.

## Requirement

Each recorded vehicle speed must be less than or equal to its corresponding speed limit.

## Test Scenarios

| Test | Dataset | Expected result |
| --- | --- | --- |
| Within-limit validation | vehicle_telemetry_compliant.csv | All recorded speeds satisfy the limit, including 45 mph in a 45 mph zone |
| Violation detection | vehicle_telemetry.csv | Exactly one violation: 48 mph in a 45 mph zone at 10:00:02 |

Both tests pass when their expected outcomes are confirmed. A passing detection test means the known violation was found—not that the dataset is compliant.

## Run

From the repository root, with pytest installed:

```bash
python -m pytest AV_Validation/tests -v
```

## Skills Demonstrated

- Reading CSV telemetry with Python
- Comparing recorded behavior against a requirement
- Testing compliant and violating scenarios
- Checking violation timestamps and speed values
- Using pytest assertions

## Scope

This is a small educational case study using synthetic data. It does not use employer data, connect to a vehicle, or establish autonomous-driving safety.