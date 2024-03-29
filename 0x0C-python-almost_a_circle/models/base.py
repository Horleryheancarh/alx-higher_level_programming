#!/usr/bin/python3
"""Module that contains class Base"""
import json
import csv
import os.path


class Base:
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ List to JSON string """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """JSON string to dictionary"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """JSON string to dictionary"""
        if cls.__name__ == "Rectangle":
            new = cls(10, 10)
        else:
            new = cls(10)
        new.update(**dictionary)
        return new

    @classmethod
    def save_to_file(cls, list_objs):
        """Save object to file"""
        filename = "{}.json".format(cls.__name__)
        list_dic = []

        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                list_dic.append(list_objs[i].to_dictionary())

        lst = cls.to_json_string(list_dic)

        with open(filename, 'w') as f:
            f.write(lst)

    @classmethod
    def load_from_file(cls):
        """Returns list of instances"""
        filename = "{}.json".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as f:
            list_str = f.read()

        list_cls = cls.from_json_string(list_str)
        list_ins = []

        for index in range(len(list_cls)):
            list_ins.append(cls.create(**list_cls[index]))

        return list_ins

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Method that saves to CSV"""
        filename = "{}.csv".format(cls.__name__)

        if cls.__name__ == "Rectangle":
            list_dic = [0, 0, 0, 0, 0]
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_dic = [0, 0, 0, 0]
            list_keys = ['id', 'size', 'x', 'y']

        matrix = []

        if not list_objs:
            pass
        else:
            for obj in list_objs:
                for i in range(len(list_keys)):
                    list_dic[i] = obj.to_dictionary()[list_keys[i]]
                matrix.append(list_dic[:])

        with open(filename, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(matrix)

    @classmethod
    def load_from_file_csv(cls):
        """Method that loads CSV"""
        filename = "{}.csv".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as f:
            reader = csv.reader(f)
            csv_list = list(reader)

        if cls.__name__ == "Rectangle":
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_keys = ['id', 'size', 'x', 'y']

        matrix = []

        for elem in csv_list:
            dict_csv = {}
            for i in enumerate(elem):
                dict_csv[list_keys[i[0]]] = int(i[1])
            matrix.append(dict_csv)

        list_ins = []

        for i in range(len(matrix)):
            list_ins.append(cls.create(**matrix[i]))

        return list_ins
