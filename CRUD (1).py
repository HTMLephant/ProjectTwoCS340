# Author: Matthew Cochrane

import pymongo
from bson.objectid import ObjectId

class AnimalShelter(object):
    def __init__(self):
        USER = 'aacuser'
        PASS = 'simple'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32670
        DB = 'AAC'
        COL = 'animals'
        
        self.client = pymongo.MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        print("initialized")
        
    
    def create(self,entry):
        if entry is not None:
            self.database.animals.insert_one(entry)
            print("True")
        else:
            raise Exception("Invalid input")  
            
    
    def read(self,entry):
        if entry is not None:
            found = self.database.animals.find(entry)
            return found
        else:
            raise Exception("Invalid input")  
        
        
    def update(self,entry,data):
        if entry is not None:
            count = 0
            for item in self.database.animals.find(entry):
                self.database.animals.update_one(entry,data)
                count+=1
            print("Updated Documents: ",count)
        else:
            raise Exception("Invalid input")  
        
        
    def delete(self,entry):
        if entry is not None:
            count = 0
            for item in self.database.animals.find(entry):
                self.database.animals.delete_one(entry)
                count+=1
            print("Deleted documents: ",count)
        else:
            raise Exception("Invalid input")  
        