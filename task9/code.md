## Problem Statement

Develop an attendance recovery computation program that calculates a student's current attendance percentage based on classes attended and total classes conducted. The program must determine the minimum consecutive classes a student needs to attend to reach a specified eligibility threshold under future attendance scenarios.

---

## Algorithm

1. **Initialize Inputs:** Read total classes conducted so far (`total_classes`), total classes attended so far (`attended_classes`), and the target attendance eligibility threshold percentage (`target_percentage`).
2. **Calculate Current Percentage:** Compute the current attendance percentage as $(\frac{\text{attended\_classes}}{\text{total\_classes}}) \times 100$.
3. **Check Threshold Eligibility:**
* If the current percentage is greater than or equal to the target percentage, set the required consecutive classes to $0$.
* Otherwise, proceed to calculate future requirements.


4. **Calculate Future Consecutive Classes:** Solve for $x$ (the number of consecutive classes attended from now on) such that:

$$\frac{\text{attended\_classes} + x}{\text{total\_classes} + x} \ge \frac{\text{target\_percentage}}{100}$$



Rearranging the formula gives:

$$x \ge \frac{(\frac{\text{target\_percentage}}{100} \times \text{total\_classes}) - \text{attended\_classes}}{1 - \frac{\text{target\_percentage}}{100}}$$


5. **Round Up:** Round $x$ up to the nearest whole integer using a ceiling function, since class counts must be whole numbers.
6. **Output Results:** Display current attendance statistics and the minimum consecutive classes needed to reach eligibility.

---

## Flowchart

```mermaid
flowchart TD
    A([Start]) --> B[/Read Total Classes, Attended Classes, Target Percentage/]
    B --> C[Current Percentage = Attended / Total * 100]
    C --> D{Current Percentage >= Target?}
    D -- Yes --> E[Required Classes = 0]
    D -- No --> F[Calculate x: target fraction * Total - Attended / 1 - target fraction]
    F --> G[Required Classes = ceil(x)]
    E --> H[/Output Results and Required Classes/]
    G --> H
    H --> I([End])

```

---


---

## Sample Input

* **Total Classes Conducted:** `40`
* **Classes Attended:** `28`
* **Target Attendance Percentage:** `75.0`

---

## Sample Output

```text
Total Classes Conducted: 40
Classes Attended: 28
Current Attendance Percentage: 70.00%
Target Attendance Threshold: 75.0%
Minimum consecutive classes needed to reach target: 4

```
