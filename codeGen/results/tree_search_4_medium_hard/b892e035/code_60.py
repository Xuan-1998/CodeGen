from functools import lru_cache

@lru_cache(None)
def correct_numbering(n, p1=0, p2=0):
    if n == 0:
        return 1.0 if all(set([p1, p2]).issubset({16, 8, 4, 2, 1})) else 0.0
    prob = correct_numbering(n-1, p1*0.5, p2*0.5)
    return prob * max(p1 / (p1 + p2), p2 / (p1 + p2))

def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        prob = correct_numbering(n)
        print(round(prob, 6))  # Round to 10^-6 precision

if __name__ == "__main__":
    main()
