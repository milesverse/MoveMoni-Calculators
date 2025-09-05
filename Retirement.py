def retirement_calculator(current_age, retirement_age, yearly_contribution, annual_interest_rate=5):
    # Estimate retirement savings using compound interest formula.
    try:
        # Validate inputs
        if current_age < 0 or retirement_age <= current_age:
            raise ValueError("Retirement age must be greater than current age.")
        if yearly_contribution <= 0:
            raise ValueError("Yearly contribution must be greater than 0.")
        if annual_interest_rate < 0:
            raise ValueError("Interest rate cannot be negative.")

        years = retirement_age - current_age
        r = annual_interest_rate / 100  # convert % to decimal

        # Future Value using annuity formula
        future_value = yearly_contribution * (((1 + r) ** years - 1) / r)
        total_contributions = yearly_contribution * years
        total_interest = future_value - total_contributions

        return {
            "years_to_save": years,
            "future_value": round(future_value, 2),
            "total_contributions": round(total_contributions, 2),
            "total_interest": round(total_interest, 2)
        }

    except (ValueError, TypeError, ZeroDivisionError) as e:
        return {"error": str(e)}
