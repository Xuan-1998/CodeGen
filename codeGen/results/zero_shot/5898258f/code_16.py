import sys

def solve():
    T = int(input())
    for _ in range(T):
        N, X = map(int, input().split())
        A = list(map(int, input().split()))
        
        # Counting sort to count the occurrences of each possible value
        counts = [0] * (2*10**9 + 1)
        for a in A:
            counts[a] += 1
        
        max_value = 0
        for i in range(2*10**9 + 1):
            if counts[i]:
                max_value = max(max_value, min(N - 1, counts[i]) * X + i * sum(counts[j] for j in range(i+1)))

        print(max_value)

if __name__ == "__main__":
    solve()
