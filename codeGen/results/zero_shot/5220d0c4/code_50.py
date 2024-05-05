max_beauty = 0
for num in arr:
    is_good_prime = is_prime(num)
    beauty = calculate_beauty(num, is_good_prime)
    if beauty > max_beauty:
        max_beauty = beauty

print(f"Maximum beauty: {max_beauty}")
