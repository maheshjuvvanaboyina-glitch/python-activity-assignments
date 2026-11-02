def reconcile_inventory(inventory_data):
    audit_report = []

    for product, data in inventory_data.items():
        opening = data["opening"]
        incoming = data["incoming"]
        dispatched = data["dispatched"]
        reported_closing = data["reported_closing"]
        safety_stock = data["safety_stock"]

        expected_closing = opening + incoming - dispatched
        discrepancy = reported_closing - expected_closing

        if reported_closing < safety_stock:
            restock_needed = safety_stock - reported_closing
        else:
            restock_needed = 0

        audit_report.append(
            {
                "product": product,
                "expected_closing": expected_closing,
                "reported_closing": reported_closing,
                "discrepancy": discrepancy,
                "restock_needed": restock_needed,
            }
        )

    return audit_report


if __name__ == "__main__":
    warehouse_stock = {
        "Laptop": {
            "opening": 120,
            "incoming": 50,
            "dispatched": 80,
            "reported_closing": 88,
            "safety_stock": 50,
        },
        "Monitor": {
            "opening": 200,
            "incoming": 30,
            "dispatched": 110,
            "reported_closing": 115,
            "safety_stock": 100,
        },
        "Keyboard": {
            "opening": 350,
            "incoming": 100,
            "dispatched": 250,
            "reported_closing": 190,
            "safety_stock": 200,
        },
    }

    report = reconcile_inventory(warehouse_stock)

    print("Warehouse Inventory Audit Report:")
    for item in report:
        print(f"Product: {item['product']}")
        print(f"  Expected Closing Stock: {item['expected_closing']}")
        print(f"  Reported Closing Stock: {item['reported_closing']}")
        print(f"  Stock Discrepancy: {item['discrepancy']}")
        print(f"  Replenishment Required: {item['restock_needed']}")
        print("-" * 40)
