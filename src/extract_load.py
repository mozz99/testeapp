# import
import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from datetime import datetime

# import das minhas variaveis de ambiente

load_dotenv()

commodities = ['DOGE', 'ETH', 'BTC', 'XRP', 'LTC', 'BCH', 'ADA', 'SOL', 'DOT']

DB_HOST = os.getenv('DB_HOST_PROD')
DB_PORT = os.getenv('DB_PORT_PROD')
DB_NAME = os.getenv('DB_NAME_PROD')
DB_USER = os.getenv('DB_USER_PROD')
DB_PASS = os.getenv('DB_PASS_PROD')
DB_SCHEMA = os.getenv('DB_SCHEMA_PROD')

API_KEY = os.getenv('API_KEY')

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)


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


def buscar_todos_dados_commodities(commodities):
    todos_dados = []
    for simbolo in commodities:
        dados = buscar_dados_crypto(simbolo, api_key=API_KEY)
        todos_dados.append(dados)
    return pd.concat(todos_dados)


def salvar_no_postgres(df, schema='public'):
    df.to_sql('commodities', engine, if_exists='append',
              index=True, index_label='Date', schema=schema)


if __name__ == "__main__":
    dados_concatenados = buscar_todos_dados_commodities(commodities)
    salvar_no_postgres(dados_concatenados, schema='public')
    print(dados_concatenados)


# pegar a cotacao dos meus ativos

# concatenar os meus ativos (1..2...3) -> (1)

# salvar no banco de dados
