def calculate_pi(terms):
    pi = 0
    for k in range(terms):
        pi += ((-1) ** k) / (2 * k + 1)
    return 4 * pi

num_terms = 100000000000000000000000000
print(calculate_pi(num_terms))
