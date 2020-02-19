#!/usr/bin/python3
"""
Test Amenity
"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import unittest
import pep8


class Testamenity(unittest.TestCase):

    def test_pep8_conformance_amenity(self):
        """
        Test that we conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "Found style errors")

    def test_class(self):
        amenity1 = Amenity()
        self.assertEqual(amenity1.__class__.__name__, "Amenity")

    def test_father(self):
        amenity1 = Amenity()
        self.assertTrue(issubclass(amenity1.__class__, BaseModel))

    def test_amenity(self):
        """
        Test attributes of Class Amenity
        """
        my_amenity = Amenity()
        my_amenity.name = "Wi-Fi"
        self.assertEqual(my_amenity.name, 'Wi-Fi')
