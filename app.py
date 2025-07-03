from flask import Flask, render_template, request
from scraper import get_price_graph
from processor import analyze_demand
from datetime import datetime

app = Flask(__name__)

# Dictionary of Australian airports using IATA codes
AIRPORTS = {
    "Sydney (SYD)": "SYD",
    "Melbourne (MEL)": "MEL",
    "Brisbane (BNE)": "BNE",
    "Perth (PER)": "PER",
    "Adelaide (ADL)": "ADL",
    "Gold Coast (OOL)": "OOL",
    "Canberra (CBR)": "CBR",
    "Hobart (HBA)": "HBA",
    "Cairns (CNS)": "CNS",
    "Townsville (TSV)": "TSV"
}

@app.route('/', methods=['GET', 'POST'])
def index():
    insights = None
    chart_data = []
    today = datetime.today().strftime('%Y-%m-%d')
    selected = {"origin": None, "destination": None, "date": today}

    if request.method == 'POST':
        origin = request.form['origin']
        destination = request.form['destination']
        date = request.form['date']

        selected = {"origin": origin, "destination": destination, "date": date}
        origin_code = AIRPORTS.get(origin)
        destination_code = AIRPORTS.get(destination)

        raw_data = get_price_graph(origin_code, destination_code, date)
        insights, chart_data = analyze_demand(raw_data)

    return render_template('index.html', insights=insights, chart_data=chart_data, airports=AIRPORTS, selected=selected)

if __name__ == '__main__':
    app.run(debug=True)
