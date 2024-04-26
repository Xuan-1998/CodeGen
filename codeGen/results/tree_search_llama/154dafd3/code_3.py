import sys

def round_to_multiple_of_5(numbers):
    result = []
    for num in numbers.split(','):
        num = float(num.strip())
        diff = abs(int(num) - num)
        if diff < 0.05:  # within 0.01 of the nearest multiple of 5
            rounded_num = int(num)
        elif num > 0:
            rounded_num = round(num / 5) * 5 + 5
        else:
            rounded_num = round(num / 5) * 5 - 5
        result.append(str(rounded_num))
    return ','.join(result)

numbers = input().strip()
print(round_to_multiple_of_5(numbers))
