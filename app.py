from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Needed for session
@app.route("/", methods=["GET", "POST"])
def index():
    if "number" not in session:
        session["number"] = random.randint(1, 100)
        session["attempts"] = 7

    message = ""

    if request.method == "POST":
        try:
            guess = int(request.form["guess"])
        except ValueError:
            message = "Please enter a valid number."
            return render_template("index.html", message=message)

        session["attempts"] -= 1

        if guess == session["number"]:
            message = f"🎉 Correct! The number was {session['number']}."
            session.clear()
        elif session["attempts"] == 0:
            message = f"😢 Out of attempts! The number was {session['number']}."
            session.clear()
        elif guess < session["number"]:
            message = f"🔼 Too low! Attempts left: {session['attempts']}"
        else:
            message = f"🔽 Too high! Attempts left: {session['attempts']}"

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
