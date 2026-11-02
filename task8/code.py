def process_exam_results(subject_marks, pass_mark, max_mark, max_grace):
    results = []
    total_grace_used = 0
    failed_count = 0
    total_marks = 0

    for subject, marks in subject_marks.items():
        current_marks = marks
        status = "Pass"

        if current_marks < pass_mark:
            shortfall = pass_mark - current_marks
            if shortfall <= max_grace:
                current_marks += shortfall
                total_grace_used += shortfall
                status = "Pass (Grace)"
            else:
                status = "Fail"
                failed_count += 1
        elif current_marks > max_mark:
            current_marks = max_mark

        total_marks += current_marks
        results.append((subject, current_marks, status))

    max_possible_marks = len(subject_marks) * max_mark
    percentage = (total_marks / max_possible_marks) * 100

    if failed_count > 0:
        final_class = "Fail"
    elif percentage >= 75:
        final_class = "Distinction"
    elif percentage >= 60:
        final_class = "First Class"
    else:
        final_class = "Pass"

    return results, total_marks, percentage, final_class


if __name__ == "__main__":
    student_marks = {
        "Mathematics": 38,
        "Physics": 72,
        "Chemistry": 65,
        "Computer Science": 85,
        "English": 78,
    }

    PASS_MARK = 40
    MAX_MARK = 100
    MAX_GRACE = 5

    res, total, pct, classification = process_exam_results(
        student_marks, PASS_MARK, MAX_MARK, MAX_GRACE
    )

    print("Subject-wise Results:")
    for sub, m, st in res:
        print(f"  {sub}: {m} - {st}")

    print(f"\nTotal Marks: {total} / {len(student_marks) * MAX_MARK}")
    print(f"Percentage: {pct:.2f}%")
    print(f"Final Classification: {classification}")
