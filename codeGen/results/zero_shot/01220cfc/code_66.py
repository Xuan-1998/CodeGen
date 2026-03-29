def can_reach_last_index(arr):
    max_reach = 0
    for i in range(len(arr)):
        jump_length = min(i + arr[i], len(arr) - 1)
        if jump_length >= i:
            max_reach = i
        else:
            break
    return max_reach == len(arr) - 1

if __name__ == "__main__":
    n = int(input())  # Read the array length from stdin
    arr = [int(x) for x in input().split()]  # Read the array elements from stdin
    print(can_reach_last_index(arr))  # Print the result to stdout
