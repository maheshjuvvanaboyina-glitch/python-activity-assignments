def calculate_bill(units, slabs, fixed_charge, surcharge_rate, rebate_threshold, rebate_amount):
    energy_charge = 0.0
    remaining_units = units
    
    for limit, rate in slabs:
        if remaining_units <= 0:
            break
        if limit is None:
            energy_charge += remaining_units * rate
            remaining_units = 0
        else:
            slab_units = min(remaining_units, limit)
            energy_charge += slab_units * rate
            remaining_units -= slab_units
            
    total = energy_charge + fixed_charge
    if units > rebate_threshold:
        total += total * surcharge_rate
    else:
        total -= rebate_amount
        
    return max(0.0, total)

def analyze_billing(monthly_data, slabs, fixed_charge, surcharge_rate, rebate_threshold, rebate_amount, threshold_pct):
    bills = []
    for month, units in monthly_data.items():
        bill = calculate_bill(units, slabs, fixed_charge, surcharge_rate, rebate_threshold, rebate_amount)
        bills.append((month, units, round(bill, 2)))
        
    analysis = []
    for i in range(len(bills)):
        month, units, bill = bills[i]
        if i == 0:
            analysis.append({"month": month, "units": units, "bill": bill, "increase_pct": 0.0, "unusual": False})
        else:
            prev_bill = bills[i-1][2]
            pct_increase = ((bill - prev_bill) / prev_bill) * 100 if prev_bill > 0 else 0.0
            unusual = pct_increase > threshold_pct
            analysis.append({"month": month, "units": units, "bill": bill, "increase_pct": round(pct_increase, 2), "unusual": unusual})
            
    return analysis

if __name__ == "__main__":
    slabs = [(100, 3.5), (200, 5.0), (None, 7.5)]
    fixed_charge = 150.0
    surcharge_rate = 0.10
    rebate_threshold = 100
    rebate_amount = 50.0
    threshold_pct = 25.0
    
    monthly_data = {
        "January": 120,
        "February": 95,
        "March": 110,
        "April": 250,
        "May": 420,
        "June": 400
    }
    
    results = analyze_billing(monthly_data, slabs, fixed_charge, surcharge_rate, rebate_threshold, rebate_amount, threshold_pct)
    for res in results:
        print(res)
