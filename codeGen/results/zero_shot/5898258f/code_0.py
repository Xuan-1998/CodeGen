import sys

def solve():
    T = int(input())
    for _ in range(T):
        N, X = map(int, input().split())
        A = list(map(int, input().split()))
        max_xor_sum = 0
        for i in range(1, N):
            max_xor_sum += A[i-1] ^ A[i]
        
        # Check if adding X to all elements gives the maximum value
        if max_xor_sum <= X:
            print(max_xor_sum)
        else:
            # Find the maximum subsequence sum that can be obtained by adding X to at most one subsequence
            max_subseq_sum = 0
            for i in range(1, N):
                max_subseq_sum += A[i-1] ^ A[i]
                if max_subseq_sum > X:
                    break
            
            # Add X to as many elements as possible
            remaining_xor_sum = max_xor_sum - max_subseq_sum
            if remaining_xor_sum <= X:
                print(max_subseq_sum + remaining_xor_sum)
            else:
                print(X)

if __name__ == "__main__":
    solve()
