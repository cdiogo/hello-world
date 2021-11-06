from flask import Flask, jsonify

import socket

app = Flask(__name__)

@app.route("/")
def hello():

    return_msg = {"message": " It's Working"}

    return jsonify(return_msg)

@app.route("/hello/<name>")
def hello_name(name):
    return_msg = {"message": f"Hello {name}"}

    return jsonify(return_msg)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
