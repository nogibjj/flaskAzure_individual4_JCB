from flask import Flask, send_file, render_template, request
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import yfinance as yf
import numpy as np


# download 30 min data for the last 7 days for the given ticker
def get_data(ticker):
    data = yf.download(ticker, period="7d", interval="5m")
    # add title to the dataframe
    data["Ticker"] = ticker
    return data


# create a plot of the data and save it to a temporary buffer


def create_plot(data):
    ticker_name = data["Ticker"][0]

    fig, ax = plt.subplots()

    # Convert the index to integers
    ax.plot(range(len(data)), data["Close"])

    ax.set_title("Close Price of " + ticker_name)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.grid()

    # Create a function to format the x-axis ticks
    def format_date(x, pos=None):
        thisind = np.clip(int(x + 0.5), 0, len(data.index) - 1)
        return data.index[thisind].strftime("%Y-%m-%d")

    # Set the x-axis formatter
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))

    fig.autofmt_xdate()
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    return buf




app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        ticker = request.form.get("ticker")
        data = get_data(ticker)
        buf = create_plot(data)
        buf.seek(0)
        return send_file(buf, mimetype='image/png')
    return render_template("index.html")

@app.route("/plot.png")
def plot_png():
    ticker = request.args.get('ticker')
    data = get_data(ticker)
    buf = create_plot(data)
    buf.seek(0)
    return send_file(buf, mimetype='image/png')


if __name__ == "__main__":
    app.run(debug=True)
