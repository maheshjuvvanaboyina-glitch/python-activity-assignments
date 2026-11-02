def calculate_parking_fee(
    entry_hour,
    entry_min,
    exit_hour,
    exit_min,
    category,
    hourly_rate,
    daily_cap,
    is_overnight,
    has_penalty,
):
    if not (
        0 <= entry_hour <= 23
        and 0 <= entry_min <= 59
        and 0 <= exit_hour <= 23
        and 0 <= exit_min <= 59
    ):
        return None, "Invalid time format"

    entry_total_mins = (entry_hour * 60) + entry_min
    exit_total_mins = (exit_hour * 60) + exit_min

    if exit_total_mins < entry_total_mins:
        exit_total_mins += 24 * 60

    total_duration_mins = exit_total_mins - entry_total_mins
    duration_hours = total_duration_mins / 60.0

    base_fee = duration_hours * hourly_rate

    if base_fee > daily_cap:
        base_fee = daily_cap

    overnight_fee = 150.0 if is_overnight else 0.0
    penalty_fee = 200.0 if has_penalty else 0.0

    total_fee = base_fee + overnight_fee + penalty_fee

    return (
        {
            "duration_hours": duration_hours,
            "base_fee": base_fee,
            "overnight_fee": overnight_fee,
            "penalty_fee": penalty_fee,
            "total_fee": total_fee,
        },
        "SUCCESS",
    )


if __name__ == "__main__":
    ENTRY_H, ENTRY_M = 10, 30
    EXIT_H, EXIT_M = 18, 0
    CATEGORY = "Car"
    HOURLY_RATE = 40.0
    DAILY_CAP = 300.0
    OVERNIGHT = False
    PENALTY = False

    result, status = calculate_parking_fee(
        ENTRY_H,
        ENTRY_M,
        EXIT_H,
        EXIT_M,
        CATEGORY,
        HOURLY_RATE,
        DAILY_CAP,
        OVERNIGHT,
        PENALTY,
    )

    if status != "SUCCESS":
        print(f"Error: {result}")
    else:
        print(f"Vehicle Category: {CATEGORY}")
        print(f"Parking Duration: {result['duration_hours']:.2f} hours")
        print(f"Base Fee: {result['base_fee']}")
        print(f"Overnight Charge: {result['overnight_fee']}")
        print(f"Penalty Charge: {result['penalty_fee']}")
        print(f"Total Parking Fee: {result['total_fee']}")
