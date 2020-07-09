#!/usr/bin/python3
'''base_model UnitTesting'''
import os
import sys
import unittest
from datetime import datetime
from models.state import State


class TestState(unittest.TestCase):
    '''class TestState'''

    def setUp(self):
        '''method that will be ran before every test'''
        self.State = State()

    def test_instantiation(self):
        '''method to test class instantiation'''
        self.assertIsInstance(self.State, State)

    def test_instance_attributes(self):
        '''method to test instance attributes'''
        len_id = len(self.State.id)
        created_time = self.State.created_at
        updated_time = self.State.updated_at
        self.assertEqual(len_id, 36)
        self.assertTrue(created_time != updated_time)
        self.assertIsInstance(self.State.created_at, datetime)
        self.assertIsInstance(self.State.updated_at, datetime)
        self.assertTrue('' == self.State.name)
        self.State.name = 'Oklahoma'
        self.assertNotEqual(self.State.updated_at, self.State.created_at)
        self.assertNotEqual(self.State.name,  '')

    def test_save(self):
        '''method to test State.save()'''
        updated_at = self.State.updated_at
        self.State.test_save = 'testing save'
        self.State.save()
        self.assertNotEqual(self.State.updated_at, updated_at)
        self.assertIsNotNone(os.path.exists('file.json'))

    def test_to_dict(self):
        '''method to test State.to_dict()'''
        # testing key equality
        state_dict = State().to_dict()
        my_dict = self.State.to_dict()
        state_keys = state_dict.keys()
        my_keys = my_dict.keys()
        self.assertEqual(state_keys, my_keys)

        # testing attrs in dicts
        self.assertTrue(hasattr(state_dict, '__class__'))

        # test that __dict__ & .to_dict() are diff
        self.assertIsNot(self.State.__dict__, self.State.to_dict())

    if __name__ == '__main__':
        unittest.main()
