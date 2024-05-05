def main():
    n, q = map(int, input().split())
    arr = list(input())

    for _ in range(q):
        l, r = map(int, input().split())
        prefix_sum = 0
        min_remove = float('inf')

        for i in range(l-1, r):
            if arr[i] == '+':
                prefix_sum += 1
            else:
                prefix_sum -= 1

            if prefix_sum == 0:
                min_remove = min(min_remove, i-l+1)
            elif prefix_sum < 0:
                min_remove = min(min_remove, r-i)

        print(min_remove)

if __name__ == "__main__":
    main()
