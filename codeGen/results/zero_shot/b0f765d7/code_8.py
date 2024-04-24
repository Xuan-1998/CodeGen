import sys

def read_input():
    n = int(input().strip())
    juices = [tuple(input().strip().split()) for _ in range(n)]
    return n, juices

def preprocess(juices):
    # Initialize the mapping with infinity prices for all combinations
    min_prices = {'A': float('inf'), 'B': float('inf'), 'C': float('inf'),
                  'AB': float('inf'), 'AC': float('inf'), 'BC': float('inf'),
                  'ABC': float('inf')}
    for price, vitamins in juices:
        price = int(price)
        # Update the price for the current vitamin combination
        min_prices[vitamins] = min(min_prices.get(vitamins, float('inf')), price)
        # Update the prices for combinations that can be formed with current juice
        for comb in list(min_prices.keys()):
            new_comb = ''.join(sorted(set(comb + vitamins)))
            min_prices[new_comb] = min(min_prices.get(new_comb, float('inf')), min_prices[comb] + price)
    return min_prices

def find_minimum_price(min_prices):
    # Check for the price directly for all vitamins
    min_price = min_prices.get('ABC', float('inf'))
    # Check for combinations of two juices
    for comb1 in ['A', 'B', 'C']:
        for comb2 in ['AB', 'AC', 'BC']:
            if comb1 in comb2:  # They should cover all vitamins together
                min_price = min(min_price, min_prices[comb1] + min_prices[comb2])
    # Check for combinations of three juices
    min_price = min(min_price, min_prices['A'] + min_prices['B'] + min_prices['C'])
    return min_price if min_price != float('inf') else -1

# Main function to solve the problem
def main():
    n, juices = read_input()
    min_prices = preprocess(juices)
    result = find_minimum_price(min_prices)
    print(result)

if __name__ == "__main__":
    main()
