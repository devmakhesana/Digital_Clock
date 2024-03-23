from tkinter import *
import datetime


class Clock:
    def __init__(self):
        self.root = Tk()
        self.root.title("Digital Clock")
        self.root.attributes('-fullscreen', True)
        self.root.config(bg="#1E1F22")
        self.digital_clock()
        self.root.mainloop()

    def digital_clock(self):
        digital_clock = Frame(self.root, borderwidth=0, relief='raised', bg='#1E1F22', highlightcolor='white', highlightthickness=0)
        digital_clock.pack(side='top', pady=300, padx=100)

        self.time_var = StringVar()
        self.time_var.set(datetime.datetime.now().strftime('%c'))

        clock_label = Label(digital_clock, textvariable=self.time_var, fg='white', font=("Times New Roman", 90), justify='center', bg='#1E1F22')
        clock_label.pack()

        self.update_clock()

    def update_clock(self):
        self.time_var.set(datetime.datetime.now().strftime('%c'))
        self.root.after(1000, self.update_clock)


if __name__ == '__main__':
    Clock()
