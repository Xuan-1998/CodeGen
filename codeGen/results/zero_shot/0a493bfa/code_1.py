# Step 1: Read input
n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

# Step 2: Initialize a dictionary to store the beauty of each number in the array
beauty_dict = {i: i for i in arr}

# Step 3: Iterate over all pairs of numbers in the array and update their beauty accordingly
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        gcd = find_gcd(arr[i], arr[j])
        beauty_dict[arr[i]] += gcd
        beauty_dict[arr[j]] -= gcd

# Step 4: Find the maximum beauty of the array by iterating over all numbers and their beauty
max_beauty = max(beauty_dict.values())

print(max_beauty)
