from flask import Flask, render_template, request
from random import randint

app = Flask(__name__)


@app.route("/")
def index() -> None:
    return render_template("index.html")


@app.route("/roll<int:num>d<int:dice>", methods=["GET"])
def roll(num, dice) -> None:
    count = 0
    result = 0
    while count < num:
        result += randint(1, dice)
        count += 1
    score = str(result)
    num_string = str(num)
    dice_string = str(dice)
    score_string = str(score)
    f = open("scores.txt", "a")
    f.write(f"\n{num_string}d{dice_string} => {score_string}\n")
    f.close()
    return render_template("roll.html", num_string=num_string, dice_string=dice_string, score_string=score_string)


if __name__ == "__main__":
    app.run(port=8080)
