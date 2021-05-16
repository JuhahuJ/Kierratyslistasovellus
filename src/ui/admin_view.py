'''this module is responsible for admin view'''
from tkinter import ttk, constants
from tkinter.messagebox import askyesno
from services.recycle_service import recycle_service


class AdminView:
    '''this class is responsible for the admin view of the app'''

    def __init__(self, root, handle_start):
        self._root = root
        self._password_entry = None
        self._show_users_button = None
        self._logout_button = None
        self._handle_start = handle_start
        self._frame = None
        self._initialize()

    def pack(self):
        '''pack the frame'''
        self._frame.pack(fill=constants.X)

    def destroy(self):
        '''destroy the frame'''
        self._frame.destroy()

    def show_users(self):
        '''show all registered users'''
        self._show_users_button.destroy()
        self._logout_button.destroy()
        users_label = ttk.Label(master=self._frame, text="Users:")
        users_label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)
        for i in range(len(recycle_service.get_users())):
            user_button = ttk.Button(
                master=self._frame, text=(recycle_service.get_users()[i][1]), command=lambda j=recycle_service.get_users()[i][1]: self.confirm(j))
            user_button.grid(columnspan=2, sticky=constants.EW, padx=5, pady=5)
        self._logout_button = ttk.Button(
            master=self._frame, text="Logout", command=self._handle_start)
        self._logout_button.grid(
            columnspan=2, sticky=constants.EW, padx=5, pady=5)

    def show_stats(self):
        '''shows amount of recycled materials of all users'''
        self._show_stats_button.destroy()
        self._logout_button.destroy()
        recycle_amount_label = ttk.Label(
            master=self._frame, text="Amount recycled by all users")
        recycle_amount_label.grid(padx=5, pady=5, column=2)
        list_of_recyclables = ["Bottles and cans", "Cardboard", "Electronics",
                               "Glass", "Metal", "Plastic", "Paper", "Batteries", "Clothes"]
        for i in range(0, 8):
            recyclable_label = ttk.Label(master=self._frame, text=(
                list_of_recyclables[i], "recycled:"))
            recyclable_amount_label = ttk.Label(
                master=self._frame, text=recycle_service.recycle_list_all()[i])
            recyclable_label.grid(padx=5, pady=5, column=1)
            recyclable_amount_label.grid(padx=5, pady=5, column=2)
        self._logout_button = ttk.Button(
            master=self._frame, text="Logout", command=self._handle_start)
        self._logout_button.grid(
            columnspan=2, sticky=constants.EW, padx=5, pady=5)

    def confirm(self, username):
        '''confirm that admin wants to delete a user'''
        deleteconfirmation = askyesno(
            title="confirmation", message='Are you sure you want to delete this user?')
        if deleteconfirmation:
            recycle_service.remove_user(username)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(master=self._frame, text="Admin menu")

        self._show_users_button = ttk.Button(
            master=self._frame, text="Show users", command=self.show_users)

        self._show_stats_button = ttk.Button(
            master=self._frame, text="Show statistics", command=self.show_stats)

        self._logout_button = ttk.Button(
            master=self._frame, text="Logout", command=self._handle_start)

        heading_label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)
        self._show_users_button.grid(
            columnspan=2, sticky=constants.EW, padx=5, pady=5)
        self._show_stats_button.grid(
            columnspan=2, sticky=constants.EW, padx=5, pady=5)
        self._logout_button.grid(
            columnspan=2, sticky=constants.EW, padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=200)
