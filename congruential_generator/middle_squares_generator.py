import math
import validation_generators as gv

def middle_square_generator(seed, n):
    """
    Generates pseudo-random numbers using the middle-square method.

    Parameters:
    - seed: Initial seed value.
    - n: Number of pseudo-random numbers to generate.

    Returns:
    - List of generated pseudo-random numbers.
    """
    if seed <= 100:
        print("Enter a seed greater than two digits.")
        return 0
    elif gv.gen_validation(seed=seed, n=n) == 0:
        print("However, this validation does not need to be met for middle-square method.")

    results = []
    fixed_seed_str_below = len(str(seed)) // 2
    fixed_seed_str_above = math.ceil(len(str(seed)) / 2)

    for _ in range(n):
        seed_str = str(seed)
        new_number = str(int(seed_str) ** 2)

        if len(new_number) % 2 != 0:
            new_number = '0' + new_number

        half = len(new_number) // 2
        pseudo_number = new_number[half - fixed_seed_str_below: half + fixed_seed_str_above]

        results.append(pseudo_number)
        seed = int(pseudo_number)
    
    return results

# Example usage:
# seed = 1234
# quantity = 5
# generated_numbers = middle_square_method(seed, quantity)
# print("Your pseudo-random numbers are:", generated_numbers)
