import requests

def get_price_graph(departure_id, arrival_id, departure_date):
    url = f"https://google-flights4.p.rapidapi.com/price-graph/for-one-way?departureId={departure_id}&arrivalId={arrival_id}&departureDate={departure_date}"

    headers = {
        'x-rapidapi-key': "492cd2f13amsh057f16e070e36f3p1f4122jsnc0a6a47f6f64",
        'x-rapidapi-host': "google-flights4.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("❌ Error:", response.status_code, response.text)
        return []

    print("✅ Response received from API")
    return response.json().get("data", [])
