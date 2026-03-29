# Receive input
n = int(input())
a = list(map(int, input().split()))

# Initialize count of good subsequences
good_subsequences_count = 0

for i in range(1, n + 1):
    # Check if there exists a subsequence with numbers divisible by i
    for j in range(n - (n // i) + 1):
        subsequence = [a[k] for k in range(j, j + n // i)]
        is_divisible = all(num % i == 0 for num in subsequence)
        if is_divisible:
            good_subsequences_count += 1

# Print the result
print(good_subsequences_count % (10**9 + 7))
