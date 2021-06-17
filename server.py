from flask import Flask
import now
PORT = 8000
app = Flask(__name__)


@app.route("/")
def root():
    MESSAGE = str(now.n())
    return MESSAGE

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
