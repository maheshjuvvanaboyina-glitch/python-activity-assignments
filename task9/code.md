## Problem Statement

Develop an ATM transaction sequence simulation program that processes a series of deposit and withdrawal requests against an initial account balance. The program must enforce minimum/maximum balance rules, transaction and daily withdrawal limits, reject invalid or insufficient-fund transactions, log transaction details, and generate a final statement and summary.

---

## Algorithm

1. **Initialize Inputs:** Read initial account balance, daily withdrawal limit, minimum balance required, and a list of transaction requests (each containing type and amount).
2. **Iterate Through Transactions:** For each transaction in the sequence:
* **Deposit:** Add the amount to the current balance, record the transaction as successful, and update the transaction log.
* **Withdrawal:** Validate the withdrawal request:
* Check if the withdrawal amount exceeds the single transaction limit.
* Check if the withdrawal amount exceeds the remaining daily limit.
* Check if the balance after withdrawal drops below the minimum required balance.
* If any check fails, mark the transaction as failed and log the reason.
* If all checks pass, subtract the amount from the balance, update the daily withdrawal total, and record the transaction as successful.




3. **Handle Invalid Types:** If a transaction type is unrecognized, mark it as invalid and log the failure.
4. **Generate Summary:** Compute total successful deposits, total successful withdrawals, and the final account balance.
5. **Output Results:** Display the transaction log and the final summary statement.

---

## Flowchart

```mermaid
flowchart TD
    A([Start]) --> B[/Read Initial Balance, Limits, Transaction List/]
    B --> C[Initialize current_balance, daily_withdrawn = 0, log = []]
    C --> D{More Transactions?}
    D -- Yes --> E[Get next transaction: type, amount]
    E --> F{Type == Deposit?}
    F -- Yes --> G[current_balance += amount]
    G --> H[Record Success & Log]
    H --> D
    F -- No --> I{Type == Withdrawal?}
    I -- Yes --> J{Valid Amount & Within Limits & Min Balance Met?}
    J -- No --> K[Record Failure & Log Reason]
    J -- Yes --> L[current_balance -= amount, daily_withdrawn += amount]
    L --> M[Record Success & Log]
    K --> D
    M --> D
    I -- No --> N[Record Invalid Type & Log]
    N --> D
    D -- No --> O[/Output Transaction Log and Final Summary/]
    O --> P([End])

```

---


---

## Sample Input

* **Initial Balance:** `5000.0`
* **Daily Withdrawal Limit:** `3000.0`
* **Minimum Balance Requirement:** `500.0`
* **Transaction List:**
`[('DEPOSIT', 2000.0), ('WITHDRAWAL', 1500.0), ('WITHDRAWAL', 4000.0), ('DEPOSIT', 500.0), ('WITHDRAWAL', 2500.0)]`

---

## Sample Output

```text
Transaction Log:
  [1] DEPOSIT of 2000.0 -> SUCCESS | Balance: 7000.0
  [2] WITHDRAWAL of 1500.0 -> SUCCESS | Balance: 5500.0
  [3] WITHDRAWAL of 4000.0 -> FAILED | Reason: Daily limit exceeded
  [4] DEPOSIT of 500.0 -> SUCCESS | Balance: 6000.0
  [5] WITHDRAWAL of 2500.0 -> SUCCESS | Balance: 3500.0

Initial Balance: 5000.0
Total Withdrawn Today: 4000.0
Final Account Balance: 3500.0

```
