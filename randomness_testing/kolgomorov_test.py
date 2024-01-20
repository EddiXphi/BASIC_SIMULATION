import scipy.stats as stats

def kolgomorov_test(pseudo_array, confidence_level):
    """
    Performs a Kolmogorov-Smirnov test on a sequence of pseudo-random numbers.

    Parameters:
    - pseudo_array: List of pseudo-random numbers.
    - confidence_level: Confidence level for the test.

    Returns:
    - A message indicating whether the null hypothesis is accepted or rejected at the specified confidence level.
    """
    alpha = 1 - confidence_level
    x = pseudo_array

    # Sort the array and calculate cumulative distribution function
    sorted_values = sorted(x)
    cumulative_distribution = [i / len(x) for i in range(1, len(x) + 1)]

    # Calculate the absolute differences
    differences = [abs(cumulative_distribution[i] - sorted_values[i]) for i in range(len(x))]

    # Find the maximum difference
    max_difference = max(differences)

    # Calculate the critical value from the Kolmogorov-Smirnov distribution
    critical_value = stats.ksone.ppf(1 - alpha / 2, len(x))

    if max_difference < critical_value:
        return f"The null hypothesis is accepted"
    else:
        return f"The null hypothesis is rejected"
