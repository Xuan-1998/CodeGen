def stringify(head):
    result = []
    while head is not None:
        result.append(str(head.value))
        head = head.next
    return ' -> '.join(result) + 'null'

# Example usage:
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

print(stringify(head))  # Output: "1 -> 2 -> 3null"
