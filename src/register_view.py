from tkinter import ttk, constants
from entities.user import User
from services.recycle_service import recycle_service

class RegisterView:
    def __init__(self, root, handle_start):
        self._root = root
        self._username_entry = None
        self._password_entry = None
        self._handle_start = handle_start
        self._frame = None
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _register_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()
        recycle_service.register(username, password)  
        self._handle_start()



    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        
        heading_label = ttk.Label(master=self._frame, text="Register")

        username_label = ttk.Label(master=self._frame, text="Username")
        self._username_entry = ttk.Entry(master=self._frame)

        password_label = ttk.Label(master=self._frame, text="Password")
        self._password_entry = ttk.Entry(master=self._frame)

        button = ttk.Button(master=self._frame, text="Create account", command=self._register_handler)
     
        heading_label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)
        username_label.grid(padx=5, pady=5)
        self._username_entry.grid(row=1, column=1, sticky=constants.EW, padx=5, pady=5)
        password_label.grid(padx=5, pady=5)  
        self._password_entry.grid(row=2, column=1, sticky=constants.EW, padx=5, pady=5)
        button.grid(columnspan=2, sticky=constants.EW, padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=300)