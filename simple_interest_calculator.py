"""
Simple Interest Calculator
---------------------------
Calculates simple interest and total amount based on
Principal, Rate of Interest, and Time.

Formula:
    Simple Interest (SI) = (P * R * T) / 100
    Total Amount (A)     = P + SI
"""


def calculate_simple_interest(principal: float, rate: float, time: float) -> float:
    """Calculate simple interest given principal, rate (%), and time (years)."""
    if principal < 0 or rate < 0 or time < 0:
        raise ValueError("Principal, rate, and time must be non-negative numbers.")
    return (principal * rate * time) / 100


def calculate_total_amount(principal: float, interest: float) -> float:
    """Calculate the total amount (principal + interest)."""
    return principal + interest


def get_positive_float(prompt: str) -> float:
    """Prompt the user until a valid non-negative float is entered."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a non-negative number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def main():
    print("=== Simple Interest Calculator ===")
    principal = get_positive_float("Enter Principal amount: ")
    rate = get_positive_float("Enter Rate of Interest (%): ")
    time = get_positive_float("Enter Time (in years): ")

    interest = calculate_simple_interest(principal, rate, time)
    total = calculate_total_amount(principal, interest)

    print("\n--- Results ---")
    print(f"Principal Amount : {principal:.2f}")
    print(f"Rate of Interest : {rate:.2f}%")
    print(f"Time             : {time:.2f} years")
    print(f"Simple Interest  : {interest:.2f}")
    print(f"Total Amount     : {total:.2f}")


if __name__ == "__main__":
    main()
