def analyze_manufacturing(material_cost, labor_hours, labor_rate, machine_hours, machine_rate, wastage_pct, overheads, target_profit_pct, target_selling_price):
    material_with_wastage = material_cost * (1 + wastage_pct / 100)
    labor_cost = labor_hours * labor_rate
    machine_cost = machine_hours * machine_rate
    total_cost = material_with_wastage + labor_cost + machine_cost + overheads
    calculated_selling_price = total_cost * (1 + target_profit_pct / 100)
    profit_target_met = calculated_selling_price >= target_selling_price
    return total_cost, calculated_selling_price, profit_target_met

if __name__ == "__main__":
    material_cost = 120.0
    labor_hours = 2.5
    labor_rate = 18.0
    machine_hours = 1.5
    machine_rate = 30.0
    wastage_pct = 5.0
    overheads = 25.0
    target_profit_pct = 20.0
    target_selling_price = 260.0

    total_cost, calculated_selling_price, profit_target_met = analyze_manufacturing(
        material_cost, labor_hours, labor_rate, machine_hours, machine_rate, 
        wastage_pct, overheads, target_profit_pct, target_selling_price
    )

    print(f"Total Manufacturing Cost: ${total_cost:.2f}")
    print(f"Calculated Selling Price: ${calculated_selling_price:.2f}")
    print(f"Profit Target Met: {profit_target_met}")
