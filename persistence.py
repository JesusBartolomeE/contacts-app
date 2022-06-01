from typing import List
import csv

class DB:
    
    def __init__ (self):
        
        self.__file = "dB.csv"

    def write_contacts(self,data):
        with open(self.__file, "a+") as contacts:  
            create_contact= csv.writer(contacts, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            create_contact.writerow(data) 

    def read_contacts(self):
        with open(self.__file, "r") as contacts:  
            read_contacts= csv.reader(contacts, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            data = list (read_contacts)
        return data   

    def delete_contact(self,id):
        data = self.read_contacts()
        with open(self.__file, "w") as contacts:
            writer = csv.writer(contacts)
            for row in data:
                if row[0] != id:
                        writer.writerow(row)

    def get_contact(self,id):
        data = self.read_contacts()
        for row in data:
            if row[0] == id:
                return row  