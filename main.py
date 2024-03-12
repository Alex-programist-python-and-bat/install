from multiprocessing import Pool as P
from tqdm import tqdm as T

def c(k):
    return ((-1) ** k) / (2 * k + 1)

def p(t, n):
    with P(n) as p:
        return 4 * sum(T(p.imap(c, range(t)), total=t, desc="Calculating pi", unit="term"))

t, n = 1000000, 7
print(p(t, n))  
print(f"{n} cores was used")
