#!/usr/bin/python3
'''base_model UnitTesting'''
import os
import sys
import unittest
from datetime import datetime
from models.review import Review


class TestReview(unittest.TestCase):
    '''class TestReview'''

    def setUp(self):
        '''method that will be ran before every test'''
        self.Review = Review()

    def test_instantiation(self):
        '''method to test class instantiation'''
        self.assertIsInstance(self.Review, Review)

    def test_has_attrs(self):
        '''method to test class attrs exist'''
        self.assertTrue(hasattr(self.Review, 'place_id'))
        self.assertTrue(hasattr(self.Review, 'user_id'))
        self.assertTrue(hasattr(self.Review, 'text'))

    def test_instance_attributes(self):
        '''method to test instance attributes'''
        len_id = len(self.Review.id)
        created_time = self.Review.created_at
        updated_time = self.Review.updated_at
        self.assertEqual('', self.Review.place_id)
        self.assertEqual(len_id, 36)
        self.assertNotEqual(created_time, updated_time)
        self.assertIsInstance(self.Review.created_at, datetime)
        self.assertIsInstance(self.Review.updated_at, datetime)
        self.assertTrue('' == self.Review.place_id)
        self.assertTrue('' == self.Review.user_id)
        self.assertTrue('' == self.Review.text)
        self.Review.place_id = 'test_id'
        self.Review.user_id = 'user_id'
        self.Review.text = 'placeholder'
        self.assertNotEqual(self.Review.updated_at, self.Review.created_at)
        self.assertTrue(self.Review.place_id != '')
        self.assertTrue(self.Review.user_id != '')
        self.assertTrue(self.Review.text != '')

    def test_save(self):
        '''method to test Review.save()'''
        updated_at = self.Review.updated_at
        self.Review.test_save = 'testing save'
        self.Review.save()
        self.assertNotEqual(self.Review.updated_at, updated_at)
        self.assertIsNotNone(os.path.exists('file.json'))

    def test_to_dict(self):
        '''method to test Review.to_dict()'''
        # testing key equality
        review_dict = Review().to_dict()
        my_dict = self.Review.to_dict()
        review_keys = review_dict.keys()
        my_keys = my_dict.keys()
        self.assertEqual(review_keys, my_keys)

        # testing attrs in dicts
        self.assertTrue(hasattr(review_dict, '__class__'))

        # test that __dict__ & .to_dict() are diff
        self.assertIsNot(self.Review.__dict__, self.Review.to_dict())

    if __name__ == '__main__':
        unittest.main()
