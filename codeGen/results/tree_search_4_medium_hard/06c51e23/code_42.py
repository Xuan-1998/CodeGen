import heapq

def solve():
    n, t = map(int, input().split())
    fraction = float(input())

    pq = [(0, 0)]
    memo = {(i, 0): 0 for i in range(n + 1)}

    while pq:
        curr_grade, curr_time = heapq.heappop(pq)

        if curr_time > t:
            continue

        i = n
        while i > 0 and fraction % (10 ** i) >= 1 / (10 ** i):
            i -= 1

        new_grade = curr_grade + 1 if i > 0 else curr_grade
        new_time = curr_time + int(10 ** i)

        if memo.get((i, new_time)) is None:
            heapq.heappush(pq, (new_grade, new_time))
            memo[(i, new_time)] = new_grade

    return str(max(memo.values()))

print(solve())
