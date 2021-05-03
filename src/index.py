from tkinter import Tk
from start_view import StartView
from list_view import ListView
from register_view import RegisterView


class UI:
    '''this class is responsible for changing between the different views of the'''
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        '''starts the app'''
        self._show_start_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    def _handle_list(self):
        self._show_list_view()

    def _handle_start(self):
        self._show_start_view()

    def _handle_register(self):
        self._show_register_view()

    def _show_start_view(self):
        self._hide_current_view()
        self._current_view = StartView(
            self._root, self._handle_list, self._handle_register)
        self._current_view.pack()

    def _show_list_view(self):
        self._hide_current_view()
        self._current_view = ListView(self._root, self._handle_start)
        self._current_view.pack()

    def _show_register_view(self):
        self._hide_current_view()
        self._current_view = RegisterView(self._root, self._handle_start)
        self._current_view.pack()


window = Tk()
window.title("Kierrätys")

ui = UI(window)
ui.start()

window.mainloop()
