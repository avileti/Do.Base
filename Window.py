import tkinter as tk

LARGE_FONT= ("Verdana" , 12)


class SeaofBTCapp(tk.TK):

    def _init (self, *args, **kwargs):
        
        tk.Tk._init_(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        
        frame = StartPage(container, self)

        self.frames(StartPage) = frame

        frame.grid(row=0, column = 0, sticky="nsew")

        self.show_frame(StartPage)

      def show_frame(self, cont):

          frame = self.frames[cont]
          frame.tkraise()


class StartPage(tk.frame):

    def _init_(self, parent, controller):
        tk.Frame._init_(self,parent)
        label = tk.Label(self, text="Start_Page", font=LARGE FONT)
        label.pack(pady=10,padx=10)

app = SeaofBTCapp()
app.mainloop()
        
