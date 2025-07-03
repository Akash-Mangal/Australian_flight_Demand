import pandas as pd

def analyze_demand(price_data):
    if not price_data or 'price' not in price_data[0]:
        print("❌ Data does not contain 'price'. Here’s what came in:", price_data)
        return {}, []

    df = pd.DataFrame(price_data)
    df['price'] = df['price'].astype(float)
    df['demand_score'] = 1 / df['price']  # simple inverse relation

    insights = {
        "avg_price": round(df['price'].mean(), 2),
        "min_price": df['price'].min(),
        "max_price": df['price'].max(),
        "highest_demand_date": df.loc[df['demand_score'].idxmax(), 'departureDate'],
        "lowest_demand_date": df.loc[df['demand_score'].idxmin(), 'departureDate'],
    }
    return insights, df.to_dict(orient='records')