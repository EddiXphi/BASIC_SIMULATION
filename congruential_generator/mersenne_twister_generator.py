def mersenne_twister_generator(seed, n):
    """
    Generates a sequence of pseudo-random numbers using the Mersenne Twister algorithm.

    Parameters:
    - seed: Initial seed value.
    - n: Number of pseudo-random numbers to generate.

    Returns:
    - List of generated pseudo-random numbers.
    """
    numeros_pseudos = []

    # Internal state
    state = [0] * 624
    index = 624

    # Initialization with the given seed
    state[0] = seed
    for i in range(1, 624):
        state[i] = 0xFFFFFFFF & (0x6C078965 * (state[i-1] ^ (state[i-1] >> 30)) + i)
    index = 0

    # Twist function
    def twist():
        nonlocal state, index
        for i in range(624):
            temp = 0xFFFFFFFF & ((state[i] & 0x80000000) + (state[(i+1) % 624] & 0x7FFFFFFF))
            temp_shift = temp >> 1
            if temp % 2 != 0:
                temp_shift = temp_shift ^ 0x9908B0DF
            state[i] = state[(i+397) % 624] ^ temp_shift
        index = 0

    # Number extraction function
    def extract_number():
        nonlocal state, index
        if index >= 624:
            twist()
        y = state[index]
        y = y ^ (y >> 11)
        y = y ^ ((y << 7) & 0x9D2C5680)
        y = y ^ ((y << 15) & 0xEFC60000)
        y = y ^ (y >> 18)
        index += 1
        return (0xFFFFFFFF & y) / 2**32

    for _ in range(n):
        numeros_pseudos.append(extract_number())

    return numeros_pseudos

# Example usage:
# generated_numbers = mersenne_twister_generator(12345, 10)
# print(generated_numbers)
