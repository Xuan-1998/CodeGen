def checkSubarraySum(arr: list[int], k: int) -> bool:
    n = len(arr)
    total_sum = 0
    remainder_map = {0: True}

    for i, num in enumerate(arr):
        total_sum += num
        remainder = (total_sum % k + k) % k
        if remainder in remainder_map:
            return True
        remainder_map[remainder] = True

    return False
