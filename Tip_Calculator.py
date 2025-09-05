def tip_calculator(bill_amount, tip_percent=10, people=1):
    # Calculate total tip and amount per person.
    try:
        # Validate inputs
        if bill_amount <= 0:
            raise ValueError("Bill amount must be greater than 0.")
        if tip_percent < 0:
            raise ValueError("Tip percent cannot be negative.")
        if people <= 0:
            raise ValueError("Number of people must be at least 1.")

        # Calculate tip and totals
        total_tip = bill_amount * (tip_percent / 100)
        total_amount = bill_amount + total_tip
        per_person = total_amount / people

        return {
            "total_tip": round(total_tip, 2),
            "total_amount": round(total_amount, 2),
            "per_person": round(per_person, 2)
        }

    except (ValueError, TypeError) as e:
        return {"error": str(e)}

print(tip_calculator(100, 30, 4))