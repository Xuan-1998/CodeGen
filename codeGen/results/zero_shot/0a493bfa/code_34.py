# Read input
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Sort bad primes in ascending order
b.sort()

# Initialize maximum beauty
max_beauty = 0

# Iterate over array elements
for i in range(n):
    # Calculate gcd of current element with others
    for j in range(i+1, n):
        a[j] = math.gcd(a[i], a[j])

# Update max beauty
max_beauty = sum(a)

print(max_beauty)
