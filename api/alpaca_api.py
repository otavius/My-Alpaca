from alpaca.trading.client import TradingClient 
from config.paper_account import APCA_API_KEY_ID, APCA_API_SCRET_KEY



class AlpacaApi:
    
    def __init__(self):
        self.client = TradingClient(APCA_API_KEY_ID, APCA_API_SCRET_KEY)
        
    def account_details(self):
        account = self.client.get_account()
        return account
    
    def clean_account(self):
        return {
            "account_number ": self.account_details().account_number,
            "PDT_Rule": self.account_details().pattern_day_trader,
            "currency": self.account_details().currency,
            "cash": self.account_details().cash,
            "margin": self.account_details().initial_margin,
            "portfolio_value": self.account_details().portfolio_value,
            "buying_power": self.account_details().buying_power,
            "options_buying_power": self.account_details().options_buying_power,
            "options_approved_level": self.account_details().options_approved_level,
            "options_trading_level": self.account_details().options_trading_level
        }