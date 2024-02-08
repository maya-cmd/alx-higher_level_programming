#!/usr/bin/python3

"""A singly-linked list new class is defined."""


class Node:
    """Represent a singly-linked list node."""

    def __init__(self, data, next_node=None):
        """A new node is intialzed.

        Args:
            data (int): The  new node's data.
            next_node (Node): The new node's next data.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """The node's data is set."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """The next_node of the node is set."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """The singly-linked list is reperented."""

    def __init__(self):
        """A new SinglyLinkedList is represented."""
        self.__head = None

    def sorted_insert(self, value):
        """A new node is inserted to the SinglyLinkedList.

        The node is inserted into the list at the correct
        ordered numerical position.

        Args:
            value (Node): The new Node to insert.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Define the print() singlyLinkedList's representation."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
