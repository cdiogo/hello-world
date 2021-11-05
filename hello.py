from flask import Flask, jsonify

import socket

app = Flask(__name__)

@app.route("/")
def hello():

    return_msg = {"message": "Hello!!!!",
                  "hostname": str(socket.gethostname())
                  }

    return jsonify(return_msg)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
