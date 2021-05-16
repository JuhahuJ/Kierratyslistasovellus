'''this module is responsible for the ui of the app'''
from ui.start_view import StartView
from ui.list_view import ListView
from ui.register_view import RegisterView
from ui.admin_login_view import AdminLoginView
from ui.admin_view import AdminView


class UI:
    '''this class is responsible for changing between the different views of the app'''

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

    def _handle_admin_login(self):
        self._show_admin_login_view()

    def _handle_admin(self):
        self._show_admin_view()

    def _show_start_view(self):
        self._hide_current_view()
        self._current_view = StartView(
            self._root, self._handle_list, self._handle_register, self._handle_admin_login)
        self._current_view.pack()

    def _show_list_view(self):
        self._hide_current_view()
        self._current_view = ListView(self._root, self._handle_start)
        self._current_view.pack()

    def _show_register_view(self):
        self._hide_current_view()
        self._current_view = RegisterView(self._root, self._handle_start)
        self._current_view.pack()

    def _show_admin_login_view(self):
        self._hide_current_view()
        self._current_view = AdminLoginView(
            self._root, self._handle_admin, self._handle_start)
        self._current_view.pack()

    def _show_admin_view(self):
        self._hide_current_view()
        self._current_view = AdminView(self._root, self._handle_start)
        self._current_view.pack()
