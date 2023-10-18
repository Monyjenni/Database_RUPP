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
  new_company = {'name': 'PBC BookStore', 'items': []}
  companies.append(new_company)
  return {'msg': 'successfully'}

  

@app.get('/test')
def test():
  return {'msg': 'Hello World'}

if __name__ == '__main__':
  app.run(debug=True)
  
