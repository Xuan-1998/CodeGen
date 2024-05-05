# Step 1: Read the input
t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    
    # Step 2: Sort the sequence b
    b.sort()
    
    # Step 3: Check if the sequence can be obtained from another sequence a
    is_possible = False
    for i in range(len(b) - 1):
        if b[i + 1] - b[i] > 0:
            is_possible = True
            break
    
    # Step 4: Print the result
    print("YES" if is_possible else "NO")
