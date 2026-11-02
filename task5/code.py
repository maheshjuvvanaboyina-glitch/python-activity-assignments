def calculate_fare(passenger, distance_slabs, class_multipliers, fixed_reservation_fee, cancellation_fee_rate):
    distance = passenger['distance']
    travel_class = passenger['class']
    age = passenger['age']
    category = passenger['category']
    is_cancelled = passenger['is_cancelled']
    
    base_fare = 0.0
    remaining_distance = distance
    
    for limit, rate in distance_slabs:
        if remaining_distance <= 0:
            break
        if limit is None:
            base_fare += remaining_distance * rate
            remaining_distance = 0
        else:
            slab_dist = min(remaining_distance, limit)
            base_fare += slab_dist * rate
            remaining_distance -= slab_dist
            
    multiplier = class_multipliers.get(travel_class, 1.0)
    class_fare = base_fare * multiplier
    
    discount = 0.0
    if category == "Senior" and age >= 60:
        discount = class_fare * 0.40
    elif category == "Child" and age <= 12:
        discount = class_fare * 0.50
        
    discounted_fare = class_fare - discount
    total_fare = discounted_fare + fixed_reservation_fee
    
    cancellation_charge = 0.0
    net_payable = total_fare
    
    if is_cancelled:
        cancellation_charge = total_fare * cancellation_fee_rate
        net_payable = cancellation_charge
        
    return {
        "passenger_name": passenger['name'],
        "class": travel_class,
        "gross_fare": round(class_fare, 2),
        "discount": round(discount, 2),
        "reservation_fee": fixed_reservation_fee,
        "total_fare": round(total_fare, 2),
        "is_cancelled": is_cancelled,
        "cancellation_charge": round(cancellation_charge, 2),
        "net_payable": round(net_payable, 2)
    }

if __name__ == "__main__":
    distance_slabs = [(100, 1.5), (400, 1.2), (None, 0.9)]
    class_multipliers = {"Sleeper": 1.0, "AC_3Tier": 2.5, "AC_1Tier": 4.0}
    fixed_reservation_fee = 50.0
    cancellation_fee_rate = 0.20
    
    passengers = [
        {"name": "Alice", "age": 65, "class": "AC_3Tier", "distance": 600, "category": "Senior", "is_cancelled": False},
        {"name": "Bob", "age": 30, "class": "Sleeper", "distance": 250, "category": "Regular", "is_cancelled": True},
        {"name": "Charlie", "age": 10, "class": "AC_1Tier", "distance": 800, "category": "Child", "is_cancelled": False}
    ]
    
    for p in passengers:
        statement = calculate_fare(p, distance_slabs, class_multipliers, fixed_reservation_fee, cancellation_fee_rate)
        print(statement)
