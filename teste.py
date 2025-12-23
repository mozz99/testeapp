from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import pandas as pd
from datetime import datetime


def buscar_dados_crypto(simbolo, convert="BRL", amount=1, api_key="xxxx"):
    url = "https://pro-api.coinmarketcap.com/v2/tools/price-conversion"

    parameters = {
        "amount": amount,
        "symbol": simbolo,
        "convert": convert
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

        # 🔍 Validação da resposta
        if "data" not in data:
            print("Erro retornado pela API:")
            print(data["status"])
            return None

        # Extrações seguras
        price = data["data"][0]["quote"][convert]["price"]
        api_timestamp = data["status"].get("timestamp")
        request_datetime = datetime.now()

        df = pd.DataFrame({
            "datetime_request": [request_datetime],
            "api_timestamp": [api_timestamp],
            "Close": [price],
            "simbolo": [simbolo],
            "moeda": [convert]
        })

        return df

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print("Erro de conexão:", e)
        return None

df = buscar_dados_crypto("DOGE", api_key="6fb2273e-bce0-4762-9075-cd71e817b4b3")
print(df)