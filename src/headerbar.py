# headerbar.py
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

@Gtk.Template(resource_path='/org/gnome/cryptowatcher/headerBar.ui')
class HeaderBar(Gtk.HeaderBar):
    """Headerbar of the application"""

    __gtype_name__ = 'HeaderBar'

    _menu_button = Gtk.Template.Child()

    def __init__(self):
        Gtk.HeaderBar.__init__(self)
        
        self.set_title('Crypto Watcher')
        self._build_widget()

    def _build_widget(self):
        """
        Generate header widgets
        """
        self.set_show_close_button(True)

        # Prepare the menu options
        self.preferences_action = Gio.SimpleAction.new("preferences", None)
        self.about_action = Gio.SimpleAction.new("about", None)

        menu_model = Gio.Menu()
        menu_model.append("Preferences", "win.preferences")
        menu_model.append("About", "win.about")

        # Set options to the menu
        self._menu_button.set_menu_model(menu_model)

        # Set menu models actions
        self.preferences_action.connect("activate", self.preferences_callback)
        self.about_action.connect("activate", self.about_callback)

    def about_callback(self, action, parameter):
        print("You clicked \"About\"")

    def preferences_callback(self, action, parameter):
        print("You clicked \"Preferences\"")
