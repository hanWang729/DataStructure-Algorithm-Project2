class MinHeapTree:
    def __init__(self):
        self.data = list()

    def heapify_down(self, index):
        min_index = index

        for c in [index * 2 + 1, index * 2 + 2]:
            if c < len(self.data) and self.data[c] > min_index:
                min_index = c
        if min_index == index:
            return
        self.data[index], self.data[min_index] = self.data[min_index], self.data[index]
        self.heapify_down(min_index)

    def heapify_up(self, index):
        if index == 0:
            return
        parent_index = int((index - 1) / 2)
        if self.data[index] < self.data[parent_index]:
            self.data[index], self.data[parent_index] = self.data[parent_index], self.data[index]
            self.heapify_up(parent_index)

    # Return a min value and remove it from the heap
    def pop(self):
        self.data[0], self.data[-1] = self.data[-1], self.data[0]
        result = self.data.pop()
        self.heapify_down(0)
        return result

    def push(self, new_node):
        # Add a new node into the data list
        self.data.append(new_node)
        # Maintain the min heap
        self.heapify_up(len(self.data) - 1)


tree = MinHeapTree()
tree.push(2)
print(tree.data)
tree.push(5)
print(tree.data)
tree.push(10)
print(tree.data)
print(tree.pop())
print(tree.data)
