def count_matrices():
    T = int(input())
    
    for _ in range(T):
        N = int(input())
        count = 0
        
        for i in range(1, N-1):
            # calculate the other element on the diagonal
            j = N - i
            
            # calculate the off-diagonal elements
            k = (N - i) // 2 if (N - i) % 2 == 0 else (N - i + 1) // 2
            l = (N - j) // 2 if (N - j) % 2 == 0 else (N - j + 1) // 2
            
            # calculate the determinant of the matrix
            det = i * j - k * l
            
            # count the matrices with positive determinant
            if det > 0:
                count += 1
        
        print(count)

count_matrices()
