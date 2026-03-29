def solve():
    n, q = map(int, input().split())
    signs = list(input())

    for _ in range(q):
        l, r = map(int, input().split())
        prefix_sum = sum(signs[l-1:r])
        if prefix_sum == 0:
            print(0)
        else:
            # Find the first and last elements in the range where the sign-variable sum is zero
            start = l - 1
            end = r
            while start < end and signs[start] * (prefix_sum + signs[start+1]) <= 0:
                start += 1
            while start < end and signs[end-1] * (prefix_sum + signs[end-2]) <= 0:
                end -= 1
            # Count the number of elements in the range that need to be removed
            print(r - l + 1 - (end - start))
