# coin.py
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

class Coin:

    def __init__(self):
        self.name = ''
        self.prices = []
        self.logo = ''

    @staticmethod
    def load_from_json(json_data, coin_name):
        data = json_data[coin_name]

        coin = Coin()
        coin.name = coin_name.capitalize()
        coin.prices.append(Price(USD_KEY, data[USD_KEY]))
        coin.prices.append(Price(EUROS_KEY, data[EUROS_KEY]))
        return coin

class Price:

    def __init__(self, unit, value):
        self.unit = unit
        self.value = value