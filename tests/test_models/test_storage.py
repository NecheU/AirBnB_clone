#!/usr/bin/python3
""" Test the user model """
import datetime
import unittest
from models.engine.file_storage import FileStorage


class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = FileStorage()
        self.user.name = "My First Model"
        self.user.my_number = 89

    def test_correct_instance(self):
        self.assertTrue(isinstance(self.user, FileStorage))

    def test_value_is_set(self):
        pass

    def test_right_value(self):
        pass

    def test_keys_exist_in_dict(self):
        pass

    def test_recreate_class_from_dict(self):
        pass

    def test_exception(self):
        pass
