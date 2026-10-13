from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "ACEest Fitness & Gym"

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

@app.route("/members")
def members():
    return jsonify({
        "members": 150
    })

@app.route("/trainers")
def trainers():
    return jsonify({
        "trainers": 10
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
