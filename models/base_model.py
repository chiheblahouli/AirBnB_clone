#!/usr/bin/python3
""" BaseModel module """

from datetime import datetime
from models import storage
import uuid


class BaseModel():
    '''class BaseModel defines common attributes/methods for other classes'''

    __check = {}

    def __init__(self, *args, **kwargs):
        if (kwargs is not None and kwargs != {}):
            for keys in kwargs.keys():
                if keys == 'created_at' or keys == 'updated_at':
                    dt = kwargs[keys]
                    form = '%Y-%m-%dT%H:%M:%S.%f'
                    if type(kwargs[keys]) is str:
                        dt = datetime.strptime(kwargs[keys], form)
                    setattr(self, keys, dt)
                elif keys != "__class__":
                    setattr(self, keys, kwargs[keys])
            storage.new(self)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        '''updates public instance attr updated_at with current datetime'''
        self.updated_at = datetime.utcnow()
        storage.save()

    def to_dict(self):
        '''returns a dict containing all keys/values of __dict__ of instance'''
        self_dict = dict(self.__dict__)

        for item in self.__dict__:
            if item == 'created_at' or item == 'updated_at':
                dt = self.__dict__[item].strftime('%Y-%m-%dT%H:%M:%S.%f')
                self_dict.update({item: dt})
            else:
                self_dict.update({item: self.__dict__.get(item)})
        self_dict.update({'__class__': self.__class__.__name__})
        return self_dict

    def __str__(self):
        '''should print: [<class name>] (<self.id>) <self.__dict__>'''
        return "[{}] ({}) {}\
                ".format(self.__class__.__name__, self.id, self.__dict__)

    def update_file(self):
        '''Updates the storage if the dictionary changes'''
        storage.new(self)
        self.__check = self.__dict__
