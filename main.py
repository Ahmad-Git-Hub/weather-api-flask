from flask import Flask, render_template

# this is website object using constructor
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/najiApi/v1/<station>/<date>")
def about(station, date):
    temperature = 23
    return {"station": station,
            "date": date,
            "temperature": temperature

            }
    # return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)



