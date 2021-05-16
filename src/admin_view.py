from tkinter import ttk, constants
from services.recycle_service import recycle_service
from tkinter.messagebox import askyesno


class AdminView:
    '''this class is responsible for the start view of the app'''
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

    def _admin_handler(self):
        password = self._password_entry.get()
        recycle_service.login_admin(password)
        self._handle_list()

    def show_users(self):
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
        self._logout_button.grid(columnspan=2, sticky=constants.EW, padx=5, pady=5)

    def del_user(self, username):
        recycle_service.remove_user(username)

    def confirm(self, username):
        tempname = askyesno(title="confirmation", message='Are you sure you want to delete this user?')
        if tempname:
            self.del_user(username)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(master=self._frame, text="Admin menu")

        self._show_users_button = ttk.Button(
            master=self._frame, text="Show users", command=self.show_users)

        self._logout_button = ttk.Button(
            master=self._frame, text="Logout", command=self._handle_start)

        heading_label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)
        self._show_users_button.grid(columnspan=2, sticky=constants.EW, padx=5, pady=5)
        self._logout_button.grid(columnspan=2, sticky=constants.EW, padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=300)
