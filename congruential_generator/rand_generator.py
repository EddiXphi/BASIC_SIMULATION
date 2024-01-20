import numpy as np

# Initialize the lists inside the function
def rand_pseudo(semilla, n):
    pseudos = []
    pseudos_acotado = []

    for i in range(n):
        # Linear congruential generator formula: x_{nueva} = (a * x_{actual}) % m
        a = 7**5
        m = 2**31 - 1

        # Calculate the next pseudorandom number
        x_nueva = (a * semilla) % m

        # Normalize the pseudorandom number to the range [0, 1)
        numero_acotado = semilla / m

        # Append the generated numbers to the lists
        pseudos.append(x_nueva)
        pseudos_acotado.append(numero_acotado)

        # Update the seed for the next iteration
        semilla = x_nueva

    # Return the generated lists
    return pseudos, pseudos_acotado

# Set the seed and the number of iterations
semilla = 100
n = 10000

# Call the function to generate pseudorandom numbers
generated_pseudos, generated_pseudos_acotado = rand_pseudo(semilla, n)

# Print the generated pseudorandom numbers
print("Generated Pseudorandom Numbers:", generated_pseudos)
print("Generated Pseudorandom Numbers (Normalized):", generated_pseudos_acotado)
