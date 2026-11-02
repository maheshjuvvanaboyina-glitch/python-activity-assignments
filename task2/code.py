def process_hospital_bill(patient_record, policy):
    consultation = patient_record['consultation']
    diagnostics = patient_record['diagnostics']
    treatment = patient_record['treatment']
    category = patient_record['category']
    
    gross_bill = consultation + diagnostics + treatment
    
    discount_rate = policy['discounts'].get(category, 0.0)
    discount_amount = gross_bill * discount_rate
    
    subtotal = gross_bill - discount_amount
    
    max_cap = policy.get('max_out_of_pocket', float('inf'))
    payable_amount = min(subtotal, max_cap)
    
    if payable_amount <= policy['tiers']['subsidized_limit']:
        classification = "Subsidized Tier"
    elif payable_amount <= policy['tiers']['standard_limit']:
        classification = "Standard Tier"
    else:
        classification = "Premium Tier"
        
    return {
        "patient_id": patient_record['id'],
        "name": patient_record['name'],
        "gross_bill": round(gross_bill, 2),
        "discount_amount": round(discount_amount, 2),
        "payable_amount": round(payable_amount, 2),
        "classification": classification
    }

if __name__ == "__main__":
    policy = {
        "discounts": {
            "General": 0.0,
            "Senior Citizen": 0.15,
            "Insured": 0.25
        },
        "max_out_of_pocket": 50000.0,
        "tiers": {
            "subsidized_limit": 10000.0,
            "standard_limit": 35000.0
        }
    }
    
    patients = [
        {"id": 101, "name": "Alice", "consultation": 1500, "diagnostics": 4000, "treatment": 8000, "category": "Senior Citizen"},
        {"id": 102, "name": "Bob", "consultation": 2000, "diagnostics": 12000, "treatment": 45000, "category": "Insured"},
        {"id": 103, "name": "Charlie", "consultation": 1000, "diagnostics": 2500, "treatment": 5000, "category": "General"}
    ]
    
    for patient in patients:
        result = process_hospital_bill(patient, policy)
        print(result)
