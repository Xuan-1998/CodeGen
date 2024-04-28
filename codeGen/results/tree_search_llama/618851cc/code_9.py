n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

# Sort both arrays
A.sort()
B.sort()

# Initialize pointers for both arrays
i = j = 0

while i < n and j < m:
    # Calculate the sum of the current elements in A and B
    total = A[i] + B[j]

    if total not in A and total not in B:
        print(A[i], B[j])
        break

    # If the total is less than any element in A, increment i
    elif total < A[i]:
        j += 1

    # If the total is greater than any element in B, increment j
    else:
        i += 1


