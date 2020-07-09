#!/usr/bin/python3
'''base_model UnitTesting'''
import os
import sys
import unittest
from datetime import datetime
from models.place import Place


class TestPlace(unittest.TestCase):
    '''class TestPlace'''

    def setUp(self):
        '''method that will be ran before every test'''
        self.Place = Place()

    def test_instantiation(self):
        '''method to test class instantiation'''
        self.assertIsInstance(self.Place, Place)

    def test_has_attrs(self):
        '''method to test initial attributes exist'''
        self.assertTrue(hasattr(self.Place, 'id'))
        self.assertTrue(hasattr(self.Place, 'city_id'))
        self.assertTrue(hasattr(self.Place, 'user_id'))
        self.assertTrue(hasattr(self.Place, 'description'))
        self.assertTrue(hasattr(self.Place, 'number_rooms'))
        self.assertTrue(hasattr(self.Place, 'number_bathrooms'))
        self.assertTrue(hasattr(self.Place, 'max_guest'))
        self.assertTrue(hasattr(self.Place, 'price_by_night'))
        self.assertTrue(hasattr(self.Place, 'latitude'))
        self.assertTrue(hasattr(self.Place, 'longitude'))
        self.assertTrue(hasattr(self.Place, 'name'))

    def test_instance_attributes(self):
        '''method to test instance attributes'''
        len_id = len(self.Place.id)
        created_time = self.Place.created_at
        updated_time = self.Place.updated_at
        self.assertEqual('', self.Place.city_id)
        self.assertEqual('', self.Place.user_id)
        self.assertEqual(len_id, 36)
        self.assertTrue(created_time != updated_time)
        self.assertIsInstance(self.Place.created_at, datetime)
        self.assertIsInstance(self.Place.updated_at, datetime)

        # test empty values
        self.assertTrue('' == self.Place.name)
        self.assertTrue('' == self.Place.user_id)
        self.assertTrue('' == self.Place.description)

        # assign attrs
        self.Place.city_id = 'test_city_id'
        self.Place.user_id = 'test_user_id'
        self.Place.description = 'test descr'
        self.Place.number_rooms = 3
        self.Place.number_bathrooms = 2
        self.Place.max_guest = 4
        self.Place.price_by_night = 150
        self.Place.latitude = 50.00
        self.Place.longitude = 100.00
        self.Place.name = 'Tulsa'
        self.Place.amenity_ids = ['test_strings', 'ts_str_2']

        # test str attrs
        self.assertNotEqual(self.Place.updated_at, self.Place.created_at)
        self.assertNotEqual(self.Place.name,  '')
        self.assertNotEqual(self.Place.city_id, '')
        self.assertNotEqual(self.Place.user_id, '')
        self.assertNotEqual(self.Place.description, '')

        # test int attrs
        self.assertIsNotNone(self.Place.number_rooms)
        self.assertIsNotNone(self.Place.number_bathrooms)
        self.assertIsNotNone(self.Place.max_guest)
        self.assertIsNotNone(self.Place.price_by_night)
        self.assertIsNotNone(self.Place.latitude)
        self.assertIsNotNone(self.Place.longitude)

    def test_save(self):
        '''method to test Place.save()'''
        updated_at = self.Place.updated_at
        self.Place.test_save = 'testing save'
        self.Place.save()
        self.assertNotEqual(self.Place.updated_at, updated_at)
        self.assertIsNotNone(os.path.exists('file.json'))

    def test_to_dict(self):
        '''method to test Place.to_dict()'''
        # testing key equality
        place_dict = Place().to_dict()
        my_dict = self.Place.to_dict()
        place_keys = place_dict.keys()
        my_keys = my_dict.keys()
        self.assertEqual(place_keys, my_keys)

        # testing attrs in dicts
        self.assertTrue(hasattr(place_dict, '__class__'))

        # test that __dict__ & .to_dict() are diff
        self.assertIsNot(self.Place.__dict__, self.Place.to_dict())

    if __name__ == '__main__':
        unittest.main()
