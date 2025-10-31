# app.py (add to previous Step 3 code)
from flask import Flask, render_template, request, redirect, url_for, abort

app = Flask(__name__)

items = {}
next_id = 1

@app.get("/")
def home():
    return render_template("index.html")

@app.get("/items")
def list_items():
    return render_template("items.html", items=list(items.values()))

@app.post("/items")
def create_item():
    global next_id
    title = request.form.get("title", "").strip()
    if title:
        items[next_id] = {"id": next_id, "title": title}
        next_id += 1
    return redirect(url_for("list_items"))

# ----- NEW: Edit (show form) -----
@app.get("/items/<int:item_id>/edit")
def edit_item(item_id):
    item = items.get(item_id)
    if not item:
        abort(404)
    return render_template("edit_item.html", item=item)

# ----- NEW: Update (process form) -----
@app.post("/items/<int:item_id>/update")
def update_item(item_id):
    item = items.get(item_id)
    if not item:
        abort(404)
    title = request.form.get("title", "").strip()
    if title:
        item["title"] = title
    return redirect(url_for("list_items"))

# ----- NEW: Delete -----
@app.post("/items/<int:item_id>/delete")
def delete_item(item_id):
    if item_id in items:
        del items[item_id]
    return redirect(url_for("list_items"))

if __name__ == "__main__":
    app.run(debug=True)
