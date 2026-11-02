## Problem Statement

Develop a campus event financial planning program that computes total event expenses by incorporating venue, equipment, transport, catering, and certificate costs. The program must account for total sponsorships and participant registration fees to determine net financial shortfalls and calculate the minimum registration count required for the event to break even.

---

## Algorithm

1. **Initialize Inputs:** Read venue cost, equipment cost, transport cost, catering cost per person, certificate cost per person, total sponsorship amount, and registration fee per participant.
2. **Calculate Variable Costs:** Compute the variable cost per participant as the sum of catering cost per person and certificate cost per person.
3. **Calculate Fixed Costs:** Compute total fixed costs as the sum of venue cost, equipment cost, and transport cost.
4. **Calculate Net Fixed Cost:** Subtract the sponsorship amount from the total fixed costs.
5. **Calculate Contribution Margin:** Determine the net contribution per participant by subtracting the variable cost per person from the registration fee per participant.
6. **Check Feasibility:** If the contribution margin is less than or equal to zero, output that break-even is impossible with the current fee structure.
7. **Calculate Break-Even Count:** Divide the net fixed cost by the contribution margin and round up to the nearest whole integer using a ceiling function.
8. **Output Results:** Display fixed costs, variable costs per person, net fixed costs, and the minimum registration count required to break even.

---

## Flowchart

```mermaid
flowchart TD
    A([Start]) --> B[/Read Inputs: Venue, Equipment, Transport, Catering/Person, Certificate/Person, Sponsorship, Fee/Person/]
    B --> C[Variable Cost / Person = Catering + Certificate]
    C --> D[Fixed Costs = Venue + Equipment + Transport]
    D --> E[Net Fixed Cost = Fixed Costs - Sponsorship]
    E --> F[Contribution Margin = Fee / Person - Variable Cost / Person]
    F --> G{Contribution Margin > 0?}
    G -- No --> H[/Output: Break-even Impossible/]
    G -- Yes --> I[Break-Even Count = ceil(Net Fixed Cost / Contribution Margin)]
    I --> J[/Output: Fixed Costs, Net Fixed Cost, Min Break-Even Count, Total Cost/]
    H --> K([End])
    J --> K([End])

```

---



---

## Sample Input

* **Venue Cost:** 5000.0
* **Equipment Cost:** 1500.0
* **Transport Cost:** 800.0
* **Catering Cost per Person:** 250.0
* **Certificate Cost per Person:** 50.0
* **Sponsorship Amount:** 3000.0
* **Registration Fee per Participant:** 400.0

---

## Sample Output

```text
Fixed Costs: 7300.0
Variable Cost Per Person: 300.0
Net Fixed Cost: 4300.0
Minimum Registration Count to Break Even: 43
Total Event Cost at Break-Even: 20200.0

```
