from api.alpaca_api import AlpacaApi
import json

if __name__ == "__main__":
    api = AlpacaApi()
    
    print(json.dumps(api.clean_account(), indent=2))