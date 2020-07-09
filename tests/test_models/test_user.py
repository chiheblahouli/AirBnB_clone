#!/usr/bin/python3
'''base_model UnitTesting'''
import os
import sys
import unittest
from datetime import datetime
from models.user import User


class TestBase_Model(unittest.TestCase):
    '''class TestBase_Model'''

    def setUp(self):
        '''Method that will be ran before every test'''
        self.User = User()

    def test_instantiation(self):
        '''method to test class instantiation'''
        self.assertIsInstance(self.User, User)

    def test_attrs_type(self):
        '''method to test email attribute of User class'''
        # testing types of attrs
        self.assertTrue(type(self.User.email) == str)
        self.assertTrue(type(self.User.password) == str)
        self.assertTrue(type(self.User.first_name) == str)
        self.assertTrue(type(self.User.last_name) == str)

    def test_attrs_initial(self):
        # testing initial condition of attrs
        self.assertEqual('', self.User.email)
        self.assertEqual('', self.User.password)
        self.assertEqual('', self.User.first_name)
        self.assertEqual('', self.User.last_name)

    def test_attrs_updating(self):
        # testing updating of attrs
        self.User.email = 'email'
        self.User.password = 'password'
        self.User.first_name = 'first'
        self.User.last_name = 'last'
        self.assertNotEqual('', self.User.email)
        self.assertNotEqual('', self.User.password)
        self.assertNotEqual('', self.User.first_name)
        self.assertNotEqual('', self.User.last_name)

    if __name__ == '__main__':
        unittest.main()
