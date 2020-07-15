"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
        pass

    def __str__(self):
        return str(self.value)
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def print_list(self):
        cur = self.head
        print('Nodes in DLL: ')
        while cur:
            print(cur.value)
            cur = cur.next
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        pass
        # create instance of ListNode with value
        new_node = ListNode(value)
        # if DLL is empty
        if self.length == 0:
            # set head and tail to the new node instance
            self.head = new_node
            self.tail = new_node
        # if DLL is not empty
        if self.length > 0:
            # set new node's next to current head
            # set head's prev to new node
            # set head to the new node
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        # increment the DLL length attribute
        self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        pass
        # store the value of the head
        old_head = self.head.value
        # decrement the length of the DLL
        self.length -= 1
        # delete the head
        # if head.next is not None
        if self.head.next is not None:
            # set .next's prev to None
            self.head.next.prev = None
            # set head to head.next
            self.head = head.next
        # else (if head.next is None)
        elif self.head.next is None:
            # set head to None
            self.head = None
            # set tail to None
            self.tail = None
        # return the value
        return old_head

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        pass
        # create instance of ListNode with value
        new_node = ListNode(value)
        # if DLL is empty
        if self.length == 0:
            self.head,self.tail = new_node,new_node
            # set head and tail to the new node instance
        # if DLL is not empty
        if self.length > 0:
            # set new node's prev to current tail
            # set tail's next to new node
            # set tail to the new node
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        # increment the DLL length attribute
        self.length += 1

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        pass
        # store the value of the tail
        old_tail = self.tail.value
        # decrement the length of the DLL
        self.length -= 1
        # delete the tail
        # if tail.prev is not None
        if self.tail.prev is not None:
            # set tail.prev's next to None
            self.tail.prev.next = None
            # set tail to tail.prev
            self.tail = tail.prev
        # else (if tail.prev is None)
        elif self.tail.prev is None:
            # set head to None
            self.head = None
            # set tail to None
            self.tail = None
        # return the value
        return old_tail
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        pass
        self.node = node
        # if already head 
        if self.head is self.node:
            # none
            return None
        # if tail
        if self.tail is self.node:
            # set previous to tail
            self.tail = self.tail.prev
        # change previous next to current next
        self.node.prev.next = self.node.next
        # if current next is not None
        if self.node.next is not None:
            # change next previous to current previous
            self.node.next.prev = self.node.prev
        # remove previous on head
        self.node.prev = None
        # make next the current head
        self.node.next = self.head
        # change head prev to new head
        self.head.prev = self.node
        # change head to current node
        self.head = self.node

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass
        self.node = node
        # if already tail 
        if self.tail is self.node:
            # none
            return None
        # if head
        if self.head is self.node:
            # set next head to new head
            self.head = self.head.next
        # change next previous to current previous
        self.node.next.prev = self.node.prev
        # if previous is not None
        if self.node.prev is not None:
            # change previous next to current next
            self.node.prev.next = self.node.next
        # remove next on tail
        self.node.next = None
        # make prev the current tail
        self.node.prev = self.tail
        # change tail prev to new tail
        self.tail.next = self.node
        # change tail to current node
        self.tail = self.node

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        pass
        self.node = node
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head, self.tail = None, None
        else:
            if self.node is self.head:
                self.node.next.prev = self.node.prev
                self.head = self.node.next
            elif self.node is self.tail:
                self.node.prev.next = self.node.next
                self.tail = self.node.prev
            else:
                self.node.next.prev = self.node.prev
                self.node.prev.next = self.node.next
        self.length -= 1
        

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass
        if self.head is None:
            return None
        maximum = self.head.value
        current = self.head
        while current.next:
            if current.next.value > maximum:
                maximum = current.next.value
            current = current.next
        return maximum

LL = DoublyLinkedList()
gav = LL.add_to_head(ListNode('Gavin'))
LL.print_list()