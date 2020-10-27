import os

from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def YAM():
    fake_time = [999]
    status = "Yam's Python course is 16 weeks long..."
    if request.method == "GET":
        if len(request.args.getlist("weeks")) == 0:
            verdict = "What week are you in?"
            holishit_result = ""
        else:
            fake_time = request.args.getlist("weeks")
            fake_time = int(fake_time[0])
            time_left = (16 - fake_time) * 4
            verdict = f"You are at week: {fake_time}"
            holishit_result = f"that means you have {time_left} weeks to go!"
    return render_template("index.html",
                           status=status,
                           verdict=verdict,
                           holishit_result=holishit_result
                           )


if __name__ == "__main__":
    app.run(debug=False)
