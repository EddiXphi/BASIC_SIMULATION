import congruential_generator.blumBlumShub_generator as blumBlumShub_generator
import congruential_generator.additive_congruential_generator as additive_congruential_generator
import congruential_generator.quadratic_congruential_generator as quadratic_congruential_generator
import congruential_generator.mixed_linear_congruential_generator as mixed_linear_congruential_generator
import congruential_generator.multiplicative_congruential_generator as multiplicative_congruential_generator
import congruential_generator.middle_squares_generator as middle_squares_generator
import congruential_generator.mersenne_twister_generator as mersenne_twister_generator
import congruential_generator.constant_multiplier_generator as constant_multiplier_generator
import congruential_generator.middle_products_generator as middle_products_generator
import congruential_generator.displacement_register_generator as displacement_register_generator
import pyfiglet

import randomness_testing.chi_square_test as chi_square_test
import randomness_testing.gaps_test as gaps_test
import randomness_testing.kolgomorov_test as kolgomorov_test
import randomness_testing.mean_test as mean_test
import randomness_testing.poker_test as poker_test
import randomness_testing.variance_test as variance_test

# Print all options from pyfiglet
ascii_banner = pyfiglet.figlet_format("Pseudo-random Number Generator", font='small')
print(ascii_banner)

# Define functions for each option
options = {
    1: lambda: blumBlumShub_generator.gen_blumblumshub(
        int(input("Enter the value of 'm': ")),
        int(input("Enter the value of 'seed': ")),
        int(input("Enter the value of 'n': "))
    ),
    2: lambda: additive_congruential_generator.additive_congruential_generator(
        int(input("Enter the value of 'a': ")),
        int(input("Enter the value of 'c': ")),
        int(input("Enter the value of 'm': ")),
        int(input("Enter the value of 'Seed': ")),
        int(input("Enter the value of 'n': "))
    ),
    3: lambda: quadratic_congruential_generator.quadratic_congruential_generator(
        int(input("Enter the value of 'a': ")),
        int(input("Enter the value of 'b': ")),
        int(input("Enter the value of 'c': ")),
        int(input("Enter the value of 'm': ")),
        int(input("Enter the value of 'Seed': ")),
        int(input("Enter the value of 'n': "))
    ),
    4: lambda: mixed_linear_congruential_generator.mixed_linear_congruential_generator(
        int(input("Enter the value of 'a': ")),
        int(input("Enter the value of 'c': ")),
        int(input("Enter the value of 'm': ")),
        int(input("Enter the value of 'Seed': ")),
        int(input("Enter the value of 'n': "))
    ),
    5: lambda: multiplicative_congruential_generator.multiplicative_congruential_generator(
        int(input("Enter the value of 'a': ")),
        int(input("Enter the value of 'c': ")),
        int(input("Enter the value of 'm': ")),
        int(input("Enter the value of 'Seed': ")),
        int(input("Enter the value of 'n': "))
    ),
    6: lambda: middle_squares_generator.middle_square_generator(
        int(input("Enter the value of 'Seed': ")),
        int(input("Enter the value of 'n': "))
    ),
    7: lambda: mersenne_twister_generator.mersenne_twister_generator(
        int(input("Enter the value of 'Seed': ")),
        int(input("Enter the value of 'n': "))
    ),
    8: lambda: constant_multiplier_generator.constant_multiplier_generator(
        int(input("Enter the value of 'a': ")),
        int(input("Enter the value of 'Seed': ")),
        int(input("Enter the value of 'n': "))
    ),
    9: lambda: middle_products_generator.middle_products_generator(
        int(input("Enter the value of 'Seed 1': ")),
        int(input("Enter the value of 'Seed 2': ")),
        int(input("Enter the value of 'n': "))
    ),
    10: lambda: displacement_register_generator.displacement_register_generator(
        int(input("Enter the value of 'Seed 1': ")),
        int(input("Enter the value of 'a': ")),
        int(input("Enter the value of 'b': ")),
        int(input("Enter the value of 'm': ")),
        int(input("Enter the value of 'n': "))
    ),
}

# Print the menu to the user
print("Select an option:")
print("1. Blum-Blum-Shub Generator | xi = (seed**2) % m ")
print("2. Additive Congruential Generator | xi = (seed+c) % m")
print("3. Quadratic Congruential Generator | xi =  ( a *(seed**2) + b*seed + c) % m")
print("4. Mixed Linear Congruential Generator |   xi = (a *seed + c) % m" )
print("5. Multiplicative Congruential Generator | xi = (a *seed) % m")
print("6. Middle Squares Generator | xi =  seed** 2 ...and take the middle n digits )")
print("7. Mersenne Twister Generator | xi = seed and 0xFFFFFFFF & xi ")
print("8. Constant Multiplier Generator | xi =  seed * multiplier")
print("9. Middle Products Generator | xi =  y0= seed0 * seed1 ... (n numbers in halves ) ...   seed0 = seed1   seed1 = new_seed")
print("10. Shift Register Generator | xi = (self.a * self.state + self.b) % self.m")

# Ask the user to choose an option
option = int(input("Enter the option number: "))

# Execute the function corresponding to the selected option
if option in options:
    pseudo_numbers = options[option]()
else:
    print("Invalid option")

print("Pseudo Numbers", pseudo_numbers)

# Ask for user input for statistical tests
confidence_level = float(input("Enter the value of 'confidence level' [0,1]: "))
decimal_numbers = int(input("Enter the value of 'number of decimals' > 0: "))

greater_than = float(input("Enter the value of the lower limit 'greater than' [0,1] (hole_test): "))
less_than = float(input("Enter the value of the lower limit 'greater than' [0,1] (hole_test): "))
if greater_than > less_than:
    print("Check the intervals because they are not between zero and 1")
    print(f"greater than {greater_than}, {less_than}")

print()
print("######### Results ############" )
print()
print("Mean Test: \n", mean_test.mean_test(pseudo_numbers, confidence_level))
print("Variance Test: \n", variance_test.variance_test(pseudo_numbers, confidence_level))
print("Kolmogorov Test: \n", kolgomorov_test.kolgomorov_test(pseudo_numbers, confidence_level))
print("Poker Test: \n", poker_test.poker_test(pseudo_numbers, confidence_level, decimal_numbers))
print("Chi-Square Test: \n", chi_square_test.chi_square_test(pseudo_numbers, confidence_level))
print("Gaps Test: \n ", gaps_test.gap_hole_test(pseudo_numbers, confidence_level, greater_than, less_than))