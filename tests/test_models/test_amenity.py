#!/usr/bin/python3
'''base_model UnitTesting'''
import os
import sys
import unittest
from datetime import datetime
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    '''class TestAmenity'''

    def setUp(self):
        '''method that will be ran before every test'''
        self.Amenity = Amenity()

    def test_instantiation(self):
        '''method to test class instantiation'''
        self.assertIsInstance(self.Amenity, Amenity)

    def test_has_attrs(self):
        '''method to test attrs in Amenity exist'''
        self.assertTrue(self.Amenity, 'name')

    def test_instance_attributes(self):
        '''method to test instance attributes'''
        len_id = len(self.Amenity.id)
        created_time = self.Amenity.created_at
        updated_time = self.Amenity.updated_at
        self.assertEqual(len_id, 36)
        self.assertTrue(created_time != updated_time)
        self.assertIsInstance(self.Amenity.created_at, datetime)
        self.assertIsInstance(self.Amenity.updated_at, datetime)
        self.assertTrue('' == self.Amenity.name)
        self.Amenity.name = 'Washer/Dryer'
        self.assertNotEqual(self.Amenity.updated_at, self.Amenity.created_at)
        self.assertNotEqual(self.Amenity.name,  '')

    def test_save(self):
        '''method to test Amenity.save()'''
        updated_at = self.Amenity.updated_at
        self.Amenity.test_save = 'testing save'
        self.Amenity.save()
        self.assertNotEqual(self.Amenity.updated_at, updated_at)
        self.assertIsNotNone(os.path.exists('file.json'))

    def test_to_dict(self):
        '''method to test Amenity.to_dict()'''
        # testing key equality
        amenity_dict = Amenity().to_dict()
        my_dict = self.Amenity.to_dict()
        amenity_keys = amenity_dict.keys()
        my_keys = my_dict.keys()
        self.assertEqual(amenity_keys, my_keys)

        # testing attrs in dicts
        self.assertTrue(hasattr(amenity_dict, '__class__'))

        # test that __dict__ & .to_dict() are diff
        self.assertIsNot(self.Amenity.__dict__, self.Amenity.to_dict())

    if __name__ == '__main__':
        unittest.main()
