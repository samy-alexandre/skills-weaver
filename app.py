from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>SkillWeaver Online</h1>
    <p>Le serveur fonctionne.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
