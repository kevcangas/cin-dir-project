import tkinter as tk
from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure

from robot import Robot


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
        label_data.place(x=30, y=30)

        #theta
        label_theta = tk.Label(self.main_frame, text_styles, text="theta")
        label_theta.place(x=30, y=60)

        self.entry_theta = ttk.Entry(self.main_frame, width=10, cursor="xterm")
        self.entry_theta.place(x=150, y=60)

        #d
        label_d = tk.Label(self.main_frame, text_styles, text="d")
        label_d.place(x=30, y=90)

        self.entry_d = ttk.Entry(self.main_frame, width=10, cursor="xterm")
        self.entry_d.place(x=150, y=90)

        #a
        label_a = tk.Label(self.main_frame, text_styles, text="a")
        label_a.place(x=30, y=120)

        self.entry_a = ttk.Entry(self.main_frame, width=10, cursor="xterm")
        self.entry_a.place(x=150, y=120)

        #alpha
        label_alpha = tk.Label(self.main_frame, text_styles, text="alpha")
        label_alpha.place(x=30, y=150)

        self.entry_alpha = ttk.Entry(self.main_frame, width=10, cursor="xterm")
        self.entry_alpha.place(x=150, y=150)

        #Control buttons
        button_add = ttk.Button(self.main_frame, text="Add slabon", command=lambda: parameters_table())
        button_add.place(x=30, y=180)

        button_plot = ttk.Button(self.main_frame, text="Plot robot", command=lambda: plot_robot())
        button_plot.place(x=150, y=180)

        #Table parameters
        title_table = tk.Label(self.main_frame, text_styles, text="Parameters selected")
        title_table.place(x=300, y=30)
        self.e = tk.Label(self.main_frame, width=5, fg='black',font=('Arial',10), text="Theta")
        self.e.place(x=300, y=60)
        self.e = tk.Label(self.main_frame, width=5, fg='black',font=('Arial',10), text="d")
        self.e.place(x=350, y=60)
        self.e = tk.Label(self.main_frame, width=5, fg='black',font=('Arial',10), text="a")
        self.e.place(x=400, y=60)
        self.e = tk.Label(self.main_frame, width=5, fg='black',font=('Arial',10), text="alpha")
        self.e.place(x=450, y=60)
        
    
        #Add data to table
        def parameters_table():
            self.theta.append(int(self.entry_theta.get()))
            self.d.append(int(self.entry_d.get()))
            self.a.append(int(self.entry_a.get()))
            self.alpha.append(int(self.entry_alpha.get()))

            total_rows = len(self.theta)
            for i in range(total_rows):
                self.e = Entry(self.main_frame, width=5, fg='black',font=('Arial',10))

                self.e.place(x=300, y=i*30 + 90)
                self.e.insert(END, str(self.theta[i]))

                self.e = Entry(self.main_frame, width=5, fg='black',font=('Arial',10))

                self.e.place(x=350, y=i*30 + 90)
                self.e.insert(END, str(self.d[i]))

                self.e = Entry(self.main_frame, width=5, fg='black',font=('Arial',10))

                self.e.place(x=400, y=i*30 + 90)
                self.e.insert(END, str(self.a[i]))

                self.e = Entry(self.main_frame, width=5, fg='black',font=('Arial',10))

                self.e.place(x=450, y=i*30 + 90)
                self.e.insert(END, str(self.alpha[i]))
        
        def plot_robot():
            config =[]
            for i in range(len(self.theta)):
                config.append([self.theta[i], self.d[i], self.a[i], self.alpha[i]])
            
            robot = Robot(config)
            fig = Figure(figsize = (3, 3), dpi = 100)

            robot_plotted = robot.show_robot(fig)
            canvas = FigureCanvasTkAgg(fig, master=self.main_frame)
            canvas.draw()
            canvas.get_tk_widget().place(x=300, y=250)
            toolbar = NavigationToolbar2Tk(canvas, self.main_frame)
            toolbar.update()
            canvas.get_tk_widget().place(x=300, y=250)

def run():
    root = App()
    root.mainloop()


if __name__ == '__main__':
    run()