import validation_generators as gv

def constant_multiplier_generator(multiplier, seed, n):
    """
    Generates pseudo-random numbers using the constant multiplier method.

    Parameters:
    - multiplier: Constant multiplier.
    - seed: Initial seed value.
    - n: Number of pseudo-random numbers to generate.

    Returns:
    - List of generated pseudo-random numbers.
    """
    # Check if the seed has at least three digits
    if len(str(seed)) < 3:
        print("The seed must have at least three digits.")
        return 0
    
    # Validate using generadores_validacion module (but m is not considered here)
    if gv.gen_validation(a=multiplier, seed=seed, n=n) == 0:
        print("Validation is not correct, but m is not considered in this case")

    results = []

    for i in range(n):
        product = seed * multiplier
        product_str = str(product)

        # If the length of the product is less than 2 * length of seed, add leading zeros
        while len(product_str) < 2 * len(str(seed)):
            product_str = '0' + product_str

        # Extract the middle digits
        start = (len(product_str) - len(str(seed))) // 2
        end = start + len(str(seed))
        pseudo_number = int(product_str[start:end])

        # Add to the results list
        results.append(pseudo_number)

        # Update seed for the next iteration
        seed = pseudo_number

    return results

# Example usage:
# multiplier = 4
# seed = 2**8
# n = 3
# generated_numbers = constant_multiplier_generator(multiplier, seed, n)
# print("Generated pseudo-random numbers:", generated_numbers)
