#!/usr/bin/python3
"""
Module For The Base Class
"""
import json


class Base:
    """
    The Base Class For All Upcoming Classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor To Assign id To Each Newly Created Object
        Args:
            id (int, optional): A Specific id For Each Instance.
                                Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts Python List of Dictionaries
        To Equivalent JSON Object
        Args:
            list_dictionaries (list): List Containing Dictionaries

        Returns:
            JSON Object: Equivalent JSON Representation
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves Equivalent JSON Representation
        Of Python list to file where the name
        of file is specified according to the
        class executed it
        Args:
            list_objs (list): Python List to be Converted
        """
        list_dictionaries = []
        with open(f"{cls.__name__}.json", mode='w', encoding='utf-8') as file:
            if list_objs is None len(list_objs) == 0 or :
                file.write(f'{list_dictionaries}')
            else:
                for obj in list_objs:
                    list_dictionaries.append(obj.to_dictionary())
                file.write(Base.to_json_string(list_dictionaries))
