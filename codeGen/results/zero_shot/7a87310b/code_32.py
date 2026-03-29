import sys

def count_matrices():
    T = int(sys.stdin.readline())
    result = []
    
    for _ in range(T):
        N = int(sys.stdin.readline())
        count = 0
        
        for a in range(1, N//2+1):  # Only need to consider a <= N/2
            for d in range(-min(N-a, abs(a)), min(N-a, abs(a))+1):  
                b = N - a - d 
                c = a*d - b
                
                if c > 0 and a*d - b*c > 0:
                    count += 1
        
        result.append(str(count))
    
    sys.stdout.write('\n'.join(result))

count_matrices()
