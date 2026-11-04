
# Hospital Billing and Patient Classification System

## 1. Problem Statement

Develop an automated hospital billing and patient classification system. The system calculates consultation fees, diagnostic charges, and treatment costs. It applies concessions or insurance discounts based on patient categories, validates billing constraints such as maximum out-of-pocket limits and minimum payable amounts, and classifies patients into payment tiers or discharge statuses according to institutional payment policies.

## 2. Algorithm

1. Start.
2. Read patient name and category.
3. Read consultation fee, diagnostic charges, and treatment cost.
4. Calculate total bill.
5. Apply discount based on patient category.
6. Calculate final payable amount.
7. Apply minimum payable amount and maximum bill cap.
8. Classify patient into payment tier.
9. Display total bill, discount, payable amount, and status.
10. Stop.

## 3. Flowchart (Mermaid Code)

``` mermaid
flowchart TD
    A([Start]) --> B[/Enter Patient Name and Category/]
    B --> C[/Enter Consultation Fee, Diagnostic Charges, Treatment Cost/]
    C --> D[Calculate Total Bill]
    D --> E{Patient Category?}
    E -->|Senior| F[Apply 20% Discount]
    E -->|Insurance| G[Apply 30% Discount]
    E -->|Normal| H[No Discount]
    F --> I[Calculate Payable Amount]
    G --> I
    H --> I
    I --> J{Payable Below Minimum?}
    J -->|Yes| K[Set Minimum Payable]
    J -->|No| L[Check Maximum Cap]
    K --> L
    L --> M{Payable Above Cap?}
    M -->|Yes| N[Apply Maximum Cap]
    M -->|No| O[Classify Payment Tier]
    N --> O
    O --> P[/Display Bill and Status/]
    P --> Q([Stop])
```
## 4. Sample Input

```

Enter patient name: Ravi
Enter patient category (normal/senior/insurance): senior
Enter consultation fee: 500
Enter diagnostic charges: 1000
Enter treatment cost: 2000

```

## 5. Sample Output

```

--- Hospital Billing Report ---
Patient Name: Ravi
Patient Category: senior
Total Bill: 3500.0
Discount: 700.0
Final Payable: 2800.0
Payment Tier: Standard
Discharge Status: Payment Required

```
