import math

def middle_products_generator(seed0, seed1, n):
    """
    Generates pseudo-random numbers using the middle products method.

    Parameters:
    - seed0: First seed value.
    - seed1: Second seed value.
    - n: Number of pseudo-random numbers to generate.

    Returns:
    - List of generated pseudo-random numbers.
    """
    # Check if both seeds have at least three digits
    if seed0 <= 999 and seed1 <= 999:
        print("Both seeds must have at least three digits.")
        return

    results = []
    size_fixed_seed_str_below = len(str(seed0)) // 2
    size_fixed_seed_str_above = math.ceil(len(str(seed0)) / 2)

    for i in range(n):
        y0 = seed0 * seed1

        seed_str = str(y0)
        new_number = seed_str

        # If the length of the product is less than 2 * length of seed0, add leading zeros
        if len(new_number) % 2 != 0:
            new_number = '0' + new_number

        half = len(new_number) // 2
        pseudo_number = new_number[half - size_fixed_seed_str_below: half + size_fixed_seed_str_above]

        results.append(pseudo_number)
        seed0 = seed1
        seed1 = int(pseudo_number)

    return results

# Example usage:
# seed0 = 1234
# seed1 = 5678
# n = 5
# generated_numbers = middle_products_generator(seed0, seed1, n)
# print("Generated pseudo-random numbers:", generated_numbers)
