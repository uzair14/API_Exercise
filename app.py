from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug import exceptions
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class Contacts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    number = db.Column(db.String(120), unique=False, nullable=False)
    # email = db.Column(db.String(120), unique=True, nullable=False)
    workplace = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name



from controllers import contacts


@app.route('/')
def welcome():
    return jsonify({'message': 'Hello from Flask!'}), 200

@app.route('/api/contacts', methods = ['GET', 'POST'])
def contact():
    fns = {
        'GET': contacts.index
        # 'POST': contacts.create
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code

# @app.route('/api/contacts/<int:contact_id>', methods=['GET', 'DELETE','PUT'])
# def contact_handler(contact_id):
#     fns = {
#         'GET': contacts.show,
#         'DELETE': contacts.destroy,
#         'PUT': contacts.update
#     }
#     resp, code = fns[request.method](request, contact_id)
#     return jsonify(resp), code

@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return {'message': f'Oops! {err}'}, 404

@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return {'message': f'Oops! {err}'}, 400

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return {'message': f"It's not you, it's us {err}"}, 500


if __name__ == "__main__":
    app.run(debug=True)

