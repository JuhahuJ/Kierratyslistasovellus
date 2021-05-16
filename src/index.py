'''this module starts the app's functions'''
from tkinter import Tk
from ui.ui import UI


def main():
    '''creating the window loop for the app'''
    window = Tk()
    window.title("Kierrätys")

    ui = UI(window)
    ui.start()

    window.mainloop()


if __name__ == "__main__":
    main()
