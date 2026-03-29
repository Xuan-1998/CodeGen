import sys

def solve():
    n, q = map(int, input().split())
    signs = list(input())

    prefix_sums = [0] * (n + 1)
    for i in range(n):
        prefix_sums[i + 1] = prefix_sums[i] + (-1 if signs[i] == '-' else 1)

    for _ in range(q):
        l, r = map(int, input().split())
        total_sum = prefix_sums[r] - prefix_sums[l]
        if total_sum != 0:
            # Use binary search to find the minimal number of elements that can be removed
            low, high = 1, r - l + 1
            while low <= high:
                mid = (low + high) // 2
                new_sum = prefix_sums[r] - prefix_sums[l + mid]
                if new_sum == 0:
                    break
                elif new_sum < 0:
                    low = mid + 1
                else:
                    high = mid - 1
            print(r - l - mid)
        else:
            print(0)

if __name__ == '__main__':
    solve()
