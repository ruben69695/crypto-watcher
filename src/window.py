# window.py
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

from .headerbar import HeaderBar
from .coincontainer import CoinContainer


@Gtk.Template(resource_path='/org/gnome/cryptowatcher/window.ui')
class CryptoWatcherWindow(Gtk.ApplicationWindow):
    """ Main Window """

    __gtype_name__ = 'CryptoWatcherWindow'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._build_widgets()

    def _build_widgets(self):
        """
        Build main window widgets.
        """

        # Headerbar
        header_bar = HeaderBar()
        self.add_action(header_bar.preferences_action)
        self.add_action(header_bar.about_action)
        self.set_titlebar(header_bar)

        # Main container
        main_container = CoinContainer()
        self.add(main_container)