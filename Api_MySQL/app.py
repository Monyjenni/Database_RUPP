from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create an instance of the Flask application
app = Flask(__name__)

# Configure the Flask app for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456789@localhost:3306/apdb'
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

    # Return the list as JSON
    return jsonify(terms_list)

@app.route('/terms1')
def get_terms1():
    # Use db.session.query and .all() to get all results
    results = db.session.query(terms).all()

    # Use _asdict() to convert each result to a dictionary
    terms_list = [term._asdict() for term in results]

    # Return the list as JSON
    return jsonify(terms_list)

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='127.0.0.1', port=5000)
