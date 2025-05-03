from tkinter import *

class Display :
    def __init__(self):
        pass

    def main_windows(self):
        app = Tk()
        app.title("PyTask")
        app.geometry("600x725")
        app.maxsize(700,825)
        app.minsize(560,585)

        app.mainloop()