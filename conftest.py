import pytest
import app
from controllers import contacts

@pytest.fixture
def api(monkeypatch):
    test_contacts = [ {'id':1, 'name': 'person1', 'number':'07632421834', 'email': 'bob@gmail.com', 'workplace': 'Electric and co.'},
    {'id':2, 'name': 'person2', 'number':'07834567912', 'email': 'tim@gmail.com', 'workplace': 'Plumber and co.'},
    {'id':3, 'name': 'person3', 'number':'07541945678', 'email': 'bill@gmail.com', 'workplace': 'Fish and Chips co'},
    {'id':4, 'name': 'person4', 'number':'07894567431', 'email': 'jimmy@gmail.com', 'workplace': 'Hospital and co'}]
    monkeypatch.setattr(contacts, "contacts", test_contacts)
    api = app.app.test_client()
    return api
