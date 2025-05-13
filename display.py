from tkinter import *

class Display :
    def __init__(self):
        pass

    def main_windows(self):
        bg_color = "#8f8bd6"
        app = Tk()
        app.title("PyTask")
        app.config(bg=bg_color)
        app.geometry("600x725")
        app.maxsize(700,825)
        app.minsize(560,585)

        #Bandeau
        bg_band_color = "#3933b5"
        band = Frame(app,bg= bg_band_color)
        title = Label(band,text="PyTask",font=("Impact",16),fg="white",bg = bg_band_color)
        title.pack(padx=30,pady=30)

        band.pack(side=TOP,fill=X)

        app.mainloop()


display = Display()
display.main_windows()