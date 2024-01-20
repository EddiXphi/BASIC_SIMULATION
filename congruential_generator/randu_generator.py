# Set the number of iterations
n = 10000

# Initialize lists to store generated pseudorandom numbers
pseudos = []
pseudos_acotado = []

# Initialize the seed for the generator
semilla = 12345  # You may replace this with the desired seed value

# Generate pseudorandom numbers using a linear congruential generator
for i in range(n):
    # Linear congruential generator formula: x_{nueva} = (a * x_{actual} + c) % m
    a = 2**16 + 3
    c = 0  # No constant term in this example
    m = 2**31

    # Calculate the next pseudorandom number
    x_nueva = (a * semilla + c) % m

    # Normalize the pseudorandom number to the range [0, 1)
    numero_acotado = semilla / m

    # Append the generated numbers to the lists
    pseudos.append(x_nueva)
    pseudos_acotado.append(numero_acotado)

    # Update the seed for the next iteration
    semilla = x_nueva
