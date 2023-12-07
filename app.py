from flask import Flask, send_file, render_template
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
import yfinance as yf


# download 30 min data for the last 7 days for the given ticker
def get_data(ticker):
    data = yf.download(ticker, period="7d", interval="30m")
    # add title to the dataframe
    data["Ticker"] = ticker
    return data


# create a plot of the data and save it to a temporary buffer
def create_plot(data):
    ticker = data["Ticker"][0]
    fig, ax = plt.subplots()
    ax.plot(data["Close"])
    ax.set_title("Close Price of " + ticker)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.grid()
    fig.autofmt_xdate()
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    return buf


# create a Flask app
app = Flask(__name__)


# define the root route
@app.route("/")
def index():
    return render_template("index.html")


# define the route for the plot image
@app.route("/plot.png")
def plot_png():
    # get the ticker from the query parameters
    ticker = "MSFT"
    data = get_data(ticker)
    buf = create_plot(data)
    # embed the plot in the html output
    data = base64.b64encode(buf.read()).decode("ascii")
    return render_template("index.html", ticker=ticker, data=data)
