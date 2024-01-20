import scipy.stats
import numpy as np

def mean_test(pseudo_array, confidence_level):
    """
    Performs a hypothesis test on the mean of a sequence of pseudo-random numbers.

    Parameters:
    - pseudo_array: List of pseudo-random numbers.
    - confidence_level: Confidence level for the test.

    Returns:
    - A message indicating whether the null hypothesis is accepted or rejected at the specified confidence level.
    """
    #pseudo_array = str(pseudo_array)
    alpha = 1 - confidence_level
    n = len(pseudo_array)

    # Convert the input array to a NumPy array
    generator = np.array(pseudo_array)
    mean_value = generator.mean()

    # Calculate the critical values for a two-tailed test
    z_alpha_over_2 = scipy.stats.norm.ppf(1 - alpha / 2)
    lower_limit = 0.5 - z_alpha_over_2 * (1 / (12 * (n ** 0.5)))
    upper_limit = 0.5 + z_alpha_over_2 * (1 / (12 * (n ** 0.5)))

    if lower_limit < mean_value < upper_limit:
        return f"The null hypothesis is accepted"
    else:
        return f"The null hypothesis is rejected"
