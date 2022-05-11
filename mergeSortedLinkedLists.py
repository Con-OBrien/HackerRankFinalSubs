#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Since we are traversing through two lists fully, the time complexity is 0(m+n) where m and n are the lengths of the two lists
def mergeLists(head1, head2):
    print(head1, head2)
    # 1. Initialize dummy node using pre provided method to store result
    dummyNode = SinglyLinkedListNode(0)
    # tail will store the last node
    tail = dummyNode

    while True:
        # If any of list is empty, directly join all the elements of the other list
        if head1 is None:
            # set next value in tail to be head2
            tail.next = head2
            break
        if head2 is None:
            # set next value in tail to be head1
            tail.next = head1
            break

        # Compare the head data values, if head1 is smaller, the tail is appended and the head is changed
        if head1.data <= head2.data:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        # Once values have been analysed, go to next val and advance tail until break point
        tail = tail.next
    # Return the head of the merged list
    return dummyNode.next
