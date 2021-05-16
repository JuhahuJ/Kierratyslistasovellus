from tkinter import ttk, constants
from services.recycle_service import recycle_service


class AdminView:
    '''this class is responsible for the start view of the app'''
    def __init__(self, root, handle_start):
        self._root = root
        self._password_entry = None
        self._handle_start = handle_start
        self._frame = None
        self._initialize()

    def pack(self):
        '''pack the frame'''
        self._frame.pack(fill=constants.X)

    def destroy(self):
        '''destroy the frame'''
        self._frame.destroy()

    def _admin_handler(self):
        password = self._password_entry.get()
        recycle_service.login_admin(password)
        self._handle_list()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(master=self._frame, text="Admin login")

        password_label = ttk.Label(master=self._frame, text="Password")
        self._password_entry = ttk.Entry(master=self._frame)

        logout_button = ttk.Button(
            master=self._frame, text="Logout", command=self._handle_start)

        heading_label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)
        password_label.grid(padx=5, pady=5)
        self._password_entry.grid(
            row=2, column=1, sticky=constants.EW, padx=5, pady=5)
        logout_button.grid(columnspan=2, sticky=constants.EW, padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=300)
