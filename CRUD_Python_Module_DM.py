# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, USER, PASS): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        #  
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
    # method of creating records to implement the C in CRUD. 
    def create(self, data):
        try:
            if data is not None: # if data insert is not empty
                self.database.animals.insert_one(data)  # data should be dictionary   
                return True # successful insert
            else:  
                return False # unsuccessful insert
        except Exception as e:
            print(f"Error creating record: {e}") # relevant error message
            return 0

    # method of reading records to implement the R in CRUD.
    def read(self, search, projection = None):
        try:
            if projection:
                cursor = self.database.animals.find(search, projection)
            else:
                cursor = self.database.animals.find(search) # find query results in database
            result = list(cursor)
            for animal in result:
                print(animal, "\n") # list applicable results
        except Exception as e:
            print(f"Error finding record: {e}") # relevant error message
            result = []
        return result   
            
    # method of updating records to implement the U in CRUD 
    def update(self, query, new_data):
        try:
            result = self.database.animals.update_many(query, {'$set' : new_data}) # update specifed query value using the set operator in Mongodb
            return f"Records updated: {result.modified_count}"
        except Exception as e:
            print(f"Error updating record: {e}") # relevant error message
            return 0
        
    # method of deleting records to implement the D in CRUD 
    def delete(self, query):
        try:
            result = self.database.animals.delete_many(query) # remove all results that match the specified query
            return f"Records removed: {result.deleted_count}"
        except Exception as e:
            print(f"Error deleting record: {e}\n") # relevant error message
            return 0
                