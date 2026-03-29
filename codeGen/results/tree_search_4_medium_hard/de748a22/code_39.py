import heapq

def min_removals():
    n, q = map(int, input().split())
    signs = list(input())

    pq = [(0, 0, n-1)] # (sign_sum, left, right)
    result = []

    for _ in range(q):
        l, r = map(int, input().split())
        while pq and pq[0][2] < l:
            heapq.heappop(pq)

        left, right, sign_sum = pq[0]
        if signs[l-1] == '+':
            sign_sum -= 1
        else:
            sign_sum += 1

        while pq and pq[-1][1] <= l:
            heapq.heappop(pq)

        new_left, right, new_sign_sum = pq[0]
        if signs[r] == '+':
            new_sign_sum -= 1
        else:
            new_sign_sum += 1

        if sign_sum * new_sign_sum < 0:
            result.append(min(r-l+1, abs(sign_sum)))
        elif sign_sum == 0:
            result.append(0)
        else:
            result.append(abs(sign_sum))

        while pq and pq[0][2] <= r:
            left, right, sign_sum = pq[0]
            if signs[right] == '+':
                sign_sum -= 1
            else:
                sign_sum += 1

            heapq.heappush(pq, (sign_sum, left+1, right))

    print(*result, sep='\n')

if __name__ == "__main__":
    min_removals()
