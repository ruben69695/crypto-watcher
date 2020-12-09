# coinrow.py
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
from gi.repository.GdkPixbuf import Pixbuf

from .models import Coin

@Gtk.Template(resource_path='/org/gnome/cryptowatcher/coinRow.ui')
class CoinRow(Gtk.Box):
    """ Coin box representation """

    __gtype_name__ = 'CoinRow'

    _coin_icon: Gtk.Image = Gtk.Template.Child()
    _coin_name: Gtk.Label = Gtk.Template.Child()
    _coin_price: Gtk.Label = Gtk.Template.Child()

    def __init__(self, coin: Coin):
        Gtk.Box.__init__(self)
        self.coin_model = coin

        self._build_widgets()

    def _build_widgets(self):
        self._coin_name.set_text(self.coin_model.name)
        self._coin_price.set_text(str(self.coin_model.prices[0].value) + ' ' + self.coin_model.prices[0].unit.upper())

        pix = Pixbuf.new_from_resource_at_scale(
            self.coin_model.logo, 75, 75, True)
        
        self._coin_icon.set_from_pixbuf(pix)



