def calculate_payroll(employee, deduction_slabs):
    basic = employee['basic']
    housing = employee['housing_allowance']
    transport = employee['transport_allowance']
    overtime = employee['overtime_hours'] * employee['overtime_rate']
    incentive = employee['incentive']
    
    gross_salary = basic + housing + transport + overtime + incentive
    
    total_deduction = 0.0
    remaining_salary = gross_salary
    
    for limit, rate in deduction_slabs:
        if remaining_salary <= 0:
            break
        if limit is None:
            total_deduction += remaining_salary * rate
            remaining_salary = 0
        else:
            taxable_part = min(remaining_salary, limit)
            total_deduction += taxable_part * rate
            remaining_salary -= taxable_part
            
    net_salary = gross_salary - total_deduction
    
    return {
        "employee_id": employee['id'],
        "name": employee['name'],
        "gross_salary": round(gross_salary, 2),
        "total_deductions": round(total_deduction, 2),
        "net_salary": round(net_salary, 2)
    }

if __name__ == "__main__":
    deduction_slabs = [(30000, 0.05), (50000, 0.12), (None, 0.20)]
    
    employees = [
        {"id": 201, "name": "David", "basic": 40000, "housing_allowance": 10000, "transport_allowance": 5000, "overtime_hours": 10, "overtime_rate": 200, "incentive": 3000},
        {"id": 202, "name": "Eva", "basic": 25000, "housing_allowance": 6000, "transport_allowance": 3000, "overtime_hours": 5, "overtime_rate": 150, "incentive": 1000},
        {"id": 203, "name": "Frank", "basic": 70000, "housing_allowance": 15000, "transport_allowance": 8000, "overtime_hours": 15, "overtime_rate": 250, "incentive": 5000}
    ]
    
    for emp in employees:
        statement = calculate_payroll(emp, deduction_slabs)
        print(statement)
