from services import Contacts

contacts = Contacts()

def test_insert_contact():
    response = contacts.add_contact({"fullname":"Davidcito"})
    assert response == True

def test_get_contacts():
    response = contacts.read_contacts()
    assert type(response) == list