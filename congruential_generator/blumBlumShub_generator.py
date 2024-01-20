import validation_generators as gv  # Assuming that 'validation' module contains the 'gen_validation' function

def gen_blumblumshub(m, seed, n):
    """
    Generates a sequence of pseudo-random numbers using the Blum Blum Shub algorithm.

    Parameters:
    - m: Integer, modulus for the algorithm.
    - seed: Integer, initial seed value.
    - n: Integer, number of random numbers to generate.

    Returns:
    - List of pseudo-random numbers generated using the Blum Blum Shub algorithm.
    """
    if gv.gen_validation(m=m, seed=seed, n=n) == 0:
        print("Validation is not correct")
        return 0

    random_numbers = []

    for i in range(n):
        seed = (seed ** 2) % m
        random_number = seed / m
        random_numbers.append(random_number)

    return random_numbers

# Example usage:
# m_value = 256
# seed_value = 42
# count = 10
# result = gen_blumblumshub(m_value, seed_value, count)
# print(result)
