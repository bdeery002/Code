# App.y is Analogous to "The Manager" It listens for customers (URLs), decides which chef (function) should handle the order, and sends the final plate (HTML) back to the table.

# The manager brings in three specialists
# Flask: render_template: The "Plater" who knows how to combine data with HTML files.
#request: The "Mailroom Clerk" who looks at what the user sent (like their name in the URL).

from flask import Flask, render_template, request

# This line creates the Application Object. It’s the Manager putting on their uniform and looking around the room. By saying __name__, the Manager is orienting themselves: "Okay, I'm running in this folder, so I should look for a templates folder right here next to me."
app = Flask(__name__)

# Define the route for the root URL ("/")

@app.route("/", methods =["GET", "POST"])
def index():
    if request.method == "POST":
        return render_template("greet.html", name=request.form.get("name", "world"))
    else:
        return render_template("index.html")
