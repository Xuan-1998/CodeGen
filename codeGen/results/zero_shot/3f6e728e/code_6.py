import sys

def x_sequences(N, M, U, L):
    # Sort radii in ascending order
    U.sort()
    L.sort()

    # Count unique radii
    unique_upper = len(set(U))
    unique_lower = len(set(L))

    # Calculate X-sequences
    return (1 + unique_upper) * (1 + unique_lower)

def main():
    T = int(input())
    
    for _ in range(T):
        N, M, C = map(int, input().split())
        U = list(map(int, input().split()))
        L = list(map(int, input().split()))

        sequences = x_sequences(N, M, U, L)
        
        print(sequences % (10**9 + 7))

if __name__ == "__main__":
    main()
