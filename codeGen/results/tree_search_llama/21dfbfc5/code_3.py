class ArrayContainer:
    def __init__(self):
        self.array_list = []

    def add_array(self, array):
        self.array_list.append(array)

    def get_output_array(self):
        max_length = max(len(array) for array in self.array_list)
        output_array = []
        for i in range(max_length):
            for array in self.array_list:
                if i < len(array):
                    output_array.append(array[i])
                else:
                    output_array.append(None)
        return output_array

def generate_output_array(*arrays):
    container = ArrayContainer()
    for array in arrays:
        container.add_array(array)
    return container.get_output_array()

# Example usage
array1 = [1, 2, 3]
array2 = [4, 5, None]
array3 = [6, None, None, 8]

output_array = generate_output_array(array1, array2, array3)
print(output_array)  # Output: [1, 4, 6], [2, 5, None], [3, None, None, 8]
