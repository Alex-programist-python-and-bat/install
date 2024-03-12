import time
from tqdm import tqdm

def calculate_pi(terms):
    pi = 0
    for k in tqdm(range(terms), desc="Calculating pi", unit="term"):
        pi += ((-1) ** k) / (2 * k + 1)
        time.sleep(0.0001)  # для задержки иллюстрации
    return 4 * pi

num_terms = 10000000000000000000000000
print(calculate_pi(num_terms))
