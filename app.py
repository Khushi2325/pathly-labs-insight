from flask import Flask, render_template, request
from analysis import analyze_stock

app = Flask(
    __name__,
    template_folder="../website/templates",
    static_folder="../website/static"
)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    symbol = request.args.get("symbol", "").upper().strip()

    if not symbol:
        return render_template("home.html", error="Enter a valid stock")

    if not symbol.endswith(".NS"):
        symbol += ".NS"

    return stock(symbol)

@app.route("/stock/<symbol>")
def stock(symbol):
    data = analyze_stock(symbol)

    if not data:
        return "No data found", 404

    return render_template("stock.html", data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
