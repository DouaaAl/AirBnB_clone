import json
import os
from models.base_model import BaseModel

class FileStorage:
    """
    file storage class
    """

    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """
        create new self
        """
        obj_class_name = obj.__class__.__name__

        key = "{}.{}".format(obj_class_name, obj.id)

        FileStorage.__objects[key] = obj

    def all(self):
        """
        return the objects attribute
        """
        return FileStorage.__objects

    def save(self):
        """
        get dictionnaries and put them in a json file
        """

        all_objects = __objects
        object_dict = {}

        for key in all_objects.keys():
            object_dict[key] = all_objects[key].to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(object_dict, file)

    def reload(self):
        """
        reload all json to dict
        """

        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    obj_dict = json.load(file)

                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split(".")

                        cls = eval(class_name)

                        instance = cls()

                        FileStorage.__objects[key] = instance
                except:
                    pass

if __name__ == "__main__":
    instance = FileStorage()

