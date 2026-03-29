from collections import defaultdict

def zookeeper(q):
    memo = defaultdict(bool)
    
    for _ in range(q):
        u, v = map(int, input().split())
        
        if u & v == v:
            print("YES")
        else:
            dp_u = False
            
            for w in range(2**30): 
                if u & w == w and memo[w]:
                    dp_u = True
                    break
                
            if not dp_u:
                print("NO")
