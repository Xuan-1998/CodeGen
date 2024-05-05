import math

def count_configurations(n):
    return math.comb(n+2, n)

def calculate_probability(n):
    inverse_modulo = pow(2, n+2, 998244353)
    probability = (math.comb(n+2, n) * inverse_modulo) % 998244353
    return probability

def main():
    n = int(input())
    probability = calculate_probability(n)
    print(probability)

if __name__ == "__main__":
    main()
