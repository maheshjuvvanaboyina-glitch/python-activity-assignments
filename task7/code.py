import math


def calculate_event_finances(
    venue_cost,
    equipment_cost,
    transport_cost,
    catering_per_person,
    certificate_per_person,
    sponsorship,
    fee_per_person,
):
    variable_cost_per_person = catering_per_person + certificate_per_person
    fixed_costs = venue_cost + equipment_cost + transport_cost
    net_fixed_cost = fixed_costs - sponsorship
    contribution_margin = fee_per_person - variable_cost_per_person

    if contribution_margin <= 0:
        return None, fixed_costs, variable_cost_per_person, net_fixed_cost

    break_even_count = math.ceil(net_fixed_cost / contribution_margin)
    return (
        break_even_count,
        fixed_costs,
        variable_cost_per_person,
        net_fixed_cost,
    )


if __name__ == "__main__":
    venue = 5000.0
    equipment = 1500.0
    transport = 800.0
    catering_pp = 250.0
    certificate_pp = 50.0
    sponsorship = 3000.0
    fee_pp = 400.0

    result = calculate_event_finances(
        venue,
        equipment,
        transport,
        catering_pp,
        certificate_pp,
        sponsorship,
        fee_pp,
    )

    if result[0] is None:
        print("Break-even is not achievable with the current registration fee.")
    else:
        be_count, fc, vc_pp, nfc = result
        total_var_cost = vc_pp * be_count
        total_cost = fc + total_var_cost
        print(f"Fixed Costs: {fc}")
        print(f"Variable Cost Per Person: {vc_pp}")
        print(f"Net Fixed Cost: {nfc}")
        print(f"Minimum Registration Count to Break Even: {be_count}")
        print(f"Total Event Cost at Break-Even: {total_cost}")
