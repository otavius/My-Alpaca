import datetime 
from pydantic.dataclasses import dataclass
import decimal

@dataclass
class Account:
    account_number:int
    currency:str
    cash:float 
    portfolio_value:int 
    equity:int