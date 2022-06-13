from bson import ObjectId
from flask import Flask
from flask_pymongo import pymongo
import os 

class DB:

    def __init__(self):

        self._CONNECTION_STRING = os.getenv("DB_CONECTION") 
        self._client = pymongo.MongoClient(self._CONNECTION_STRING)
        self._db = self._client.get_database('first-test')

    def _get_collection(self,name_collecction):
        return pymongo.collection.Collection( self._db, name_collecction)

    def insert_contact(self,contact):
        collection = self._get_collection('Contacts')
        collection.insert_one(contact)
        print(contact)

    def get_contacts(self):
        data = self._get_collection('Contacts').find()
        return data

    def get_contact_by_id(self,id):
        row = self._get_collection('Contacts').find_one({'_id':ObjectId(id)})    
        return row

    def update_contact_id(self,id,contact):
        print("Estoy aqui")
        print(id)
        print(contact)
        self._get_collection('Contacts').update_one({'_id':ObjectId(id)},{'$set':{"fullname":contact["fullname"],"phone":contact["phone"],"email":contact["email"]}})
        return ""

    def delete_contact(self,id):
        self._get_collection('Contacts').delete_one({'_id':ObjectId(id)})
        return ""