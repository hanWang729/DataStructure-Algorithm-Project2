class MinHeapTree:
    """
    A helper structure to store the node.
    The property of this structure is: The value of parent node is always smaller than the
    values of child nodes.
    In order to maintain the property, there are two helper function named heapify_down and heapify up.

    The nodes in MinHeapTree are stored in a list following with the rule:
        if the index of parent node is i, the index of child node is 2*i+1 and 2*i+2
    """
    def __init__(self):
        self.data = list()

    def heapify_down(self, index):
        """
        A function to maintain the property of min heap
        :param index: The index node need to be adjust
        """
        min_index = index

        for c in [index * 2 + 1, index * 2 + 2]:
            if c < len(self.data) and self.data[c] > min_index:
                min_index = c
        if min_index == index:
            return
        self.data[index], self.data[min_index] = self.data[min_index], self.data[index]
        self.heapify_down(min_index)

    def heapify_up(self, index):
        """
        A function to maintain the property of min heap
        :param index: The index node need to be adjust
        """
        if index == 0:
            return
        parent_index = int((index - 1) / 2)
        if self.data[index] < self.data[parent_index]:
            self.data[index], self.data[parent_index] = self.data[parent_index], self.data[index]
            self.heapify_up(parent_index)

    # Return a min value and remove it from the heap
    def pop(self):
        """
        Since we always want to get the min value in the list. the min value is at index 0
        1. we replace the value of index 0 and index -1
        2. use list's pop function get the min value and remove it from the list
        3. heapify down the node at index 0
        """
        self.data[0], self.data[-1] = self.data[-1], self.data[0]
        result = self.data.pop()
        self.heapify_down(0)
        return result

    def push(self, new_node):
        """
        1. At a new node at the end of the list
        2. Heapify up the new node
        """
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
