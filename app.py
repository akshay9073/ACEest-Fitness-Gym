from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "ACEest Fitness & Gym",
        "version": "1.0"
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