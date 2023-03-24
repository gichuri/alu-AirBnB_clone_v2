#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import column, String, Integer, DateTime
import models

Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models"""
    id = column(String(60), nullable=False, primary_key=True)
    created_at = column(DateTime, nullable=False, default=(datetime.utcnow()))
    updated_at = column(datetime, nullable=False, default=datetime.utcnow())
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

        if kwargs:
            if "id" not in kwargs:
                kwargs["id"] = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                kwargs['created_at'] = datetime.now().isoformat()
            if 'updated_at' not in kwargs:
                kwargs['updated_at'] = datetime.now().isoformat()

            for key, value in kwargs.items():
                if key == 'created_at':
                    kwargs[key] = datetime.strptime(value,'%Y-%m-%dT%H:%M:%S.%f')
                if key == 'updated_at' :
                    kwargs[key] = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if hasattr(self, key) and key != "__class__":
                    setattr(self, key, value)
            if '__class__' in kwargs:
                del kwargs['__class__']

            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        """Convert instance into dict format"""
        my_dict = dict(self.__dict__)
        for key in self.__dict__.keys():
            if key == "_sa_instance_state":
                del (my_dict[key])

        # my_dict["__class__"] = str(type(self).__name__)
        my_dict.update({'__class__': self.__class__.__name__})
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict["created_at"] = self.created_at.isoformat()
        # delete _sa_instance_state
        if hasattr(self, '_sa_instance_state'):
            del dictionary['_sa_instance_state']

        return dictionary
    def delete(self):
        """ delete current instance from storage by calling strorage.delete"""
        models.storage.delete(self)
