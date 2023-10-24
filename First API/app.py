from flask import Flask

app = Flask(__name__)

companies = [
    {
        "name": "ABSARA",
        "items": [
            {
                "name": "pen",
                "price": 15.99
            },
            {
                "name": "book",
                "price": 11
            }
        ]
    }
]

@app.get('/company')
def Company():
  return {"companies": companies}
  

@app.post('/addCompany')
def addCompany():
    new_company_data = request.get_json()

    if not new_company_data:
        return "Invalid JSON data", 400

    companies.append(new_company_data)
    return "Successfully added a new company", 200

  

@app.get('/test')
def test():
  return {'msg': 'Hello World'}

if __name__ == '__main__':
  app.run(debug=True)
  
