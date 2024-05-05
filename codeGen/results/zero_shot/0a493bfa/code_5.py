while prime_numbers:
    p = heapq.heappop(prime_numbers)
    # Apply operation based on whether p is a good prime or not
    if p not in b:
        # Good prime! Apply f(s) = f(s/p) + s
        pass
    else:
        # Bad prime! Apply f(s) = f(s/p) - s
        pass

print(max_beauty)  # Print the maximum beauty of the array
