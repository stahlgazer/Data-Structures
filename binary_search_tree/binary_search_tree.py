"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from stack import Stack
from queue import Queue


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.value}"

    # Insert the given value into the tree
    def insert(self, value):
        # Case 1: value is less than self.value
        if value < self.value:
            # If there is no left child, insert value here
            if self.left is None:
               self.left = BSTNode(value)
            else:
                # Repeat the process on left subtree
                self.left.insert(value)

        # Case 2: value is greater than or equal self.value
        elif value >= self.value:
            # If there is no right child, insert value here
            if self.right is None:
               self.right = BSTNode(value)
            else:
                # Repeat the process on right subtree
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Case 1: self.value is equal to the target
        if self.value == target:
            return True
        # Case 2: target is less than self.value 
        if target < self.value:
            # if self.left is None, it isn't in the tree
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        # Case 3: otherwise
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # forget about the left subtree
        if self.right is not None:
            # iterate through the nodes using a loop construct
            return self.right.get_max()
        # no self.right means its the maximum   
        else: return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.right is not None:
            self.right.for_each(fn)
        if self.left is not None:
            self.left.for_each(fn)
        else: 
            pass

# Part 2 -----------------------
    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node=None):
        # if the current node is None
        # we know we've reached the end of a recursion
        # (base case) we want to return
        if self is None:
            return

        # check if we can "move left"
        if self.left is not None:
            self.left.in_order_print()

        # visit the node by printing its value
        print(self.value)

        # check if we can "move right"
        if self.right is not None:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node=None):
        # You should import the queue class from earlier in the
        # week and use that class to implement this method
        # Use a queue to form a "line" 
        # for the nodes to "get in"
        # start by placing the root in the queue:
        line = Queue()
        line.enqueue(self)
        # need a while loop to iterate:
        # what are we checking in the while statement?
        # while length of queue is greater than 0
        while len(line) > 0:
            # dequeue item from front of queue
            removed = line.dequeue()
            # print that item
            print(removed.value)
            # place current item's left node in queue if not None
            if removed.left is not None:
                line.enqueue(removed.left)
            # place current item's right node in queue if not None
            if removed.right is not None:
                line.enqueue(removed.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node=None):
        pass
        # initialize an empty stack
        stack = []
        # push the root node onto the stack
        stack.append(self)
        # need a while loop to manager our iteration
        # if stack is not empty enter the while loop
        while len(stack) > 0:
            # pop top item off the stack
            current = stack.pop()
            # print that item's value
            print(current)

            # if there is a right subtree
            if current.right:
                # append right item onto the stack
                stack.append(current.right)
                
            # if there is a left subtree
            if current.left:
                # append left item onto the stack
                stack.append(current.left)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


tree = BSTNode(1)
tree.insert(7)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.in_order_print()
print(tree.contains(2))
tree.dft_print()
print(tree.contains(1))
tree.bft_print()