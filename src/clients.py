# clients.py
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

import json
from requests_futures.sessions import FuturesSession


class CoinClient:

    def __init__(self, base_url='https://api.coingecko.com/api/v3/', timeout=60):
        self.base_url = base_url
        self.timeout = timeout

    def _build_query_string(self, data_dictionary):
        query_string = ''

        if data_dictionary:
            query_string += '?'
            for key, value in data_dictionary.items():
                query_string += f"{key}={value}&"

        return query_string
    
    def get_coins(self, coin_list, currency_list):
        session = FuturesSession()
        endpoint = 'simple/price'

        coins_ids = ','.join(coin_list)
        currencies = ','.join(currency_list)
        query_string = self._build_query_string({ 
            'ids': coins_ids, 
            'vs_currencies': currencies, 
            'include_last_updated_at': 'true'
        })

        future = session.get(self.base_url + endpoint + query_string)
        response = future.result()

        return response.json()
        
    
