import sys

# Step 1: Parse the input
n = int(input())
juices = [tuple(input().split()) for _ in range(n)]
for i in range(n):
    price, vitamins = juices[i]
    juices[i] = (int(price), set(vitamins))

# Step 2: Create a table for minimum price for each vitamin combination
min_price = {'A': float('inf'), 'B': float('inf'), 'C': float('inf'),
             'AB': float('inf'), 'AC': float('inf'), 'BC': float('inf'),
             'ABC': float('inf')}

# Step 3: Update the table with the minimum price for each vitamin combination
for price, vitamins in juices:
    vitamin_combinations = [''.join(sorted(vitamins))]
    for vitamin in vitamins:
        vitamin_combinations.append(vitamin)
    for comb in vitamin_combinations:
        min_price[comb] = min(min_price[comb], price)

# Step 4: Calculate the minimum total price
min_total_price = float('inf')
# Considering all juices
min_total_price = min(min_total_price, min_price['ABC'])
# Considering pairs of juices
for comb1 in ['A', 'B', 'C']:
    for comb2 in ['AB', 'AC', 'BC']:
        if comb1 in comb2:
            continue
        min_total_price = min(min_total_price, min_price[comb1] + min_price[comb2])
# Considering three individual juices
min_total_price = min(min_total_price, min_price['A'] + min_price['B'] + min_price['C'])

# Step 5: Output the result
if min_total_price == float('inf'):
    print(-1)
else:
    print(min_total_price)
