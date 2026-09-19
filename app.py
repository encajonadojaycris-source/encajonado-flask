from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def home():
    return """
    <h1>Welcome to JayCris's Student API!</h1>
    <p>My Flask API is successfully deployed on Render.</p>

    <h2>Available Endpoints:</h2>
    <ul>
        <li><a href="/student">/student</a> - Student information</li>
        <li><a href="/jaycris">/jaycris</a> - Hello message</li>
        <li><a href="/subjects">/subjects</a> - My subjects</li>
        <li><a href="/greet">/greet</a> - Personalized greeting</li>
    </ul>
    """


@app.route('/student')
def get_student():
    return jsonify({
        "student_id": "24-00196",
        "name": "Jay Cris Encajonado",
        "Course": "BSIT",
        "year": 3,
        "section": "B"
    })


@app.route('/jaycris')
def say_hello():
    name = request.args.get('name', 'Student')

    return jsonify({
        "message": "Hello, JayCris!"
    })


# NEW ENDPOINT 1
@app.route('/subjects')
def get_subjects():
    return jsonify({
        "student": "Jay Cris Encajonado",
        "subjects": [
            "\nWeb Programming",
            "\nDatabase Management",
            "\nInformation Management",
            "\nSystems Integration"
        ],
        "semester": "First Semester"
    })


# NEW ENDPOINT 2
@app.route('/greet')
def get_greet():
    return jsonify({
        "message": "Welcome, JayCris!",
        "purpose": "Personalized student greeting",
        "status": "API is working"
    })


if __name__ == '__main__':
    app.run(debug=True)

