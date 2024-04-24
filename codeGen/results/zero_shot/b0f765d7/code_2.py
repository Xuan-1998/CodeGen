import sys

def read_input():
    n = int(input().strip())
    juices = [tuple(input().strip().split()) for _ in range(n)]
    return n, juices

def preprocess_juices(juices):
    # Mapping of vitamin combinations to the minimum price
    min_price = {}
    for price, vitamins in juices:
        price = int(price)
        vitamins = ''.join(sorted(vitamins))  # Sort to standardize key
        if vitamins not in min_price or price < min_price[vitamins]:
            min_price[vitamins] = price
    return min_price

def find_min_price(min_price):
    # All possible vitamin combinations
    vitamins_combinations = [
        'A', 'B', 'C', 'AB', 'AC', 'BC', 'ABC'
    ]
    # Initialize the minimum price to a large number
    min_total_price = float('inf')
    for comb1 in vitamins_combinations:
        for comb2 in vitamins_combinations:
            for comb3 in vitamins_combinations:
                combined = set(comb1 + comb2 + comb3)
                # If the combination covers all vitamins
                if 'A' in combined and 'B' in combined and 'C' in combined:
                    # Calculate the total price of this combination
                    price = sum(min_price.get(comb, float('inf')) for comb in (comb1, comb2, comb3))
                    # Update the minimum price
                    min_total_price = min(min_total_price, price)
    return min_total_price if min_total_price != float('inf') else -1

def main():
    n, juices = read_input()
    min_price = preprocess_juices(juices)
    result = find_min_price(min_price)
    print(result)

if __name__ == "__main__":
    main()
