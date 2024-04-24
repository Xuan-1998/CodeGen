import sys

def min_price_for_vitamins(juices):
    # Initialize the minimum prices for each vitamin combination
    min_price = {
        'A': float('inf'),
        'B': float('inf'),
        'C': float('inf'),
        'AB': float('inf'),
        'AC': float('inf'),
        'BC': float('inf'),
        'ABC': float('inf')
    }

    # Update the minimum prices for each juice
    for price, vitamins in juices:
        # Update the price for the current combination of vitamins
        if price < min_price[vitamins]:
            min_price[vitamins] = price
        # Update the price for combinations with this juice
        for vitamin_combination in min_price.keys():
            combined_vitamins = ''.join(sorted(set(vitamin_combination + vitamins)))
            combined_price = min_price[vitamin_combination] + price
            if combined_price < min_price[combined_vitamins]:
                min_price[combined_vitamins] = combined_price

    # Check if it's possible to get all vitamins
    if min_price['ABC'] == float('inf'):
        # It's impossible to get all vitamins
        return -1
    else:
        # Return the minimum price for all vitamins
        return min_price['ABC']

# Read input from stdin
n = int(input().strip())
juices = []
for _ in range(n):
    price, vitamins = input().strip().split()
    price = int(price)
    vitamins = ''.join(sorted(vitamins))  # Sort the vitamins to maintain consistency
    juices.append((price, vitamins))

# Calculate and print the minimum price
min_total_price = min_price_for_vitamins(juices)
print(min_total_price)
