def can_send_over_network():
    t = int(input())
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        
        # Check if any segment in b is longer than 9 (max length of a digit)
        if any(len(str(i)) > 1 for i in b):
            print("NO")
        else:
            print("YES")

if __name__ == "__main__":
    can_send_over_network()
