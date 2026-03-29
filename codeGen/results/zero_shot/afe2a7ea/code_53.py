def set_signal_powers(town):
    return (1 if town > 0 else 0) * (1 / 2 ** (town - 1))

def calculate_probability(n):
    total_prob = 1
    for i in range(1, n + 1):
        total_prob *= set_signal_powers(i)
    return total_prob % 998244353

n = int(input())
print(calculate_probability(n))
