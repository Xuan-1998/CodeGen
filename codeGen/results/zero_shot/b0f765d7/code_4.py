from sys import stdin

# Step 1: Parse the input
n = int(stdin.readline().strip())
juices = [tuple(stdin.readline().strip().split()) for _ in range(n)]
for i in range(n):
    juices[i] = (int(juices[i][0]), set(juices[i][1]))

# Step 2: Initialize the data structure for minimum prices
min_prices = {'A': float('inf'), 'B': float('inf'), 'C': float('inf'),
              'AB': float('inf'), 'AC': float('inf'), 'BC': float('inf'),
              'ABC': float('inf')}

# Step 3: Iterate over all juices and update the minimum prices
for price, vitamins in juices:
    # Update the price for the current vitamin combination
    comb = ''.join(sorted(vitamins))
    min_prices[comb] = min(min_prices[comb], price)
    
    # Update the prices for combinations that can be formed with this juice
    for existing_comb in list(min_prices.keys()):
        new_comb = ''.join(sorted(set(existing_comb) | vitamins))
        if new_comb != existing_comb:
            min_prices[new_comb] = min(min_prices[new_comb], min_prices[existing_comb] + price)

# Step 4: The answer is the minimum price for the combination 'ABC'
answer = min_prices['ABC'] if min_prices['ABC'] != float('inf') else -1

# Step 5: Print the answer
print(answer)
