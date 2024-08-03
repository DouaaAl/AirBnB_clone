#!/usr/bin/python3
"""
Base Model
"""
import uuid
import models
from datetime import datetime

class BaseModel():
    def __init__(self, *args, **kwargs):
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, time_format))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
        models.storage.new(self)

    def save(self):
        """
        updating timeof updated_at
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()
        return self.updated_at
   
    def to_dict(self):
        """
        to dict
        """
        copy_dict = self.__dict__.copy()
        copy_dict["__class__"] = self.__class__.__name__
        copy_dict["created_at"] = self.created_at.isoformat()
        copy_dict["updated_at"] = self.updated_at.isoformat()

        return copy_dict

    def __str__(self):
        """
        string function
        """
        class_name = self.__class__.__name__

        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

if __name__ == "__main__":
    my_model = BaseModel()
    print(my_model.id)
    print(str(my_model))
    print(my_model.to_dict())
    
        
               
