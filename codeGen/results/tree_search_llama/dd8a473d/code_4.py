class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def stringify(head):
    if head is None:
        return "null"

    result = str(head.value) + " -> "
    
    if head.next is not None:
        result += stringify(head.next)
    
    return result

# Example usage:
head = Node(1)
node2 = Node(2)
node3 = Node(3)

head.next = node2
node2.next = node3

print(stringify(head))  # Output: "1 -> 2 -> 3 -> null"
