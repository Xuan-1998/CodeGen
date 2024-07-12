def max_remaining_element(n, arr):
    if n == 1:
        return arr[0]

    arr.sort(reverse=True)
    result = arr[0]

    for i in range(1, n):
        result -= arr[i]

    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    arr = list(map(int, data[1:]))
    print(max_remaining_element(n, arr))

