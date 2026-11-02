## Problem Statement

Develop an automated progressive electricity billing and consumption analysis system. The system must calculate monthly household electricity bills based on tiered consumption slabs, fixed monthly charges, high-usage surcharges, and low-usage rebates. Furthermore, the system must process historical multi-month billing records, evaluate consecutive month-over-month cost variations, and automatically flag any unusual or abnormal bill spikes that exceed a predefined percentage threshold.

---

## Algorithm

1. **Input**: Receive monthly consumption units, slab tier definitions, fixed charges, surcharge rate, rebate threshold, rebate amount, and the unusual increase percentage threshold.
2. **Bill Calculation**:
* For a given month's units, traverse the progressive slabs.
* Accumulate the cost based on units falling into each tier limit and rate.
* Add the fixed monthly charge.
* If total consumption exceeds the rebate threshold, apply a surcharge percentage; otherwise, apply a flat rebate discount.


3. **Historical Comparison**:
* Store and compute the calculated bill for each consecutive month.
* Calculate the percentage change between each month and the preceding month.
* Compare the percentage increase against the specified unusual increase threshold.


4. **Flagging Anomalies**: Mark months that exceed the threshold as containing unusual increases.
5. **Output**: Return the calculated bills, percentage changes, and anomaly alert flags.

---

## Flowchart

```mermaid
flowchart TD
    A[Start: Input Monthly Units & Rates] --> B[Loop Through Each Month]
    B --> C[Calculate Slab-based Energy Charges]
    C --> D[Add Fixed Charges]
    D --> E{Units > Rebate Threshold?}
    E -- Yes --> F[Apply Surcharge]
    E -- No --> G[Apply Rebate]
    F --> H[Store Monthly Bill]
    G --> H
    H --> I{More Months?}
    I -- Yes --> B
    I -- No --> J[Compare Consecutive Month Bills]
    J --> K{Percentage Increase > Threshold?}
    K -- Yes --> L[Flag as Unusual Increase]
    K -- No --> M[Mark as Normal]
    L --> N[End: Output Bills & Anomalies]
    M --> N

```

---


---

## Sample Input

```json
{
  "slabs": [
    [100, 3.5],
    [200, 5.0],
    [null, 7.5]
  ],
  "fixed_charge": 150.0,
  "surcharge_rate": 0.10,
  "rebate_threshold": 100,
  "rebate_amount": 50.0,
  "threshold_pct": 25.0,
  "monthly_data": {
    "January": 120,
    "February": 95,
    "March": 110,
    "April": 250,
    "May": 420,
    "June": 400
  }
}

```

---

## Sample Output

```json
[
  {"month": "January", "units": 120, "bill": 620.0, "increase_pct": 0.0, "unusual": false},
  {"month": "February", "units": 95, "bill": 432.5, "increase_pct": -30.24, "unusual": false},
  {"month": "March", "units": 110, "bill": 535.0, "increase_pct": 23.7, "unusual": false},
  {"month": "April", "units": 250, "bill": 1300.0, "increase_pct": 143.18, "unusual": true},
  {"month": "May", "units": 420, "bill": 2722.5, "increase_pct": 109.42, "unusual": true},
  {"month": "June", "units": 400, "bill": 2545.0, "increase_pct": -6.52, "unusual": false}
]

```
