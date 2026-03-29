def is_palindrome(s):
    return s == s[::-1]

def get_partitions(s, current_partition):
    if len(s) == 0:  
        return [current_partition]  

    partitions = []  
    for i in range(len(s)):  
        substring = s[:i+1]  
        if is_palindrome(substring):  
            new_partition = [substring] + current_partition  
            partitions.extend(get_partitions(s[i+1:], new_partition))  

    return partitions

if __name__ == "__main__":
    S = input()  
    partitions = get_partitions(S, [])
    for partition in partitions:
        print(partition)
