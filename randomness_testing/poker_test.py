import math
from scipy.stats import chi2

def poker_test(pseudo_array, confidence_level, decimal_places):
    """
    Performs a poker test on a sequence of pseudo-random numbers.

    Parameters:
    - pseudo_array: List of pseudo-random numbers.
    - confidence_level: Confidence level for the test.
    - decimal_places: Number of decimal places to consider.

    Returns:
    - A message indicating whether the poker test passes or fails at the specified confidence level.
    """
    alpha = 1 - confidence_level

    # Define functions to calculate combinations and factorial
    def factorial(n):
        return math.prod(range(1, n + 1))

    def comb(n, r):
        return factorial(n) / (factorial(r) * factorial(n - r))

    # Transform pseudo-random numbers to a list of lists with specified decimal places
    ri_values = [[round(element, decimal_places)] for element in pseudo_array]

    # Flatten the list of values
    ri_values_flat = [item for sublist in ri_values for item in sublist]

    # Initialize counters
    counters = {"TD": 0, "1P": 0, "2P": 0, "T": 0, "TP": 0, "P": 0, "Q": 0}

    # Process each ri number
    for ri in ri_values_flat:
        digits = list(str(ri)[2:])  # Extract decimal digits
        digit_counts = {digit: digits.count(digit) for digit in set(digits)}
        max_count = max(digit_counts.values())
        if max_count == 1:
            counters["TD"] += 1
        elif max_count == 2:
            if list(digit_counts.values()).count(2) == 1:
                counters["1P"] += 1
            else:
                counters["2P"] += 1
        elif max_count == 3:
            if list(digit_counts.values()).count(2) == 1:
                counters["TP"] += 1
            else:
                counters["T"] += 1
        elif max_count == 4:
            counters["P"] += 1
        elif max_count == 5:
            counters["Q"] += 1

    # Define probabilities and total number of observations
    probabilities = {
        "TD": 0.3024,
        "1P": 0.5040,
        "2P": 0.1080,
        "T": 0.0720,
        "TP": 0.0090,
        "P": 0.0045,
        "Q": 0.0001
    }

    # Calculate the Chi-squared statistic
    n = len(ri_values_flat)
    chi_squared_terms = [((counters[key] - n * probabilities[key])**2) / (n * probabilities[key]) for key in counters]
    chi_squared = sum(chi_squared_terms)

    # Obtain the critical value from the Chi-squared distribution
    df = n - 1
    critical_value = chi2.ppf(1 - alpha, df)

    # Compare the statistic with the critical value
    if chi_squared > critical_value:
        return f"Pseudo-random number set accepted. Chi-squared = {chi_squared:.2f}, Critical value = {critical_value:.2f}"
    else:
        return f"Pseudo-random number set not accepted. Chi-squared = {chi_squared:.2f}, Critical value = {critical_value:.2f}"

# Example usage:
# poker_test(arreglo_pseudos, 0.95, 4)
