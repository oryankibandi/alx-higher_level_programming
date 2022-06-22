#!/usr/bin/python3
"""
This module defines a Singly linked list
"""


class Node:
    def __init__(self, data, next_node=None):
        """
        Defines a node for a singly linked list

        Args:
            data (int): data of  the node
            next_node (Node): pointer to the next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        data getter
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        setter for the data attribute

        Args:
            value (int): value to be set
        """
        if type(value) != int:
            raise TypeError('data must be an integer')

        self.__data = value

    @property
    def next_node(self):
        """getter for the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        setter for the next node

        Args:
            value (node): next node
        """
        if value is not None and type(value) != Node:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        """Defines the singly linked list
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        inserts a new node in the linked list

        Args:
            value (Node): node to insert
        """
        if self.__head is None:
            self.__head = Node(value)
        else:
            current = self.__head
            previous = None
            while current and value > current.data:
                previous = current
                current = current.next_node
            if current is None:
                previous.next_node = Node(value)
            elif current is self.__head and previous is None:
                self.__head = Node(value, current)
            else:
                newNode = Node(value, current)
                previous.next_node = newNode

    def __repr__(self):
        """
        returns data as string
        """
        node = self.__head
        text = ''
        while 1:
            text += str(node.data)
            node = node.next_node
            if node.next_node is None:
                break
            else:
                text += '\n'
        return text
