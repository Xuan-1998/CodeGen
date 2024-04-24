from itertools import combinations
from collections import defaultdict
import sys

def read_input():
    n = int(input())
    juices = [tuple(input().split()) for _ in range(n)]
    return n, [(int(price), set(vitamins)) for price, vitamins in juices]

def preprocess_juices(juices):
    min_price_by_vitamin_set = defaultdict(lambda: float('inf'))
    for price, vitamins in juices:
        min_price_by_vitamin_set[frozenset(vitamins)] = min(min_price_by_vitamin_set[frozenset(vitamins)], price)
    return min_price_by_vitamin_set

def find_min_price_for_all_vitamins(min_price_by_vitamin_set):
    all_vitamins = {'A', 'B', 'C'}
    min_price = float('inf')
    for r in range(1, 4):
        for vitamin_set_combo in combinations(min_price_by_vitamin_set.keys(), r):
            combined_vitamins = set().union(*vitamin_set_combo)
            if combined_vitamins == all_vitamins:
                price = sum(min_price_by_vitamin_set[vitamin_set] for vitamin_set in vitamin_set_combo)
                min_price = min(min_price, price)
    return min_price if min_price != float('inf') else -1

def main():
    n, juices = read_input()
    min_price_by_vitamin_set = preprocess_juices(juices)
    min_price = find_min_price_for_all_vitamins(min_price_by_vitamin_set)
    print(min_price)

if __name__ == "__main__":
    main()
