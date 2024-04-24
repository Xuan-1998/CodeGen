from itertools import combinations

def read_input():
    n = int(input())
    juices = [tuple(input().split()) for _ in range(n)]
    return n, juices

def preprocess_data(juices):
    min_prices = {'A': float('inf'), 'B': float('inf'), 'C': float('inf'),
                  'AB': float('inf'), 'AC': float('inf'), 'BC': float('inf'),
                  'ABC': float('inf')}
    for price, vitamins in juices:
        price = int(price)
        for i in range(1, 4):
            for combo in combinations(vitamins, i):
                key = ''.join(sorted(combo))
                min_prices[key] = min(min_prices[key], price)
    return min_prices

def find_minimum_price(min_prices):
    # Check single juice with all vitamins
    min_total_price = min_prices['ABC']
    
    # Check two juices combinations
    for combo in combinations('ABC', 2):
        key = ''.join(combo)
        min_total_price = min(min_total_price, min_prices[key] + min_prices[''.join(set('ABC') - set(combo))])
    
    # Check three juices combinations
    min_total_price = min(min_total_price, min_prices['A'] + min_prices['B'] + min_prices['C'])
    
    return min_total_price if min_total_price != float('inf') else -1

def main():
    n, juices = read_input()
    min_prices = preprocess_data(juices)
    result = find_minimum_price(min_prices)
    print(result)

if __name__ == "__main__":
    main()
