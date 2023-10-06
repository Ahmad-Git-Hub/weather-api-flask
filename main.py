from flask import Flask, render_template
import pandas as pd

# this is website object using constructor
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/najiApi/v1/<station>/<date>")
def info(station, date):
    filename = "data_small/TG_STAID"+str(station).zfill(6)+".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10

    return {"station": station,
            "date": date,
            "temperature": temperature
            }


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)



