from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Particle Counter API GET</p>"

if __name__ == "__main__":
    app.run()