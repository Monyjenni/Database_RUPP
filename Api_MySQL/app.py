from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request
from sqlalchemy import exc

# Create an instance of the Flask application
app = Flask(__name__)

# Configure the Flask app for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:012345678@localhost:3306/apdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create an instance of the SQLAlchemy extension
db = SQLAlchemy(app)

# Import the model after initializing the db object
from models import terms

# Define routes
@app.route('/terms')
def get_terms():
    # Use db.session.query and .all() to get all results
    results = db.session.query(terms).all()

    # Create a list of dictionaries from the query results
    terms_list = [
        {
            "id": term.terms_id,
            "description": term.terms_description,
            "due_days": term.terms_due_days
        }
        for term in results
    ]
    return terms_list

@app.route('/terms1')
def get_terms1():
    # Use db.session.query and .all() to get all results
    results = db.session.query(terms).all()

    # Use _asdict() to convert each result to a dictionary
    terms_list = [term._asdict() for term in results]

    return terms_list

from models import terms,invoices

@app.get('/terms/<int:id>')
def get_term(id):
    term = db.session.query(terms)\
        .filter(terms.terms_id == id)\
        .first()
    if term:
        return term._asdict()
    else:
        return {'message': 'Term not found'}, 404

@app.get('/invoices/term/<int:term_id>')
def get_invoices_term(term_id):
    invoices_data = db.session.query(invoices, terms)\
        .join(terms, terms.terms_id == invoices.terms_id)\
        .filter(invoices.terms_id == term_id)\
        .all()
    
    if invoices_data:
        result = [{'invoice_number': inv.invoice_number, 'terms_description': term.terms_description}
                for inv, term in invoices_data]
        return result
    else:
        return {'message': 'No invoices found for the given term'}, 404

@app.post('/terms')
def post_terms():
    try:
        request_data = request.get_json()
        new_term = terms(terms_description=request_data["terms_description"],
                        terms_due_days=request_data["terms_due_days"])
        db.session.add(new_term)
        db.session.commit()
        return {'message': 'Term added successfully'}, 201
    except Exception as e:
        print(e)
        return {'message': 'Something went wrong!'}, 500

@app.put('/terms/<string:des>')
def put_terms(des):
    request_data = request.get_json()
    term = db.session.query(terms).filter(terms.terms_description == des).first()
    if term:
        term.terms_description = request_data["terms_description"]
        term.terms_due_days = request_data["terms_due_days"]
        try:
            db.session.commit()
            return {'message': 'Term updated successfully'}
        except exc.SQLAlchemyError as e:
            return {'message': str(e.__cause__)}, 500
    else:
        return {'message': 'Term not found'}, 404

@app.delete('/terms/<int:id>')
def delete_terms(id):
    term = db.session.query(terms).filter(terms.terms_id == id).first()
    if term:
        db.session.delete(term)
        try:
            db.session.commit()
            return {'message': 'Term deleted successfully'}
        except exc.SQLAlchemyError as e:
            return {'message': str(e.__cause__)}, 500
    else:
        return {'message': 'Term not found'}, 404

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='127.0.0.1', port=5000)
