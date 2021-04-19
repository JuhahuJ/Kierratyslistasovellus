from tkinter import ttk, constants

class StartView:
    def __init__(self, root, handle_list):
        self._root = root
        self._username_entry = None
        self._password_entry = None
        self._handle_list = handle_list
        self._frame = None
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        
        heading_label = ttk.Label(master=self._frame, text="Login")

        username_label = ttk.Label(master=self._frame, text="Username")
        self._username_entry = ttk.Entry(master=self._frame)

        password_label = ttk.Label(master=self._frame, text="Password")
        self._password_entry = ttk.Entry(master=self._frame)

        button = ttk.Button(master=self._frame, text="Button", command=self._handle_list)
     
        heading_label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)
        username_label.grid(padx=5, pady=5)
        self._username_entry.grid(row=1, column=1, sticky=constants.EW, padx=5, pady=5)
        password_label.grid(padx=5, pady=5)  
        self._password_entry.grid(row=2, column=1, sticky=constants.EW, padx=5, pady=5)
        button.grid(columnspan=2, sticky=constants.EW, padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=300)

