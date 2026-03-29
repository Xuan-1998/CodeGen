def expectedCarries():
    T = int(input())
    for _ in range(T):
        N = int(input())
        dp_a = [0] * (N + 1)
        dp_b = [0] * (N + 1)
        
        # Calculate cumulative sum modulo 10 for each digit position in A
        a_sum = 0
        for i in range(N, -1, -1):
            a_sum += int(input()) * (10 ** i)
            dp_a[i] = a_sum % 10
        
        # Calculate cumulative sum modulo 10 for each digit position in B
        b_sum = 0
        for i in range(N, -1, -1):
            b_sum += int(input()) * (10 ** i)
            dp_b[i] = b_sum % 10
        
        # Calculate expected number of non-zero carries using DP tables
        expected_carries = 0.0
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if (dp_a[i] + dp_b[j]) % 10 != 0:
                    expected_carries += 1.0
        
        # Calculate expected value by dividing the number of carries by total number of pairs
        expected_value = expected_carries / ((N + 1) ** 2)
        
        print(f"{expected_value:.6f}")

if __name__ == "__main__":
    expectedCarries()
