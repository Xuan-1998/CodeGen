n = int(input())
marks = list(map(int, input().split()))

# Sort the marks array
marks.sort()

# Initialize the minimum sum
min_sum = 0

# Calculate the cumulative sum of marks up to each day
cumulative_sum = 0
for i in range(n):
    cumulative_sum += marks[i]
    
    # Update the minimum sum if the current day's sum is smaller
    min_sum = min(min_sum, n - (i + 1) - cumulative_sum)

print(min_sum)
