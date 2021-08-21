class DoublyLinkedListNode:
    """
    This is a doubly linked list node structure in order to keep track on the order of nodes
    """

    def __init__(self, key, value, front=None, next=None):
        self.key = key
        self.value = value
        self.front = front
        self.next = next


class LRU_Cache(object):
    def __init__(self, capacity=5):
        self.dict = dict({})
        self.capacity = capacity
        self.head = DoublyLinkedListNode(None, None)
        self.tail = DoublyLinkedListNode(None, None)
        self.head.next = self.tail
        self.tail.front = self.head

    def __str__(self):
        out_string = ""
        node = self.head
        out_string += "---Head---\n"
        node = node.next
        while node:
            if node.key is None and node.value is None:
                out_string += "---Tail---"
            else:
                out_string += "[key: {}, value: {}]\n".format(node.key, node.value)
            node = node.next
        return out_string

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key is None:
            return -1
        if key in self.dict:
            target_node = self.dict[key]
            # Move the code to the head
            self.add_node_at_head(target_node.key, target_node.value)
            # Re-linked
            target_node.front.next = target_node.next
            target_node.next.front = target_node.front
            target_node.front = None
            target_node.next = None
            return target_node.value
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key is None and value is None:
            print("Error, key and value are None\n")
            return
        if key in self.dict:
            self.dict[key].value = value
            self.get(key)
            return
        if len(self.dict) >= self.capacity:
            self.dele_last_node()
        self.add_node_at_head(key, value)

    def add_node_at_head(self, key, value):
        """
        This is the helper function add a node at the head of linked list
        """
        new_node = DoublyLinkedListNode(key, value)
        temp_node = self.head.next
        new_node.next = temp_node
        temp_node.front = new_node
        self.head.next = new_node
        new_node.front = self.head
        self.dict[key] = new_node

    def dele_last_node(self):
        """
        Delete the last node in the linked list
        """
        last_key = self.tail.front.key
        del self.dict[last_key]
        self.tail.front = self.tail.front.front
        self.tail.front.next = self.tail


# Test 1: default test
def test1():
    print("--------------------------Test 1 ------------------------------")
    our_cache = LRU_Cache(5)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)

    print(our_cache.get(1))  # returns 1
    print(our_cache.get(2))  # returns 2
    print(our_cache.get(9))  # returns -1 because 9 is not present in the cache

    our_cache.set(5, 5)
    our_cache.set(6, 6)

    print(
        our_cache.get(3))  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

    print(our_cache)
    """
    ---Head---
    [key: 6, value: 6]
    [key: 5, value: 5]
    [key: 2, value: 2]
    [key: 1, value: 1]
    [key: 4, value: 4]
    ---Tail---
    """


# Test 2: None input
def test2():
    print("--------------------------Test 2 ------------------------------")
    our_cache = LRU_Cache(5)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(None, None)  # Error, key and value are None
    print(our_cache.get(None)) # -1
    our_cache.set(5, 5)
    our_cache.set(6, 6)
    print(our_cache)
    """
    ---Head---
    [key: 6, value: 6]
    [key: 5, value: 5]
    [key: 3, value: 3]
    [key: 2, value: 2]
    [key: 1, value: 1]
    ---Tail---
    """


# Repeat key
def test3():
    print("--------------------------Test 3 ------------------------------")
    our_cache = LRU_Cache(5)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    print(our_cache)
    # ---Head---
    # [key: 3, value: 3]
    # [key: 2, value: 2]
    # [key: 1, value: 1]
    # ---Tail---

    our_cache.set(3, 1)
    our_cache.set(1, 2)
    our_cache.set(2, 3)
    print(our_cache)
    # ---Head---
    # [key: 2, value: 3]
    # [key: 1, value: 2]
    # [key: 3, value: 1]
    # ---Tail---

    our_cache.set(1, 10)
    our_cache.set(2, 20)
    our_cache.set(3, 30)
    print(our_cache)
    # ---Head---
    # [key: 3, value: 30]
    # [key: 2, value: 20]
    # [key: 1, value: 10]
    # ---Tail---


test1()
test2()
test3()
