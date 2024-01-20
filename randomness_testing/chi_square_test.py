import numpy as np
import scipy.stats as st

def chi_square_test(arr_x, confidence_level):
    """
    Performs a chi-square goodness-of-fit test on a sequence of pseudo-random numbers.

    Parameters:
    - arr_x: List of pseudo-random numbers.
    - confidence_level: Confidence level for the test.

    Returns:
    - A message indicating whether the null hypothesis is accepted or rejected at the specified confidence level.
    """
    alpha = 1 - confidence_level

    # Generate 6 intervals
    intervals = np.linspace(0, 1, 6)
    # Estimated frequency
    expected_frequency = len(arr_x) / 5
    # Observed frequency
    observed_frequency = np.zeros(5)

    for value in arr_x:
        for i in range(5):
            if intervals[i] <= value < intervals[i+1]:
                observed_frequency[i] += 1
                # Break the loop once it's in the correct interval
                break

    # Calculate Chi-square
    chi_square = np.sum((expected_frequency - observed_frequency)**2) / expected_frequency
    # Critical value of Chi-square with 4 degrees of freedom and the given alpha
    critical_chi_square = st.chi2.isf(alpha, 4)

    result = 'accepted' if chi_square < critical_chi_square else 'rejected'
    # print(f'\tNull Hypothesis {result}. as {chi_square} {"<" if chi_square < critical_chi_square else ">"} chi: {round(critical_chi_square, 5)}')
    return f'\tNull Hypothesis {result}. as {chi_square} {"<" if chi_square < critical_chi_square else ">"} chi: {round(critical_chi_square, 5)}'
