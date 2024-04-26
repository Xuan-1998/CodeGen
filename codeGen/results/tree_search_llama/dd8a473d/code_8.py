class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def stringify(head):
    stack = []
    curr = head
    
    while curr:
        stack.append(curr.value)
        curr = curr.next

    result = "null"
    while stack:
        result = f"{stack.pop()} -> {result}"

    return result


# Example usage
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

head = node1
node1.next = node2
node2.next = node3

print(stringify(head))  # Output: 1 -> 2 -> 3 -> null
