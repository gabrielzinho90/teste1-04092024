def calculator(consumption: list, distributor_tax: float, tax_type: str) -> tuple:
    """
    returns a tuple of floats contained anual savings, monthly savings, applied_discount and coverage
    """
    annual_savings = 0
    monthly_savings = 0
    applied_discount = 0
    coverage = 0

    consumption_avg = sum(consumption) / len(consumption)

    if consumption_avg < 10000:
        discounts = {'Residencial': 0.18, 'Comercial': 0.16, 'Industrial': 0.12}
        coverage = 0.9
    elif 10000 <= consumption_avg <= 20000:
        discounts = {'Residencial': 0.22, 'Comercial': 0.18, 'Industrial': 0.15}
        coverage = 0.95
    else:
        discounts = {'Residencial': 0.25, 'Comercial': 0.22, 'Industrial': 0.18}
        coverage = 0.99

    coverage = coverage    
    applied_discount = discounts[tax_type]
    annual_savings = consumption_avg * distributor_tax * applied_discount * 12
    monthly_savings = annual_savings / 12


    return (
        round(annual_savings, 2),
        round(monthly_savings, 2),
        applied_discount,
        coverage,
    )


if __name__ == "__main__":
    print("Testing...")

    assert calculator([1518, 1071, 968], 0.95871974, "Industrial") == (
        1636.88,
        136.41,
        0.12,
        0.9,
    )


    assert calculator([1000, 1054, 1100], 1.12307169, "Residencial") == (
        2550.36,
        212.53,
        0.18,
        0.9,
    )

    assert calculator([973, 629, 726], 1.04820025, "Comercial") == (
        1561.73,
        130.14,
        0.16,
        0.9,
    )

    assert calculator([15000, 14000, 16000], 0.95871974, "Industrial") == (
        25885.43,
        2157.12,
        0.15,
        0.95,
    )

    assert calculator([12000, 11000, 11400], 1.12307169, "Residencial") == (
        33997.63,
        2833.14,
        0.22,
        0.95,
    )

    assert calculator([17500, 16000, 16400], 1.04820025, "Comercial") == (
        37659.74,
        3138.31,
        0.18,
        0.95,
    )

    assert calculator([30000, 29000, 29500], 0.95871974, "Industrial") == (
        61089.62,
        5090.8,
        0.18,
        0.99,
    )

    assert calculator([22000, 21000, 21400], 1.12307169, "Residencial") == (
        72325.82,
        6027.15,
        0.25,
        0.99,
    )
    assert calculator([25500, 23000, 21400], 1.04820025, "Comercial") == (
        64476.89,
        5373.07,
        0.22,
        0.99,
    )

    print("Everything passed")
