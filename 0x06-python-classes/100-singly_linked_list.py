#!/usr/bin/python3
"""
Module To Define Singly LList in increasing order
"""


class Node:
    """
    Defines a Node of a Singly LList
    """

    def __init__(self, data: int, next_node=None) -> None:
        """
        Initializes Node with data and sets current node's next to next node
        Args:
            data (int): Data to be Assigned to Node
            next_node (Node, optional): next node reference value.
            Defaults to None.

        Raises:
            TypeError: When data in not of type int
            TypeError: When next_node is not an instance of Node
                        and next_node is not Null
        """
        if type(data) is not int:
            raise TypeError("data must be an integer")
        self.__data = data
        if not isinstance(next_node, Node) and next_node is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

    @property
    def data(self) -> int:
        """
        Getter Method for data private attribute
        Returns:
            int: data in given node
        """
        return self.__data

    @data.setter
    def data(self, value: int):
        """
        Sets The Value of data
        Args:
            value (int): New Data Value

        Raises:
            TypeError: Given Value Is Not Of Type Int
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Getter Methodd For next Node
        Returns:
            _type_: Next Node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter Method For next Node
        Args:
            value (Node): Sets New Value To Next Node
        Raises:
            TypeError: If Given Object Is Not an Instance Of class Node
            and not NULL
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Defines a Singly Linked List
    """

    def __init__(self) -> None:
        """
        Initializes Head Node
        """
        self.__head = None

    def __str__(self) -> str:
        """
        Prints data of a Singly LList
        Returns:
            str: ""
        """
        temp = self.__head
        while temp is not None:
            print(temp.data, end="\n" if temp.next_node is not None else "")
            temp = temp.next_node
        return ""

    def sorted_insert(self, value):
        """
        Insert Singly LL at the beginning which involves updating Head Node
        Args:
            value (int): Data To Be Added To New  Node
        """
        new_node = Node(value, self.__head)
        temp = new_node
        while temp.next_node is not None:
            if temp.data > temp.next_node.data:
                max = temp.data
                temp.data = temp.next_node.data
                temp.next_node.data = max
            temp = temp.next_node
        self.__head = new_node
