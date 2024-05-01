def solve():
    s = input()
    
    for i in range(len(s) - 3):
        if s[i:i+2] == 'AB' and s[i+2:i+4] == 'BA':
            print("YES")
            return
        
    print("NO")

if __name__ == "__main__":
    solve()
