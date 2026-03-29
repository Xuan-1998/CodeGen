def can_send_sequence(t):
    t_cases = int(input())
    for _ in range(t_cases):
        n = int(input())
        b = list(map(int, input().split()))
        
        # Initialize an empty sequence a
        a = []
        
        # Iterate through the sequence b
        for i, bi in enumerate(b):
            # Check if bi can be obtained from a segment in a
            found = False
            j = 0
            while j < len(a) and not found:
                aj = len(str(a[j]))
                if aj == bi:
                    found = True
                    break
                elif aj > bi:
                    break
                j += 1
            
            # If bi cannot be obtained, we can't send b over the network
            if not found:
                print("NO")
                break
        else:  # if no break, it means all elements in b were found
            print("YES")

# Read the number of test cases
t = int(input())

can_send_sequence(t)
