
# ✈️ Flight Demand Predictor

A web-based application that visualizes and analyzes airline market demand trends based on real-time price data. Designed for travel businesses, hostel networks, and analysts, it helps identify high-demand periods and optimal travel dates using dynamic pricing insights.

---

## 🔧 Features

- **Real-Time Price Data** – Integrates with a third-party flight price API.
- **Demand Analysis** – Calculates average, minimum, and maximum price points.
- **Insightful Metrics** – Highlights dates with highest and lowest demand.
- **Interactive UI** – Simple dropdown interface with chart-based visual output.
- **Price Chart** – Monthly trend displayed using Chart.js.

---

## 🗂️ Project Structure

```

├── app.py            # Main Flask application
├── scraper.py        # Flight price API integration
├── processor.py      # Demand calculation logic
├── chatbot.py        # (Optional) for LangChain-based extensions
├── templates/
│   └── index.html    # HTML frontend + chart rendering

````

---

## 🌐 Supported Australian Airports (IATA)

- Sydney (SYD)
- Melbourne (MEL)
- Brisbane (BNE)
- Perth (PER)
- Adelaide (ADL)
- Gold Coast (OOL)
- Canberra (CBR)
- Hobart (HBA)
- Cairns (CNS)
- Townsville (TSV)

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/flight-demand-predictor.git
cd flight-demand-predictor
````

### 2. Install Dependencies

```bash
pip install flask pandas requests
```

### 3. Set Up API Key

Edit `scraper.py` and replace:

```python
'x-rapidapi-key': "YOUR_API_KEY"
```

with your [RapidAPI](https://rapidapi.com/) key.

---

### 4. Run the App

```bash
python app.py
```

Then open your browser at `http://127.0.0.1:5000`.

---

## 📊 Example Output

* Average Price: \$38.5
* Lowest Price: \$37 on 2025-07-10
* Highest Demand: 2025-07-14
* Live Chart: Price vs Date for 1 month

---
