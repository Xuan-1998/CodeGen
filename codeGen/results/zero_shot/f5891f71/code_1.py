def max_remaining_element(n, arr):
    if n == 1:
        return arr[0]
    
    abs_sum = sum(abs(x) for x in arr)
    min_abs_value = min(abs(x) for x in arr)
    negative_count = sum(1 for x in arr if x < 0)
    
    if negative_count % 2 == 0:
        return abs_sum
    else:
        return abs_sum - 2 * min_abs_value

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    arr = list(map(int, data[1:]))
    
    print(max_remaining_element(n, arr))

