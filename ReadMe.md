# Data Structure & Algorithm Project 2

This is project 2 of Udacity's nanoprogram: Data Structure and Algorithm



## Problem 1: LRU Cache

In this code, I used a combination of a doubly linked list and a dictionary to store the data. 

Note: Since the usage of a dictionary, the key of each data is unique. So, when the key is repeat, the old value of the key will be replaced, and the new data will show up at the head of the list.

**Time Complexity:** O(1), since the functions get and set are independent with the input size

**Space Complexity**: O(n) where n is the input size



## Problem 2: Finding Files

This goal of this function is to find all files under a directory that has a suffix (e.g. ".c")

I used a recursion to complete this problem

**Time Complexity:** O(d*n) where d is the deep of the dictionary (avg.) and n is the number of files in each level (avg.)

**Space Complxity**: same with time complexity



## Problem 3: Huffman Coding

This goal of this problem is to design and implement the encoder and decoder of Huffman Code.

There are several parts in this code

##### 1. MinHeapTree Structure

First, I used a minheap structure. The property of this structure is: The value of parent node is always smaller than the values of child nodes. In order to maintain the property, there are two helper function named **heapify_down** and **heapify_up.**

The nodes in MinHeapTree are stored in a list following with the rule: if the index of parent node is i, the index of child node is 2*i+1 and 2*i+2

function **pop():**

Since we always want to get the min value in the list. the min value is at index 0
           1. we replace the value of index 0 and index -1
           2. use list's pop function get the min value and remove it from the list
           3. heapify down the node at index 0

function **push():**

1. At a new node at the end of the list
2. Heapify up the new node

**Time Complexity:** Both functions **heapify_up()** and **heapify_down()** has time complexity O(log(n)). In functions **pop() **and **push()**, the insert and pop is O(1). After insertion/pop, the  **heapify_up() / heapify_down()** is called, so the entire time complexity is O(log(n))

**Space Complexity:** Same with Time Complexity

##### 2. Node Structure

This is just the foundation node structure with some simple helper function

##### 3. HuffmanTree Stucture

This is a simple structure just save the root of the Huffman tree

##### 4. A helper function: char_frequency()

This is a helper function to calculate the char frequencies in the string. The time and space complexities are both O(n)

##### 5. huffman_encoding function

1. Call function **char_frequency()** (Time & Space Complexity O(n) )
2. Generate the min heap based on char frequencies (Time & Space Complexity O(nlogn) )
3. Generate Huffman Tree (Time & Space Complexity O(n) )
4. traverse the Huffman Tree and generate encoded string for each char: use depth first search, and store and encoded sequence into a dictionary
5. encode the data based on the dictionary

##### 6. huffman_decoding function

​	Decoding the data based on Huffman Tree

​	**Time & Space Complexity:** O(nlogn)



## Problem 4: Active Directory

The goal of this problem is to look up whether the user is in a group

I used a recursive structure similar with problem 2

**Time Complexity:** O(d*n) where d is the avg. depth of the groups and n is the avg. number of groups and files in each level

**Space Complexity**: Same with time complexity



## Problem 5: Blockchain

The goal of this problem is to implement a blockchain structure.

I just follow the instruction.



## Problem 6: Union and Intersection of Two Linked Lists

The goal of this problem is to find union and intersection set of two sets with the format of input is linked list.

I just traverse the two linked list and same the items in dictionary. If the item appears in both lists, its value in dict is 2, if only appears in one of the lists, its value is 1 (Also avoid the repeat number in one list)

For union, print all items in the dict,

for intersection, only print item with value 2

