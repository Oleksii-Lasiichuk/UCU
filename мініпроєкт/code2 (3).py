 """Bad code"""


def GymPlan0(v):
    p = v * 25
    f = v // 5
    t = f * 5 * 18
    c = 100 + v * 25 * 0.6

    if p < t and p < c:
        return "pay per visit"
    elif t < p and t < c:
        return "5-visit package"
    else:
        return "membership"


"""OUR CODE"""

"""
Changes:

1. Renamed variables for better readability
2. Added remaining days, because f = v // 5 just deleted days above 5
3. In the first if-block <= instead of <
"""


def gym_plan(num_of_visits: int) -> str:
    """
    Choose which option is cheaper
    """
    pay_for_visit = num_of_visits * 25
    five_visits_package = num_of_visits // 5
    remaining = num_of_visits % 5
    cost_for_five_visits_package = (five_visits_package * 5 * 18) + (remaining * 25)
    membership = 100 + num_of_visits * 25 * 0.6

    if pay_for_visit <= cost_for_five_visits_package and pay_for_visit <= membership:
        return "pay per visit"
    if (
        cost_for_five_visits_package <= pay_for_visit
        and cost_for_five_visits_package <= membership
    ):
        return "5-visit package"
    return "membership"


print(gym_plan(24))

"""Chat gpt"""


def GymPlan0(v):
    """
    Calculate the best gym payment plan based on the number of visits `v`.
    
    :param v: int, The number of gym visits.
    :return: str, The recommended plan.
    """
    # Pay-per-visit calculation
    pay_per_visit = v * 25
    
    # 5-visit package calculation, adding cost of leftover visits
    five_visit_packages = (v // 5) * 5 * 18
    leftover_visits = (v % 5) * 25  # Remaining visits priced at pay-per-visit rate
    five_visit_total = five_visit_packages + leftover_visits
    
    # Membership cost calculation
    membership_cost = 100 + v * 25 * 0.6
    
    # Compare the costs to determine the best plan
    if pay_per_visit < five_visit_total and pay_per_visit < membership_cost:
        return "pay per visit"
    elif five_visit_total < pay_per_visit and five_visit_total < membership_cost:
        return "5-visit package"
    else:
        return "membership"


"""
Improved Variable Naming:

Changed variable names for clarity (p to pay_per_visit, t to five_visit_total, and c to membership_cost).
Calculation of Leftover Visits:

Added leftover_visits = (v % 5) * 25 to account for any visits that don’t fit into a 5-visit package, which ensures the calculation is accurate.
Simplified Conditionals:

The conditionals remain the same but are more readable with the new variable names.
"""


print(GymPlan0(24))
