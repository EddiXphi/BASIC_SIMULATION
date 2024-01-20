import pandas as pd
from collections import Counter
import numpy as np
from scipy.stats import chi2

x = [0.872, 0.950, 0.343, 0.058, 0.384,
     0.219, 0.041, 0.036, 0.213, 0.946,
     0.570, 0.842, 0.706, 0.809, 0.300,
     0.618, 0.512, 0.462, 0.005, 0.203,
     0.291, 0.151, 0.596, 0.443, 0.868,
     0.913, 0.511, 0.586, 0.608, 0.879
     ]

def gap_hole_test(pseudo_array, confidence_level, greater_than, less_than):
    """
    Performs the gap test on a sequence of pseudo-random numbers.

    Parameters:
    - pseudo_array: List of pseudo-random numbers.
    - confidence_level: Confidence level for the test.
    - greater_than: Lower bound for the gap test.
    - less_than: Upper bound for the gap test.

    Returns:
    - A message indicating whether the pseudo-random sequence passes the gap test.
    """
    n = len(pseudo_array)
    alpha = 1 - confidence_level

    num_series = pd.Series(pseudo_array)

    test_condition = (num_series > greater_than) & (num_series < less_than)
    sequence = []
    indices = []

    for i, value in enumerate(test_condition):
        if value:
            sequence.append(1)
            indices.append(i)
        else:
            sequence.append(0)

    gap_lengths = []
    for i in range(1, len(indices)):
        gap_lengths.append(indices[i] - indices[i - 1] - 1)

    number_of_gaps = len(gap_lengths)

    def count_occurrences(array):
        count = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, '5+': 0}

        for number in array:
            if 0 <= number <= 4:
                count[number] += 1
            else:
                count['5+'] += 1

        return count

    h = len(gap_lengths)

    sorted_gaps = sorted(gap_lengths)

    observed_frequencies = []

    greater_than_five = [number for number in sorted_gaps if number >= 5]
    lesser_count = Counter()

    for number in sorted_gaps:
        if number < 7:
            lesser_count[number] += 1

    greater_count = Counter(greater_than_five)

    for number, frequency in lesser_count.items():
        observed_frequencies.append(frequency)

    count_frequency_greater_than = 0
    for number, frequency in greater_count.items():
        print(f"Number {number} (greater or equal to 5): {frequency} times")
        count_frequency_greater_than += frequency
    observed_frequencies.append(count_frequency_greater_than)

    print(count_frequency_greater_than)

    expected_frequencies = []
    for i in range(0, 5):
        expected_frequencies.append((h) * (less_than - greater_than) * (1 - (less_than - greater_than)) ** i)
    expected_frequencies.append((h) * (1 - (less_than - greater_than)) ** (i + 1))

    count = count_occurrences(sorted_gaps)

    observed = []
    for key, value in count.items():
        observed.append(value)

    observed = np.array(observed)
    expected = np.array(expected_frequencies)

    X0 = ((observed - expected) ** 2) / expected

    X0 = X0.sum()
    df = len(observed) - 1

    critical_value = chi2.ppf(alpha, df)

    if X0 < critical_value:
        return f"Set of numbers ri accepted. Chi-squared = {X0:.2f}, Critical value = {critical_value:.2f}"
    else:
        return f"Set of numbers ri not accepted. Chi-squared = {X0:.2f}, Critical value = {critical_value:.2f}"

# Example usage:
# gap_test(x, 0.95, 0.8, 1)





