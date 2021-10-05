from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'quiet'

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/survey", methods=["POST"])
def vote():
    session["name"]=request.form["name"]
    session["location"]=request.form["location"]
    session["language"]=request.form["language"]
    session["comment"]=request.form["comment"]

    return redirect("/results")

@app.route("/results")
def result():
    return render_template("results.html")

if __name__ == "__main__":
    app.run(debug=True)