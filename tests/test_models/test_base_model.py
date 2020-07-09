#!/usr/bin/python3
'''base_model UnitTesting'''
import os
import sys
import pep8
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBase_Model(unittest.TestCase):
    '''class TestBase_Model'''

    def setUp(self):
        '''Method that will be ran before every test'''
        self.Base_Model = BaseModel()

    def test_instantiation(self):
        '''method to test class instantiation'''
        self.assertIsInstance(self.Base_Model, BaseModel)

    def test_has_attrs(self):
        '''method to check initial attributes'''
        self.assertTrue(hasattr(self.Base_Model, 'id'))
        self.assertTrue(hasattr(self.Base_Model, 'created_at'))
        self.assertTrue(hasattr(self.Base_Model, 'updated_at'))

    def test_instance_attributes(self):
        '''method to test class attribtues'''
        len_id = len(self.Base_Model.id)
        self.assertEqual(len_id, 36)
        self.assertIsInstance(self.Base_Model.created_at, datetime)
        self.assertIsInstance(self.Base_Model.updated_at, datetime)

    def test_save(self):
        '''method to test BaseModel.save()'''
        updated_at = self.Base_Model.updated_at
        self.Base_Model.test_save = 'testing save'
        self.Base_Model.save()
        self.assertNotEqual(updated_at, self.Base_Model.updated_at)
        self.assertIsNotNone(os.path.exists('file.json'))

    def test_to_dict(self):
        '''method to test BaseModel.to_dict()'''
        # testing key equality
        base_dict = BaseModel().to_dict()
        my_dict = self.Base_Model.to_dict()
        base_keys = base_dict.keys()
        my_keys = my_dict.keys()
        self.assertEqual(base_keys, my_keys)

        # testing __class__ key
        self.assertTrue('__class__' in my_dict)

        # test that __dict__ & .to_dict() are diff
        self.assertIsNot(self.Base_Model.__dict__, self.Base_Model.to_dict())

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0)

    if __name__ == '__main__':
        unittest.main()
