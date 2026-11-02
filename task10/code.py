def simulate_water_tank(capacity, initial_level, threshold, data):
    current_level = initial_level
    first_threshold_interval = None
    history = []
    overflows = []
    shortages = []
    
    for idx, (inflow, outflow) in enumerate(data, start=1):
        current_level += (inflow - outflow)
        
        overflow = 0
        if current_level > capacity:
            overflow = current_level - capacity
            current_level = capacity
            overflows.append((idx, overflow))
            
        shortage = 0
        if current_level < 0:
            shortage = abs(current_level)
            current_level = 0
            shortages.append((idx, shortage))
            
        if first_threshold_interval is None and current_level >= threshold:
            first_threshold_interval = idx
            
        history.append({
            "interval": idx,
            "inflow": inflow,
            "outflow": outflow,
            "level": current_level,
            "overflow": overflow,
            "shortage": shortage
        })
        
    return history, overflows, shortages, first_threshold_interval

if __name__ == "__main__":
    tank_capacity = 100.0
    initial_water = 40.0
    target_threshold = 80.0
    
    intervals_data = [
        (30.0, 10.0),
        (50.0, 20.0),
        (10.0, 45.0),
        (60.0, 10.0),
        (20.0, 20.0)
    ]
    
    history, overflows, shortages, threshold_interval = simulate_water_tank(
        tank_capacity, initial_water, target_threshold, intervals_data
    )
    
    print("Interval Simulation Results:")
    for h in history:
        print(f"Interval {h['interval']}: Inflow={h['inflow']}, Outflow={h['outflow']}, Level={h['level']}, Overflow={h['overflow']}, Shortage={h['shortage']}")
        
    print(f"\nOverflows Recorded: {overflows}")
    print(f"Shortages Recorded: {shortages}")
    print(f"First Interval Reaching Threshold ({target_threshold}): {threshold_interval}")
