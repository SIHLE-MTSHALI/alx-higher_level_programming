#!/usr/bin/python3
"""
Module 100-singly_linked_list
Defines classes Node and SinglyLinkedList.
"""


class Node:
    """
    Represents a node in a singly linked list.

    Attributes:
    data (int): Data stored in the node.
    next_node (Node): The next node in the linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initialize a Node.

        Args:
        data (int): Data of the Node.
        next_node (Node): The next node in the list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieves the data of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the data of the node.

        Args:
        value (int): The data to set in the node.

        Raises:
        TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieves the next node of the current node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node of the current node.

        Args:
        value (Node): The node to set as the next node.

        Raises:
        TypeError: If value is not a Node instance or None.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Represents a singly linked list.

    Attributes:
    head (Node): The head of the linked list.
    """

    def __init__(self):
        """
        Initialize the SinglyLinkedList.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the list at the correct position.

        Args:
        value (int): The data of the new Node.
        """
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
        while current.next_node is not None and \
                current.next_node.data < value:
            current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Defines the print() representation of the SinglyLinkedList.
        """
        values = []
        current = self.__head
        while current:
            values.append(str(current.data))
            current = current.next_node
        return "\n".join(values)
