from flask import Flask, jsonify

# Initialize the Flask app
app = Flask(__name__)

# Define a REST GET endpoint
@app.route('/api/hello', methods=['GET'])
def hello_world():
    return jsonify({"message": "Hello, World!"})

# Define a REST GET endpoint
@app.route('/api/h2', methods=['GET'])
def hello_world_v2():
    return jsonify({"message": "Hello, World2!"})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
