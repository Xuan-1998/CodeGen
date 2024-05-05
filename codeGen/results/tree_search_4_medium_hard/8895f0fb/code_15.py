import sys

def expected_carries():
    t = int(sys.stdin.readline().strip())
    
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        
        total_carries = 0
        
        for i in range(n):
            a, b = map(int, str(10**n - 1).zfill(n)[i].split()[0][::-1]), \
                   map(int, str(9*10**(n-1)).zfill(n)[i].split()[0][::-1])
            
            for j in range(len(a)):
                total_carries += (a[j] > b[j]) or (a[j] == 9 and b[j] > 0)
        
        print(float(total_carries) / float((10**n - 1)**2))
