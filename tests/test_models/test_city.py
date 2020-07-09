#!/usr/bin/python3
'''base_model UnitTesting'''
import os
import sys
import unittest
from datetime import datetime
from models.city import City


class TestCity(unittest.TestCase):
    '''class TestCity'''

    def setUp(self):
        '''method that will be ran before every test'''
        self.City = City()

    def test_instantiation(self):
        '''method to test class instantiation'''
        self.assertIsInstance(self.City, City)

    def test_has_attrs(self):
        '''method to test initial attrs exist'''
        self.assertTrue(hasattr(self.City, 'state_id'))
        self.assertTrue(hasattr(self.City, 'name'))

    def test_instance_attributes(self):
        '''method to test instance attributes'''
        len_id = len(self.City.id)
        created_time = self.City.created_at
        updated_time = self.City.updated_at
        self.assertEqual('', self.City.state_id)
        self.assertEqual(len_id, 36)
        self.assertTrue(created_time != updated_time)
        self.assertIsInstance(self.City.created_at, datetime)
        self.assertIsInstance(self.City.updated_at, datetime)
        self.assertTrue('' == self.City.name)
        self.City.name = 'Tulsa'
        self.City.state_id = 'testID'
        self.assertNotEqual(self.City.updated_at, self.City.created_at)
        self.assertNotEqual(self.City.name,  '')
        self.assertNotEqual(self.City.state_id, '')

    def test_save(self):
        '''method to test City.save()'''
        updated_at = self.City.updated_at
        self.City.test_save = 'testing save'
        self.City.save()
        self.assertNotEqual(self.City.updated_at, updated_at)
        self.assertIsNotNone(os.path.exists('file.json'))

    def test_to_dict(self):
        '''method to test City.to_dict()'''
        # testing key equality
        city_dict = City().to_dict()
        my_dict = self.City.to_dict()
        city_keys = city_dict.keys()
        my_keys = my_dict.keys()
        self.assertEqual(city_keys, my_keys)

        # testing attrs in dicts
        self.assertTrue(hasattr(city_dict, '__class__'))

        # test that __dict__ & .to_dict() are diff
        self.assertIsNot(self.City.__dict__, self.City.to_dict())

    if __name__ == '__main__':
        unittest.main()
