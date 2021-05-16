from tkinter import ttk, constants
from services.recycle_service import recycle_service


class StartView:
    '''this class is responsible for the start view of the app'''
    def __init__(self, root, handle_list, handle_register, handle_admin_login):
        self._root = root
        self._username_entry = None
        self._password_entry = None
        self._handle_list = handle_list
        self._handle_register = handle_register
        self._handle_admin_login = handle_admin_login
        self._frame = None
        self._initialize()

    def pack(self):
        '''pack the frame'''
        self._frame.pack(fill=constants.X)

    def destroy(self):
        '''destroy the frame'''
        self._frame.destroy()

    def _login_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()
        recycle_service.login(username, password)
        self._handle_list()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(master=self._frame, text="Login")

        username_label = ttk.Label(master=self._frame, text="Username")
        self._username_entry = ttk.Entry(master=self._frame)

        password_label = ttk.Label(master=self._frame, text="Password")
        self._password_entry = ttk.Entry(master=self._frame)

        login_button = ttk.Button(
            master=self._frame, text="Login", command=self._login_handler)
        register_button = ttk.Button(
            master=self._frame, text="Register", command=self._handle_register)
        admin_button = ttk.Button(
            master=self._frame, text="Login as the admin", command=self._handle_admin_login)

        heading_label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)
        username_label.grid(padx=5, pady=5)
        self._username_entry.grid(
            row=1, column=1, sticky=constants.EW, padx=5, pady=5)
        password_label.grid(padx=5, pady=5)
        self._password_entry.grid(
            row=2, column=1, sticky=constants.EW, padx=5, pady=5)
        login_button.grid(columnspan=2, sticky=constants.EW, padx=5, pady=5)
        register_button.grid(columnspan=2, sticky=constants.EW, padx=5, pady=5)
        admin_button.grid(columnspan=2, sticky=constants.EW, padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=300)
