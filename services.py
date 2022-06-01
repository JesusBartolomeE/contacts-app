from typing import List
from persistence import DB

dB = DB()

class Contacts:
     
     def add_contact(self,data):
          dB.write_contacts(data)
          
     def read_contacts(self):
          data = dB.read_contacts()
          return data     

     def delete_contact(self,id):
          dB.delete_contact(id)

     def get_id(self,id):
          row = dB.get_contact(id)
          return row

     def update_contact(self,data:List[str]):
          dB.delete_contact(data[0])
          dB.write_contacts(data)
