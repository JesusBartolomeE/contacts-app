from typing import List
from persistence import DB

dB = DB()

class Contacts:
     
     def add_contact(self,contact):
          response=dB.insert_contact(contact)
          return response

     def read_contacts(self):    
          contacts=list(dB.get_contacts())
          if type(contacts[0]) == dict:
               values=[]
               for contact in contacts:
                    values.append(list(contact.values()))
               return values     
          return contacts

     def get_by_id(self,id):
          row = dB.get_contact_by_id(id)
          return row

     def update_contact(self,id,contact):
          dB.update_contact_id(id,contact)
          return ""

     def delete_contact_by_id(self,id):
          dB.delete_contact(id)
          return ""