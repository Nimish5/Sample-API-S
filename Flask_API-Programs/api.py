from flask import Flask

app = Flask(__name__)

@app.route("/")
def python():
    return "Will complete Flask by end of March!"

app.run(port=5000)
# if __name__ == "__main__":
#     app.run(debug=True)