from crypt import methods
from flask import Flask, jsonify


app = Flask(__name__)



@app.route("/")
def home():
    print("Hello me")
    return f"""
    My Personal API<hr>
    <a href="/">Home Page</a><br>
    <a href="/aboutus">About Us</a><br>
    <a href="/info">Info Page</a><br>
    <a href="/fullinfo">Json full info</a><br>
    <a href="/api/v1.0/justice_league">justice_league Json</a><br>
    <a href="/api/v1.0/justice_league">justice_league Json</a><br>
    """


@app.route("/aboutus")
def aboutus():
    print("About Page")
    return """
    <h3>About Us</h3>
    <p>Hellow and welcome to our startup</p>
    """

@app.route("/info")
def info():
    print("Info Page")
    name = "Khaled Karman"
    age = 4500
    return f"""
    <h3>About Me</h3>
    <p>My name is <b>{name}</b></p>
    <p>I am <b>{age}</b> years old</p>
    """

@app.route("/fullinfo")
def fullinfo():
    print("Fullinfo Page")
    fullinfo = {
        "name": "Khaled Karman",
        "age": 4500
    }
    return jsonify(fullinfo)


justice_league_members = [
    {"superhero": "Aquaman", "real_name": "Arthur Curry"},
    {"superhero": "Batman", "real_name": "Bruce Wayne"},
    {"superhero": "Cyborg", "real_name": "Victor Stone"},
    {"superhero": "Flash", "real_name": "Barry Allen"},
    {"superhero": "Green Lantern", "real_name": "Hal Jordan"},
    {"superhero": "Superman", "real_name": "Clark Kent Kal-El"},
    {"superhero": "Wonder Woman", "real_name": "Princess Diana"}
]

@app.route("/api/v1.0/superhero/<superhero_name>")
def superhero(superhero_name):
    print("justice_league Page")
    val = {
        "Error": "Super hero name is wrong or it's not in our database"
    }
    for x in justice_league_members:
        if x["superhero"]==superhero_name:
            val = x
    return jsonify(val)

@app.route("/api/v1.0/real_name/<real_name>")
def real_name(real_name):
    print("justice_league Page")
    val = {
        "Error": "Real name is wrong or it's not in our database"
    }
    for x in justice_league_members:
        if x["real_name"]==real_name:
            val = x
    return jsonify(val)

@app.route("/api/v1.0/justice_league")
def justice_league():
    print("justice_league Page")
    fullinfo = {
        "name": "Khaled Karman",
        "age": 4500
    }
    return jsonify(justice_league_members)

if __name__=="__main__":
    app.run(debug=True)