# app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# --- In-memory data store (reset on server restart) ---
items = {}        # e.g., {1: {"id": 1, "title": "Buy milk"}}
next_id = 1

@app.get("/")
def home():
    return render_template("index.html")

# List items + show create form
@app.get("/items")
def list_items():
    return render_template("items.html", items=list(items.values()))

# Create item
@app.post("/items")
def create_item():
    global next_id
    title = request.form.get("title", "").strip()
    if title:
        items[next_id] = {"id": next_id, "title": title}
        next_id += 1
    return redirect(url_for("list_items"))

if __name__ == "__main__":
    app.run(debug=True)
