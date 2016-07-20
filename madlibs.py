from random import choice, sample

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet', methods=["POST", "GET"])
def greet_person():
    """Greet user."""
    if request.method == "POST":
        player = request.form.get("person")
    else:
        player = request.args.get("person")

    compliment = sample(AWESOMENESS, 3)

    return render_template("compliment.html",
                           person=player,
                           compliments=compliment)

@app.route('/game')
def show_madlib_form():
    """Gets user request tp play game"""

    form_answer = request.args.get('game')

    if form_answer == "yes":
        return render_template("game.html")
    else:
        return render_template("goodbye.html")


@app.route('/madlib')
def show_madlib():
    """Start the madlib game."""

    random_story = choice(['madlib.html', 'madlib2.html'])

    person = request.args.get('person')
    color = request.args.get('color')
    noun = request.args.get('noun')
    adj = request.args.get('adj')
    weather = request.args.getlist('weather')
    weather_list_length = len(weather)
    

    return render_template(random_story, 
                            person=person, 
                            color=color, 
                            noun=noun, 
                            adj=adj,
                            weather=weather,
                            weather_list_length=weather_list_length)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
