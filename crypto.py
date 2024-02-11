# import json
# import websocket
# import pandas as pd

assets = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT']
assets = [coin.lower() + '@kline_1m' for coin in assets]
assets_link = '/'.join(assets)

socket = "wss://stream.binance.com:9433/stream?streams="+assets_link

def get_crypto_string():
    return socket
