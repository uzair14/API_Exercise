from werkzeug.exceptions import BadRequest

from app import app,db
db.create_all()

from app import Contacts

Contacts.__table__.drop()

db.session.add(Contacts(id=1, name='Bob', number='07632421834', workplace='Electric and co.'))
db.session.commit()



# contacts = [
#     {{'id':1, 'name': 'Bob', 'number':'07632421834', 'email': 'bob@gmail.com', 'workplace': 'Electric and co.'}},
#     {'id':2, 'name': 'Tim', 'number':'07834567912', 'email': 'tim@gmail.com', 'workplace': 'Plumber and co.'},
#     {'id':3, 'name': 'Bill', 'number':'07541945678', 'email': 'bill@gmail.com', 'workplace': 'Fish and Chips co'},
#     {'id':4, 'name': 'Jimmy', 'number':'07894567431', 'email': 'jimmy@gmail.com', 'workplace': 'Hospital and co'}
# ]





def index(req):
    # return [c for c in contacts], 200
    return Contacts.query.all(), 200

# def create(req):
#     new_contact = req.get_json()
#     new_contact['id'] = sorted([c['id'] for c in contacts])[-1] +1
#     contacts.append(new_contact)
#     return new_contact, 201

# def show(req, uid):
#     return find_by_uid(uid), 200

# def destroy(req, uid):
#     contact = find_by_uid(uid)
#     contacts.remove(contact)
#     return contact, 204

# def update(req, uid):
#     contact = find_by_uid(uid)
#     data = req.get_json()
#     print(data)
#     for key, val in data.items():
#         contact[key] = val
#     return contact, 200

# def find_by_uid(uid):
#     try: 
#         return next (c for c in contacts if c['id'] == uid)
#     except:
#         raise BadRequest(f"We dont have a contact with id {uid}!")
