from typing import List

def partition_palindromic(s: str) -> List[List[str]]:
    def is_palindrome(sub_string: str) -> bool:
        return sub_string == sub_string[::-1]

    def generate_partitions(current_partition: List[str], remaining_chars: str) -> List[List[str]]:
        if not remaining_chars:
            return [current_partition]
        
        partitions = []
        for i in range(1, len(remaining_chars) + 1):
            prefix = remaining_chars[:i]
            if is_palindrome(prefix):
                partitions.extend(generate_partitions(current_partition + [prefix], remaining_chars[i:]))
        
        return partitions

    partitions = generate_partitions([], s)
    return partitions

if __name__ == "__main__":
    n = int(input())
    s = input()
    result = partition_palindromic(s)
    for p in result:
        print(p)
