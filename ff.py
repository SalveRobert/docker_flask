import os
from flask import Flask
app = Flask(__name__)

@app.route("/", methods = ["GET"])
def hello():
    return "goodmorning china now I have binchihlin."

if __name__ == "__main__":
    app.debug = False
    app.run(host = "0.0.0.0", port = os.getenv("SERVICE_PORT"))
