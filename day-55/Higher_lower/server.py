from flask import Flask
import random

app = Flask(__name__)

random_num = random.randint(0, 9)
print(random_num)

img = "https://media.giphy.com/media/UDU4oUJIHDJgQ/giphy.gif"
text = "Guess a number between 0 and 9"
color = 'black'


@app.route("/")
def Guess():
    return f"<h1>{text}</h1><img src={img}>"


@app.route("/<int:number>")
def checkGuess(number):
    global img, text, color
    if number != random_num:
        if number < random_num:
            text = "Too Low"
            img = "https://media.giphy.com/media/TgmiJ4AZ3HSiIqpOj6/giphy.gif"
        elif number > random_num:
            text = "Too High"
            img = "https://media.giphy.com/media/27sdoZn8YhLbil01q6/giphy.gif"
        color = "red"
    else:
        text = "Correct"
        img = "https://media.giphy.com/media/PS7d4tm1Hq6Sk/giphy.gif"
        color = "green"
    return f"<h1 style='color:{color};'>{text}</h1><img src={img}>"


if __name__ == "__main__":
    app.run(debug=True)
