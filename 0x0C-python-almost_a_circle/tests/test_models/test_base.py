#!/usr/bin/python3
"""Module for testing Base Class"""
import unittest
from unittest import TestCase
from unittest.mock import patch
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
from io import StringIO


class TestBaseMethods(unittest.TestCase):
    """Suite to test Base class"""

    def setUp(self):
        """Run before every test"""
        Base._Base__nb_objects = 0

    def test_id(self):
        """Test assigned id"""
        new = Base(1)
        self.assertEqual(new.id, 1)

    def test_auto_id(self):
        """Test assigned id"""
        new = Base()
        self.assertEqual(new.id, 1)

    def test_id_nb_objects(self):
        """Test assigned id"""
        new = Base()
        new1 = Base()
        new2 = Base()
        self.assertEqual(new.id, 1)
        self.assertEqual(new1.id, 2)
        self.assertEqual(new2.id, 3)

    def test_id_mix(self):
        """Test nb object attributes and assigned id"""
        new = Base()
        new1 = Base(555)
        new2 = Base(234)
        self.assertEqual(new.id, 1)
        self.assertEqual(new1.id, 555)
        self.assertEqual(new2.id, 234)

    def test_string_id(self):
        """Test string id"""
        new = Base('1')
        self.assertEqual(new.id, '1')

    def test_more_args(self):
        """Test passing more args to init"""
        with self.assertRaises(TypeError):
            new = Base(1, 1)

    def test_private_attrs_access(self):
        """Test access to private attrs"""
        new = Base()
        with self.assertRaises(AttributeError):
            new.__nb_objects

    def test_save_to_file(self):
        """Test JSON file"""
        Square.save_to_file(None)
        res = '[]\n'
        with open('Square.json', 'r') as f:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(f.read())
                self.assertEqual(str_out.getvalue(), res)

        try:
            os.remove('Square.json')
        except:
            pass

        Square.save_to_file([])
        with open('Square.json', 'r') as f:
            self.assertEqual(f.read(), '[]')

    def test_save_to_file1(self):
        """Test JSON file"""
        Rectangle.save_to_file(None)
        res = '[]\n'
        with open('Rectangle.json', 'r') as f:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(f.read())
                self.assertEqual(str_out.getvalue(), res)

        try:
            os.remove('Rectangle.json')
        except:
            pass

        Rectangle.save_to_file([])
        with open('Rectangle.json', 'r') as f:
            self.assertEqual(f.read(), '[]')
