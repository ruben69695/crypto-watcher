# coincontainer.py
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

from gi.repository import Gtk
from gi.repository import Gio

from .models import Coin
from .coinrow import CoinRow


@Gtk.Template(resource_path='/org/gnome/cryptowatcher/coinContainer.ui')
class CoinContainer(Gtk.Box):
    """ Main window container """

    __gtype_name__ = 'CoinContainer'

    def __init__(self):
        Gtk.Box.__init__(self)
        
        self.coins = [
            Coin('Bitcoin', '$19,121.27 USDT', '/org/gnome/cryptowatcher/images/bitcoin.png'),
            Coin('Ethereum', '$593.12 USDT', '/org/gnome/cryptowatcher/images/ethereum.png'),
            Coin('Litecoin', '$82.60 USDT', '/org/gnome/cryptowatcher/images/litecoin.png')
        ]
        
        self._build_widgets()

    def _build_widgets(self):
        
        for coin in self.coins:
            self.add(CoinRow(coin))


