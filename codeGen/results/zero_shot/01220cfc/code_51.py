import sys

def main():
    n = int(input())
    jumps = list(map(int, input().split()))
    max_reachable = 0
    for i in range(n):
        if i > max_reachable:
            break
        max_reachable = max(max_reachable, min(i+jumps[i], n-1))
    
    print(max_reachable >= n-1)

if __name__ == "__main__":
    main()
