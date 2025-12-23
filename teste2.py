from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import pandas as pd
from datetime import datetime, timedelta


def buscar_eth_24h(api_key, convert="BRL"):
    url = "https://pro-api.coinmarketcap.com/v2/cryptocurrency/ohlcv/historical"

    end_time = datetime.utcnow()
    start_time = end_time - timedelta(hours=24)

    parameters = {
        "symbol": "ETH",
        "convert": convert,
        "time_start": start_time.strftime("%Y-%m-%dT%H:%M:%S"),
        "time_end": end_time.strftime("%Y-%m-%dT%H:%M:%S"),
        "interval": "hourly"
    }

    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": api_key
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = response.json()

        if "data" not in data:
            print("Erro retornado pela API:")
            print(data["status"])
            return None

        quotes = data["data"]["quotes"]

        registros = []
        for q in quotes:
            registros.append({
                "datetime": q["time_open"],
                "Close": q["quote"][convert]["close"],
                "simbolo": "ETH",
                "moeda": convert
            })

        df = pd.DataFrame(registros)
        df["datetime"] = pd.to_datetime(df["datetime"])

        return df

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print("Erro de conexão:", e)
        return None

df = buscar_eth_24h(api_key="6fb2273e-bce0-4762-9075-cd71e817b4b3")
print(df)
