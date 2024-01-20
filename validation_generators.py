import math
import numpy as np

def are_coprime_with_respect_to(numbers, with_respect_to):
    """
    Checks if a given set of numbers are coprime with respect to a specific value.

    Parameters:
    - numbers: List of integers to check for coprimality.
    - with_respect_to: Integer with respect to which coprimality is checked.

    Returns:
    - True if the numbers are coprime with respect to the specified value, False otherwise.
    """
    gcd = with_respect_to

    for num in numbers:
        gcd = math.gcd(gcd, num)

    if gcd == 1:
        print(f"{numbers} are coprime with respect to {with_respect_to}.")
        return True
    else:
        print(f"{numbers} are not coprime with respect to {with_respect_to}.")
        return False


def gen_validation(a=False, c=False, m=False, seed=False, n=False, b=False, seed2=False):
    """
    Generates validation for a set of conditions related to linear congruential generator parameters.

    Parameters:
    - a, c, m, seed, n, b, seed2: Parameters for a linear congruential generator.

    Returns:
    - 0 if the conditions are not met, otherwise performs additional checks and prints relevant information.
    """
    validation_array = np.array([a, b, c, m, seed, seed2, n])

    validation_check = []

    for element in validation_array:
        if element:
            validation_check.append(element)

    for element in validation_check:
        if not isinstance(element, float):
            print("Checking initial conditions / | \\ |", element)
        else:
            print("Initial conditions are not integers.")
            return 0

    if m < 0 or (c <= -1 or c > m):
        print("You meet one of the following conditions: m<0 or ( c < 0 or c > m ) ")
        print(f"Values m= {m} c= {c}")
        print("You must ensure that: a, c, m, seed are >0 and m>a, c, seed")

        return 0
    elif (seed < 0 or seed > m):
        print("You meet one of the following conditions: ( seed < 0 or seed > m )")
        print("You must ensure that: a, c, m, seed are >0 and m>a, c, seed")

        return 0
    elif (a < 0 or a > m) or n < 0:
        print("You meet one of the following conditions: (a < 0 or a > m) or n>0")
        print("You must ensure that: a, c, m, seed are >0 and m>a, c, seed")

        return 0
    elif (seed2 < 0 or b < 0):
        print("You meet one of the following conditions: seed2 < 0 or b < 0 ")
        print("You must ensure that: a, c, m, b, seed, seed2 are >0 and m>a, c, seed, seed2, b")
        return 0
    else:
        validation_check = np.array(validation_check)

        print("Validation Array", validation_check)
        print("m", m)

        coprimes = np.delete(validation_check, np.where(validation_check == m))
        number_array = np.delete(coprimes, np.where(coprimes == n))

        print("Array to be coprime", number_array)
        if are_coprime_with_respect_to(number_array, m):
            print("Conditions approved")
        else:
            print("Numbers are not coprime, aborting mission")
            return 0

# Example usage
# numbers = [15, 28]
# with_respect_to = 7
# result = are_coprime_with_respect_to(numbers, with_respect_to)
# print(result)
