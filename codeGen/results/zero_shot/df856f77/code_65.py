from sys import stdin

def main():
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().split()))
    
    ops = 0
    for i in range(n - 1):
        if arr[i] >= arr[i+1]:
            ops += abs(arr[i] - arr[i+1]) + 1
    
    print(ops)

if __name__ == "__main__":
    main()
