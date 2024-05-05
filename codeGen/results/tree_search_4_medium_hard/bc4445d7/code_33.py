import heapq

def solve(n, edges, m, prime_factors):
    dp = [[0] * (n + 1) for _ in range(31)]
    pq = [(0, 1)]  # priority queue to store the current maximum sum and node index
    max_sum = 0

    while pq:
        curr_sum, node = heapq.heappop(pq)
        if node > n:
            break

        for neighbor in edges[node]:
            if dp[30][neighbor] == 0:  # we haven't visited this node yet
                label = 1
                for i in range(5):
                    if prime_factors[i] <= curr_sum % (10**9 + 7) // (10 ** i):
                        label = i + 1
                        break
                dp[30][neighbor] = curr_sum + label * (10**29 + 7)
                heapq.heappush(pq, (dp[30][neighbor], neighbor))

    return sum(dp[30]) % (10**9 + 7)

# input and output handling
def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        edges = [[] for _ in range(n + 1)]
        m = int(input())
        prime_factors = list(map(int, input().split()))
        for _ in range(n - 1):
            u, v = map(int, input().split())
            edges[u].append(v)
            edges[v].append(u)

        print(solve(n, edges, m, prime_factors))

if __name__ == "__main__":
    main()
