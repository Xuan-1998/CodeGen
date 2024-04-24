import sys

def read_input():
    n = int(input().strip())
    juices = [(int(price), set(vitamins)) for price, vitamins in (input().split() for _ in range(n))]
    return juices

def min_price_for_all_vitamins(juices):
    # Initialize minimum prices for each combination of vitamins
    min_price = {'A': float('inf'), 'B': float('inf'), 'C': float('inf'),
                 'AB': float('inf'), 'AC': float('inf'), 'BC': float('inf'),
                 'ABC': float('inf')}

    # Update minimum prices for each juice
    for price, vitamins in juices:
        vitamins_str = ''.join(sorted(vitamins))
        min_price[vitamins_str] = min(min_price[vitamins_str], price)
        
        # Update combinations
        for combo in list(min_price.keys()):
            new_combo = ''.join(sorted(set(combo + vitamins_str)))
            min_price[new_combo] = min(min_price[new_combo], min_price[combo] + price)

    # The answer is the minimum price for the combination 'ABC'
    return min_price['ABC'] if min_price['ABC'] != float('inf') else -1

def main():
    juices = read_input()
    result = min_price_for_all_vitamins(juices)
    print(result)

if __name__ == "__main__":
    main()
