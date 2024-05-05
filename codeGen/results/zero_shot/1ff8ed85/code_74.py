def can_send_over_network():
    t = int(input())  # number of test cases
    for _ in range(t):
        n = int(input())
        sequence_b = list(map(int, input().split()))
        
        if not (1 <= n <= 2 * 10**5) or any(not (1 <= x <= 10**9) for x in sequence_b):
            print("NO")
        else:
            for b_i in sequence_b:
                found = False
                a_i = 0
                while a_i <= b_i:
                    if a_i == b_i:
                        print("YES")
                        return
                    a_i += 1
            print("NO")

can_send_over_network()
