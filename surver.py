from flask import Flask, render_template, request, redirect
app= Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ninjas')
def ninjas():
    return render_template("ninjas.html")

@app.route('/ninjas/<ninja_color>')
def color(ninja_color):
    if ninja_color == "red":
        return render_template("red.html")
    elif ninja_color == "blue":
        return render_template("blue.html")
    elif ninja_color == "purple":
        return render_template("purple.html")
    elif ninja_color == "orange":
        return render_template("orange.html")
    else:
        return render_template("april.html")
app.run(debug=True)