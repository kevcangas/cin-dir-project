import tkinter as tk
from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


class App(tk.Tk):

    def __init__(self, *args, **kwargs) -> None:
        
        tk.Tk.__init__(self, *args, **kwargs)

        self.theta=[]
        self.d=[]
        self.a=[]
        self.alpha=[]

        self.main_frame = tk.Frame(self, bg="#708090", height=631, width=826)
        self.main_frame.pack(fill="both", expand="true")

        self.geometry("826x631")  # Sets window size to 626w x 431h pixels
        self.resizable(0, 0)  # This prevents any resizing of the screen

        text_styles = {"font": ("Verdana", 10),
                       "background": "#708090",
                       "foreground": "#E1FFFF"}

        label_data = tk.Label(self.main_frame, text_styles, text="Denavit Hartenberg parameters")
        label_data.grid(row=1, column=0)

        #theta
        label_theta = tk.Label(self.main_frame, text_styles, text="theta")
        label_theta.grid(row=2, column=0)

        self.entry_theta = ttk.Entry(self.main_frame, width=10, cursor="xterm")
        self.entry_theta.grid(row=2, column=1)

        #d
        label_d = tk.Label(self.main_frame, text_styles, text="d")
        label_d.grid(row=3, column=0)

        self.entry_d = ttk.Entry(self.main_frame, width=10, cursor="xterm")
        self.entry_d.grid(row=3, column=1)

        #a
        label_a = tk.Label(self.main_frame, text_styles, text="a")
        label_a.grid(row=4, column=0)

        self.entry_a = ttk.Entry(self.main_frame, width=10, cursor="xterm")
        self.entry_a.grid(row=4, column=1)

        #alpha
        label_alpha = tk.Label(self.main_frame, text_styles, text="alpha")
        label_alpha.grid(row=5, column=0)

        self.entry_alpha = ttk.Entry(self.main_frame, width=10, cursor="xterm")
        self.entry_alpha.grid(row=5, column=1)

        #Control buttons
        button_add = ttk.Button(self.main_frame, text="Add slabon", command=lambda: parameters_table())
        button_add.grid(row=6, column=0)

        button_plot = ttk.Button(self.main_frame, text="Plot robot")
        button_plot.grid(row=6, column=1)
    

        def parameters_table():
            self.theta.append(int(self.entry_theta.get()))
            self.d.append(int(self.entry_d.get()))
            self.a.append(int(self.entry_a.get()))
            self.alpha.append(int(self.entry_alpha.get()))

            total_rows = len(self.theta)
            for i in range(total_rows):
                self.e = Entry(self.main_frame, width=5, fg='black',font=('Arial',10))

                self.e.grid(row=i+10, column=16)
                self.e.insert(END, str(self.theta[i]))

                self.e = Entry(self.main_frame, width=5, fg='black',font=('Arial',10))

                self.e.grid(row=i+10, column=17)
                self.e.insert(END, str(self.d[i]))

                self.e = Entry(self.main_frame, width=5, fg='black',font=('Arial',10))

                self.e.grid(row=i+10, column=18)
                self.e.insert(END, str(self.a[i]))

                self.e = Entry(self.main_frame, width=5, fg='black',font=('Arial',10))

                self.e.grid(row=i+10, column=19)
                self.e.insert(END, str(self.alpha[i]))


def run():
    root = App()
    root.mainloop()


if __name__ == '__main__':
    run()