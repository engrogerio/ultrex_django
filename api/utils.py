from iqoptionapi.stable_api import IQ_Option
import os
import sys


class OptionApi:
    
    MODE = 'PRACTICE' # TODO: Where to set PRACTICE / REAL?
    def __init__(self):
        self.connection = self.get_connection()
        # self.asset = self.get_asset()
        
    def get_connection(self):
        user = os.environ.get('IQOPTIONAPI_USER', None)
        password = os.environ.get('IQOPTIONAPI_PASS', None)
        if user:
            connection = IQ_Option(user, password)
            connection.connect()
            connection.change_balance(self.MODE)
            return connection
        else:
            sys.exit("Missing environment variables!")

    def get_asset_list(self):
        money = self.connection
        money.update_ACTIVES_OPCODE()
        asset = money.get_all_ACTIVES_OPCODE()
        asset_lst = list(asset.keys())
        asset_lst.sort()
        return [(item, item) for item in asset_lst]