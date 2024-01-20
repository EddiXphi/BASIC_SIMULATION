import validation_generators as gv

def additive_congruential_generator(a, c, m, seed, n):
    """
    Generates pseudo-random numbers using the additive congruential method.

    Parameters:
    - a: Multiplier coefficient.
    - c: Constant term.
    - m: Modulus.
    - seed: Initial seed value.
    - n: Number of pseudo-random numbers to generate.

    Returns:
    - List of generated pseudo-random numbers.
    """
    if gv.gen_validation(a=a, c=c, m=m, seed=seed, n=n) == 0:
        print("Validation is not correct")
        return 0 

    random_numbers = []
    for i in range(n):
        seed = (seed + c) % m
        random_number = seed / m
        random_numbers.append(random_number)
    
    return random_numbers

# Example usage:
# a = 1664525
# c = 1013904223
# m = 2**32
# seed = 12345
# n = 3

# generated_numbers = additive_congruential_generator(a, c, m, seed, n)
# print("Generated pseudo-random numbers:", generated_numbers)
