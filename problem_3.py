import sys


class MinHeapTree:
    """
    A helper structure to store the node.
    The property of this structure is: The value of parent node is always smaller than the
    values of child nodes.
    In order to maintain the property, there are two helper function named heapify_down and heapify up.

    The nodes in MinHeapTree are stored in a list following with the rule:
        if the index of parent node is i, the index of child node is 2*i+1 and 2*i+2
    """

    def __init__(self, data_str=None):
        self.data = list()
        if data_str is not None:
            char_dict = char_frequency(data_str)
            for c in char_dict:
                new_node = Node(c, char_dict[c])
                self.push(new_node)

    def heapify_down(self, index):
        """
        A function to maintain the property of min heap
        :param index: The index node need to be adjust
        """
        min_index = index

        for c in [index * 2 + 1, index * 2 + 2]:
            if c < len(self.data) and self.data[c].freq < self.data[min_index].freq:
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
        if self.data[index].freq < self.data[parent_index].freq:
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


class Node(object):
    def __init__(self, char="", freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
        self.visited = 0

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None

    def has_unvisited_left_child(self):
        if self.has_left_child():
            if self.get_left_child().visited == 0:
                return True
        return False

    def has_unvisited_right_child(self):
        if self.has_right_child():
            if self.get_right_child().visited == 0:
                return True
        return False


class HuffmanTree:
    def __init__(self, node=None):
        self.root = node


def huffman_encoding(data):
    min_heap_tree = MinHeapTree(data)
    huffman_tree = HuffmanTree()
    while len(min_heap_tree.data) != 1:
        node1 = min_heap_tree.pop()
        node2 = min_heap_tree.pop()
        # print("Node1={}, Node2={}".format(node1.freq,node2.freq))
        new_node = Node(None, node1.freq + node2.freq)
        new_node.left = node1
        new_node.right = node2
        min_heap_tree.push(new_node)
        # for d in min_heap_tree.data:
        #     print(d.freq)
        # print("____________")
        huffman_tree.root = new_node

    root_node = huffman_tree.root
    code_dict = dict({})
    while root_node.visited == 0:
        code_str = ""
        current_node = root_node
        while current_node.visited == 0:
            if current_node.has_unvisited_left_child():
                code_str += "0"
                current_node = current_node.get_left_child()
            elif current_node.has_unvisited_right_child():
                code_str += "1"
                current_node = current_node.get_right_child()
            else:
                current_node.visited = 1
            if current_node.char != "" and current_node.char is not None:
                code_dict[current_node.char] = code_str

    # print(code_dict)
    encoded_data = ""
    for c in data:
        encoded_data += code_dict[c]

    return encoded_data, huffman_tree


def huffman_decoding(data, tree):
    result = ""
    node = tree.root
    for c in data:
        i = int(c)
        if i == 0:
            node = node.left
        else:
            node = node.right
        if node.char is not None:
            result += node.char
            node = tree.root

    return result


def char_frequency(data):
    char_dict = dict({})
    for char in data:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def test(data, index):
    print("****************Test {}********************\n".format(index))
    if data == "" or data is None:
        print("Error, please input a valid string")
        return -1
    a_great_sentence = data
    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))
    encoded_data, tree = huffman_encoding(a_great_sentence)
    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))


if __name__ == "__main__":
    # Test 1: Default
    test("The bird is the word", 1)
    # Test 2: None
    test("", 2)  # Error, please input a valid string
    # Test 3: a long sentence with lots of consecutive chars
    test("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBCCCCCCCCCCCCCCCCCCCCCCC", 3)
    # Test 4: a long sentence with no repeat char
    test("0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_+[]{}:;<>,.?", 4)
