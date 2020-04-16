from iqoptionapi.stable_api import IQ_Option
import os
import sys
import logging
import time
# logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(message)s')


class OptionApi:
    
    MODE = 'PRACTICE' # TODO: Where to set PRACTICE / REAL?
 
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
        money = self.get_connection()
        money.update_ACTIVES_OPCODE()
        asset = money.get_all_ACTIVES_OPCODE()
        asset_lst = list(asset.keys())
        asset_lst.sort()
        return [(item, item) for item in asset_lst]
    
    def commit_trade(self, type, asset, amount, action, duration):
        print("COMMITANDO")
        money = self.get_connection()
        if type == 'digital':
            _, id = money.buy_digital_spot(asset, amount, action, duration)
        else:
            _, id = money.buy(asset, amount, action, duration)
            
        while not money.get_async_order(id):
            print(f'OPERATION ID = {id}')

        order_data = money.get_async_order(id)
        return order_data