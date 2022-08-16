import json

class TestAPICase():
    def test_welcome(self, api):
        res = api.get('/')
        assert res.status == '200 OK'
        assert res.json['message'] == 'Hello from Flask!'

    def test_get_contacts(self, api):
        res = api.get('/api/contacts')
        assert res.status == '200 OK'
        assert len(res.json) == 4

    def test_get_contact(self, api):
        res = api.get('/api/contacts/3')
        assert res.status == '200 OK'
        assert res.json['name'] == 'person3'

    def test_get_contacts_error(self, api):
        res = api.get('/api/contacts/5')
        assert res.status == '400 BAD REQUEST'
        assert "contact with id 5" in res.json['message']

    def test_post_contacts(self, api):
        mock_data = json.dumps({'name': 'Garry'})
        mock_headers = {'Content-Type': 'application/json'}
        res = api.post('/api/contacts', data=mock_data, headers=mock_headers)
        assert res.json['id'] == 5

    def test_delete_contact(self, api):
        res = api.delete('/api/contacts/1')
        assert res.status == '204 NO CONTENT'

    def test_not_found(self, api):
        res = api.get('/hello')
        assert res.status == '404 NOT FOUND'
        assert 'Oops!' in res.json['message']
