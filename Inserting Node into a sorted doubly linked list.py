#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head, data):
    curr=head
    if curr.data>=data:
        node=DoublyLinkedListNode(data)
        node.prev=None
        node.next=curr
        return node
    prevnode=curr
    while curr!=None and curr.next!=None and curr.data<=data:
        prevnode=curr
        curr=curr.next
    if curr.next!=None:
        node=DoublyLinkedListNode(data)
        prevnode.next=node
        node.prev=prevnode
        node.next=curr
        curr.prev=node
    else:
        node=DoublyLinkedListNode(data)
        if data<curr.data:
            prevnode.next=node
            node.prev=prevnode
            node.next=curr
            curr.prev=node
        else:
            curr.next=node
            node.prev=curr
    return head
    
    
    
    
if __name__ == '__main__':
