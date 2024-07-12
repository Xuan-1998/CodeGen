python
def max_remaining_element(n, arr):
    if n == 1:
        return arr[0]
    
    total_sum = sum(abs(x) for x in arr)
    min_abs_value = min(abs(x) for x in arr)
    negative_count = sum(1 for x in arr if x < 0)
    
    if negative_count % 2 == 0:
        return total_sum
    else:
        return total_sum - 2 * min_abs_value

# Reading input
import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
arr = list(map(int, data[1:]))

# Calculating the maximum remaining element
result = max_remaining_element(n, arr)
print(result)

