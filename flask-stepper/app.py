from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")
def home():
    # send the variable "name" to the template
    return render_template("index.html", name="friend")

if __name__ == "__main__":
    app.run(debug=True)
