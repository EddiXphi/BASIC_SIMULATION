import scipy.stats

# x = [0.11352, 0.24528, 0.12014, 0.11963, 0.11592, 0.66175, 0.10047, 0.29429, 0.41769, 0.34661, 0.24381,
#      0.66425, 0.94441, 0.81699, 0.82584, 0.81231, 0.88835, 0.71202, 0.22591, 0.97069, 0.33214, 0.15361,
#      0.76613, 0.42239, 0.82506, 0.48166, 0.56711, 0.76950, 0.43478, 0.22817]

def variance_test(pseudo_array, confidence_level):
    """
    Performs a variance test on a sequence of pseudo-random numbers.

    Parameters:
    - pseudo_array: List of pseudo-random numbers.
    - confidence_level: Confidence level for the test.

    Returns:
    - A message indicating whether the variance test passes at the specified confidence level.
    """
    alpha = 1 - confidence_level
    x = pseudo_array

    mean = sum(x) / len(x)
    variance_result = sum((xi - mean) ** 2 for xi in x) / len(x)

    # print("The variance is: ", variance_result)

    z_alpha_over_2 = scipy.stats.chi2.ppf(alpha / 2, len(x) - 1)
    z_alpha_over_2_sided = scipy.stats.chi2.ppf(confidence_level / 2, len(x) - 1)

    lower_limit = z_alpha_over_2 / (12 * (len(x) - 1))
    upper_limit = z_alpha_over_2_sided / (12 * (len(x) - 1))

    print("The lower limit is: ", lower_limit, "and the upper limit is: ", upper_limit)

    if lower_limit < variance_result < upper_limit:
        return f"The null hypothesis is accepted"
    else:
        return f"The null hypothesis is rejected :("

# Example usage:
# variance_test(x, 0.95)
