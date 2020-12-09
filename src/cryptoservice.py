# cryptoservice.py
#
# Copyright 2020 Ruben Arrebola de Haro
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from .constants import *
from .models import Coin

from threading import Timer


SUPPORTED_COINS = [
    BITCOIN,
    ETHEREUM,
    LITECOIN
]

SUPPORTED_CURRENCIES = [
    USD_KEY,
    EUROS_KEY
]

class Event:

    def __init__(self):
        self.listeners = []

    def __iadd__(self, listener):
        """Shortcut for using += to add a listener."""
        self.listeners.append(listener)
        return self

    def notify(self, *args, **kwargs):
        for listener in self.listeners:
            listener(*args, **kwargs)

class RepeatedTimer:
    
    def __init__(self, interval, listener):
        self._timer: Timer
        self.interval = interval
        self.listener = listener
        self.is_running = False

    def start(self):
        if (not self.is_running):
            self.is_running = True
            self._timer = Timer(self.interval, self._control_handler)
            self._timer.daemon = True
            self._timer.start()
    
    def stop(self):
        """ 
        Stop the timer, and cancel the execution of the timer’s action. 
        This will only work if the timer is still in its waiting stage. 
        """
        self._timer.cancel()
        self.is_running = False

    def _control_handler(self):
        try:
            self.stop()
            self.listener()
        except Exception as identifier:
            print(identifier)
        finally:
            self.start()

class CryptoService:

    def __init__(self, crypto_client):
        self.crypto_client = crypto_client
        self.on_coins_update = Event()
        self.coins = []
        self.timer = RepeatedTimer(15, self._refresh_data)
        self.timer.start()
        
    def _refresh_data(self):
        json = self.crypto_client.get_coins(SUPPORTED_COINS, SUPPORTED_CURRENCIES)

        print(json)

        for coin in SUPPORTED_COINS:
            self.coins.append(Coin.load_from_json(json, coin))
            self.coins[-1].logo = self.get_resource_logo_by_coin_name(coin)

        self.on_coins_update.notify(self.coins)

    def get_resource_logo_by_coin_name(self, coin_name):
        if coin_name == BITCOIN:
            return '/org/gnome/cryptowatcher/images/bitcoin.png'
        elif coin_name == ETHEREUM:
            return '/org/gnome/cryptowatcher/images/ethereum.png'
        elif coin_name == LITECOIN:
            return '/org/gnome/cryptowatcher/images/litecoin.png'
        else:
            raise Exception('Not supported coin name to extract the logo resource')


    


