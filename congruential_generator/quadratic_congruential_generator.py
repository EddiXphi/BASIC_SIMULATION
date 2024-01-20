import validation_generators as gv

def quadratic_congruential_generator(a, b, c, m, seed, n):
    """
    Generates pseudo-random numbers using the quadratic congruential method.

    Parameters:
    - a: Coefficient for the quadratic term.
    - b: Coefficient for the linear term.
    - c: Constant term.
    - m: Modulus.
    - seed: Initial seed value.
    - n: Number of pseudo-random numbers to generate.

    Returns:
    - List of generated pseudo-random numbers.
    """
    if gv.gen_validation(a=a, b=b, c=c, m=m, seed=seed, n=n) == 0:
        print("Validation is not correct")
        return 0 

    random_numbers = []
    for i in range(n):
        seed = (a * (seed**2) + b * seed + c) % m
        random_number = seed / (m - 1)
        random_numbers.append(abs(random_number))
    
    return random_numbers

# Example usage:
# a = 1664525
# b = 101390
# c = 101390
# m = 2**32
# seed = 12345
# n = 3

# generated_numbers = quadratic_congruential_generator(a, b, c, m, seed, n)
# print("Generated pseudo-random numbers:", generated_numbers)
