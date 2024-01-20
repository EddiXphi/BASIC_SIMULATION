class LinearCongruentialPRNG:
    def __init__(self, seed, a, b, m):
        """
        Initializes a Linear Congruential Pseudo-Random Number Generator (PRNG).

        Parameters:
        - seed: Initial seed value.
        - a: Multiplier.
        - b: Increment.
        - m: Modulus.

        Attributes:
        - state: Current state of the PRNG.
        - a: Multiplier.
        - b: Increment.
        - m: Modulus.
        - generated_values: List to store generated pseudo-random numbers.
        """
        self.state = seed
        self.a = a
        self.b = b
        self.m = m
        self.generated_values = []

    def next_random(self):
        """
        Generates the next pseudo-random number in the sequence.

        Returns:
        - The next pseudo-random number.
        """
        self.state = (self.a * self.state + self.b) % self.m
        random_number = self.state / float(self.m)
        self.generated_values.append(random_number)
        return random_number

    def get_generated_numbers(self):
        """
        Returns the list of generated pseudo-random numbers.

        Returns:
        - List of generated pseudo-random numbers.
        """
        return self.generated_values


def displacement_register_generator(seed, a, b, m, n):
    """
    Generates a sequence of pseudo-random numbers using a Linear Congruential PRNG.

    Parameters:
    - seed: Initial seed value.
    - a: Multiplier.
    - b: Increment.
    - m: Modulus.
    - n: Number of pseudo-random numbers to generate.

    Returns:
    - List of generated pseudo-random numbers.
    """
    generator = LinearCongruentialPRNG(seed, a, b, m)
    pseudo_numbers = []

    for _ in range(n):
        pseudo_numbers.append(generator.next_random())

    return pseudo_numbers

# Example usage:
# seed = 42  # You can change the seed
# a = 1664525
# b = 1013904223
# m = 2**32
# generated_numbers = linear_congruential_generator(seed, a, b, m, 10)
# print(generated_numbers)

