import sqlite3
from flask import Flask, render_template, request, redirect, session
from flask_session import Session

app = Flask(__name__)

# Standard SQLite connection helper
def get_db_connection():
    # row_factory allows us to access columns by name (like a dictionary)
    conn = sqlite3.connect("store.db")
    conn.row_factory = sqlite3.Row
    return conn

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    db = get_db_connection()
    books = db.execute("SELECT * FROM books").fetchall()
    db.close()
    return render_template("books.html", books=books)

@app.route("/buy", methods=["POST"])
def buy():
    if "cart" not in session:
        session["cart"] = []

    book_id = request.form.get("id")
    if book_id:
        session["cart"].append(int(book_id))
        session.modified = True

    return redirect("/cart")

@app.route("/cart", methods=["GET"])
def show_cart():
    if "cart" not in session or not session["cart"]:
        return render_template("cart.html", books=[])

    db = get_db_connection()
    
    # Standard sqlite3 cannot pass a list directly into (?) like CS50's library.
    # We must generate the correct number of placeholders.
    placeholders = ",".join("?" for _ in session["cart"])
    query = f"SELECT * FROM books WHERE id IN ({placeholders})"
    
    books = db.execute(query, session["cart"]).fetchall()
    db.close()
    
    return render_template("cart.html", books=books)