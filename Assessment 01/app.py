from flask import Flask, request

app = Flask(__name__)

Classes = [
    {
        "Class": "M4",
        "Student": [
            {
                "name": "Sok",
                "gender": "Female"
            },
            {
                "name": "Sao",
                "gender": "Male"
            }
        ]
    }
]

#endpoint to get all classes
@app.get('/getAllClasses')
def getClasses():
    return Classes

#endpoint to add new class one by one
@app.post('/addClass')
def addClass():
    new_class = request.get_json()
    Classes.append(new_class)
    # status 200 means ok or succeed
    return "Successfully added new class! ", 200


if __name__ == '__main__':
    app.run(debug=True)

