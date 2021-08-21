class DoublyLinkedListNode:
    def __init__(self, key, value, front=None, next=None):
        self.key = key
        self.value = value
        self.front = front
        self.next = next


class LRU_Cache(object):
    def __init__(self, capacity=5):
        self.dict = dict({})
        self.capacity = capacity
        self.head = DoublyLinkedListNode(0, 0)
        self.tail = DoublyLinkedListNode(0, 0)
        self.head.next = self.tail
        self.tail.front = self.head

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.dict:
            target_node = self.dict[key]
            self.add_node_at_head(target_node.key, target_node.value)
            target_node.front.next = target_node.next
            target_node.next.front = target_node.front
            target_node.front = None
            target_node.next = None
            return target_node.value
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.

        if len(self.dict) >= self.capacity:
            self.dele_last_node()
        self.add_node_at_head(key, value)

    def add_node_at_head(self, key, value):
        new_node = DoublyLinkedListNode(key, value)
        temp_node = self.head.next
        new_node.next = temp_node
        temp_node.front = new_node
        self.head.next = new_node
        new_node.front = self.head
        self.dict[key] = new_node

    def dele_last_node(self):
        last_key = self.tail.front.key
        del self.dict[last_key]
        self.tail.front = self.tail.front.front
        self.tail.front.next = self.tail


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

print(our_cache.get(3))  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

for i in our_cache.dict:
    print(i, our_cache.dict[i].key, our_cache.dict[i].value)
