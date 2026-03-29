def positive_invertible_matrices(N):
    memo = {0: 1}  # Base case: trace 0 has only one invertible matrix (identity)
    
    for t in range(1, N + 1):  # Iterate over possible trace values
        a_count = 0
        b_count = 0
        
        for a in range(t // 2 + 1):
            if t - a >= a:
                b_count = memo.get(t - a, 0)
            else:
                b_count = memo[t - a]
            
            a_count += memo.get(a, 0) * b_count
        
        memo[t] = a_count
    
    positive_det_count = sum(1 for count in memo.values() if count > 0 and all((a + b <= N // 2 or b >= N // 2) for a, (b, _) in [(m[0][0], m[0][1]) for m in [[*map(int, line.split()), *[list(map(int, map(str.strip, row.split())))] for row in [line.split()]][0]] if m[0][0] + m[0][1] == N and all(x > 0 for x in m)])
    
    return positive_det_count

T = int(input())
for _ in range(T):
    N = int(input())
    if not (3 <= N <= 25000): 
        raise ValueError("Invalid input")
    print(positive_invertible_matrices(N))
