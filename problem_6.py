class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    # Your Solution Here
    list_result = LinkedList()
    if llist_1 is None:
        llist_1 = []
    if llist_2 is None:
        llist_2 = []
    ld = list_dict(llist_1, llist_2)
    for key in ld:
        list_result.append(key)
    if list_result.head is None:
        return None
    return list_result


def intersection(llist_1, llist_2):
    # Your Solution Here
    if llist_1 is None:
        llist_1 = []
    if llist_2 is None:
        llist_2 = []
    list_result = LinkedList()
    ld = list_dict(llist_1, llist_2)
    for key in ld:
        if ld[key] == 2:
            list_result.append(key)
    if list_result.head is None:
        return None
    return list_result


def list_dict(llist_1, llist_2):
    list_dict1 = dict({})
    list_dict2 = dict({})
    node1 = llist_1.head
    while (node1):
        if node1.value not in list_dict1:
            list_dict1[node1.value] = 1
        node1 = node1.next

    node2 = llist_2.head
    while (node2):
        if node2.value not in list_dict2:
            list_dict2[node2.value] = 1
            if node2.value in list_dict1:
                list_dict1[node2.value] += 1
            else:
                list_dict1[node2.value] = 1
        node2 = node2.next
    return list_dict1


def test(element_1, element_2):
    if element_1 is None:
        element_1 = []
    if element_2 is None:
        element_2 = []
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()
    for i in element_1:
        linked_list_1.append(i)
    for i in element_2:
        linked_list_2.append(i)
    print("Union Set:")
    print(union(linked_list_1, linked_list_2))
    print("Intersection Set:")
    print(intersection(linked_list_1, linked_list_2))


# Test case 1
print("----------------------Test 1------------------------")
element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]
test(element_1,element_2)


# Test case 2
print("----------------------Test 2------------------------")
element_1 = [1,1,1,1,1,1,1]
element_2 = [2,3,4,5,6]
test(element_1,element_2)


# Test case 3
print("----------------------Test 3------------------------")
element_1 = None
element_2 = None
test(element_1, element_2)



# Test case 4
print("----------------------Test 4------------------------")
element_1 = [1,1,1,1,1,1,1]
element_2 = None
test(element_1, element_2)

