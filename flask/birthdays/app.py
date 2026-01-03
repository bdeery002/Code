
import os
import sqlite3
from flask import Flask, redirect, render_template, request, g

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Database path (birthdays.db in the same directory as app.py)
DB_PATH = os.path.join(os.path.dirname(__file__), "birthdays.db")


# ---- Database helpers --------------------------------------------------------

def get_db():
    """Get a SQLite connection for the current request (dict-like rows)."""
    if "db" not in g:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row  # allow row["name"] or row["month"]
        g.db = conn
    return g.db


@app.teardown_appcontext
def close_db(exception=None):
    """Close the SQLite connection after the request."""
    db = g.pop("db", None)
    if db is not None:
        db.close()


def ensure_schema():
    """Create the birthdays table if it doesn't exist."""
    conn = sqlite3.connect(DB_PATH)
    with conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS birthdays (
                id INTEGER PRIMARY KEY,
                name TEXT,
                month INTEGER,
                day INTEGER
            );
            """
        )
    conn.close()


# Ensure schema on import so it works with `flask run` as well
ensure_schema()


# ---- Routes ------------------------------------------------------------------

@app.after_request
def after_request(response):
    """Disable caching for development convenience."""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    db = get_db()

    if request.method == "POST":
        # Read form values
        name = (request.form.get("name") or "").strip()
        month = request.form.get("month")
        day = request.form.get("day")

        # Minimal insert (SQLite will coerce numeric strings to INTEGER)
        db.execute(
            "INSERT INTO birthdays (name, month, day) VALUES (?, ?, ?)",
            (name, month, day)
        )
        db.commit()
        return redirect("/")

    # GET: fetch rows and render template
    birthdays = db.execute(
        "SELECT id, name, month, day FROM birthdays ORDER BY name ASC"
    ).fetchall()

    return render_template("index.html", birthdays=birthdays)


# ---- Entrypoint --------------------------------------------------------------

if __name__ == "__main__":
    # Also fine to run directly via `python app.py` in Codespaces
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=True)
