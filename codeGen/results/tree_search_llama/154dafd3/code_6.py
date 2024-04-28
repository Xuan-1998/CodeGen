def round_to_nearest_multiple_of_five(arr):
    return [round(num / 5) * 5 for num in arr]

# Read input array from stdin
n = int(input())
arr = [float(input()) for _ in range(n)]

# Round each number to the nearest multiple of 5
rounded_arr = round_to_nearest_multiple_of_five(arr)

# Print the rounded array to stdout
for num in rounded_arr:
    print(num)
