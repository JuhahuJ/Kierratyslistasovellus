from tkinter import ttk, constants
from services.recycle_service import recycle_service

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
        bottle_can_label = ttk.Label(master=self._frame, text="Bottles and cans recycled:")
        bottle_can_amount = ttk.Label(master=self._frame, text=recycle_service.recycle_list()[0])
        cardboard_label = ttk.Label(master=self._frame, text="Cardboard recycled:")
        cardboard_amount = ttk.Label(master=self._frame, text=recycle_service.recycle_list()[1])
        electronics_label = ttk.Label(master=self._frame, text="Electronics recycled:")
        electronics_amount = ttk.Label(master=self._frame, text=recycle_service.recycle_list()[2])
        glass_label = ttk.Label(master=self._frame, text="Glass recycled:")
        glass_amount = ttk.Label(master=self._frame, text=recycle_service.recycle_list()[3])
        metal_label = ttk.Label(master=self._frame, text="Metal recycled:")
        metal_amount = ttk.Label(master=self._frame, text=recycle_service.recycle_list()[4])
        plastic_label = ttk.Label(master=self._frame, text="Plastic recycled:")
        plastic_amount = ttk.Label(master=self._frame, text=recycle_service.recycle_list()[5])
        paper_label = ttk.Label(master=self._frame, text="Paper recycled:")
        paper_amount = ttk.Label(master=self._frame, text=recycle_service.recycle_list()[6])
        batteries_label = ttk.Label(master=self._frame, text="Batteries recycled:")
        batteries_amount = ttk.Label(master=self._frame, text=recycle_service.recycle_list()[7])
        clothes_label = ttk.Label(master=self._frame, text="Clothes recycled:")
        clothes_amount = ttk.Label(master=self._frame, text=recycle_service.recycle_list()[8])
        button = ttk.Button(master=self._frame, text="Logout", command=self._handle_start)

        label.grid(row=0, column=0)
        bottle_can_label.grid(row=1, column=0)
        bottle_can_amount.grid(row=1, column=1)
        cardboard_label.grid(row=2, column=0)
        cardboard_amount.grid(row=2, column=1)
        electronics_label.grid(row=3, column=0)
        electronics_amount.grid(row=3, column=1)
        glass_label.grid(row=4, column=0)
        glass_amount.grid(row=4, column=1)
        metal_label.grid(row=5, column=0)
        metal_amount.grid(row=5, column=1)
        plastic_label.grid(row=6, column=0)
        plastic_amount.grid(row=6, column=1)
        paper_label.grid(row=7, column=0)
        paper_amount.grid(row=7, column=1)
        batteries_label.grid(row=8, column=0)
        batteries_amount.grid(row=8, column=1)
        clothes_label.grid(row=9, column=0)
        clothes_amount.grid(row=9, column=1)
        button.grid()
        