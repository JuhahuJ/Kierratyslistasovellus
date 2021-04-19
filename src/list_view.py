from tkinter import ttk, constants

class ListView:
    def __init__(self, root, handle_start):
        self._root = root
        self._handle_start = handle_start
        self._frame = None
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Recycling list")

        button = ttk.Button(master=self._frame, text="Logout", command=self._handle_start)

        label.grid(row=0, column=0)
        button.grid(row=1, column=1)