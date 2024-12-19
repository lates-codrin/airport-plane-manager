import customtkinter
import os

    
class LogWindow(customtkinter.CTkToplevel):
    def __init__(self,master,controller,logs, *args, **kwargs):
        super().__init__(master,*args, **kwargs)
        self.geometry("800x300")
        self.__controller = controller
        self.logs = logs
        self.frame = None
        self.cr()

    def cr(self):
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1) 
        self.grid_columnconfigure(0, weight=1)

        # Title Frame
        self.title_frame = customtkinter.CTkFrame(
            master=self,
            corner_radius=0,
            width=400,
            height=50,
            fg_color="#1c1c1d"
        )
        
        
        self.title_frame.pack(fill="y")
        
        self.clear_logs_btn = customtkinter.CTkButton(
            master=self.title_frame,
            font=customtkinter.CTkFont(size=10, weight="bold"),
            text="Clear Logs",
            compound="left",
            fg_color="transparent",
            border_width=2,
            text_color=("gray10", "#DCE4EE"),
            command=self.clr_logs
        )
        self.clear_logs_btn.place(relx=0.2, rely=0.7, anchor="center")

        self.update_logs_btn = customtkinter.CTkButton(
            master=self.title_frame,
            font=customtkinter.CTkFont(size=10, weight="bold"),
            text="Update Logs",
            compound="left",
            fg_color="transparent",
            border_width=2,
            text_color=("gray10", "#DCE4EE"),
            command=self.actual_upd_logs
        )
        self.update_logs_btn.place(relx=0.7, rely=0.7, anchor="center")


        self.frame = customtkinter.CTkScrollableFrame(
            master=self,
            fg_color="#1c1c1d",
            corner_radius=0
        )
        self.frame.configure(width=300, height=200)
        self.frame.pack(fill="both")

        # Populate Logs
        self.upd_logs()

        # Configure main window
        self.configure(fg_color="#1c1c1d")
        self.after(10, self.lift)

    def set_logs(self, new_logs):
        self.logs = new_logs

    def upd_logs(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        for log in self.logs:
            label = customtkinter.CTkLabel(
                self.frame,
                text=log,
                fg_color="transparent",
                anchor="w",
                font=customtkinter.CTkFont(size=15),
                pady=0,
                height=0
            )
            label.pack(fill="x", padx=10, pady=5)

    def hide(self):
        self.withdraw()

    def show(self):
        self.deiconify()

    def clr_logs(self):
        self.logs = []
        self.upd_logs()
        self.update()
        with open("utils/log.txt", "w") as f:
            f.flush()
            f.close()
        #f.flush()

            
        

    def actual_upd_logs(self):
        labels = []
        with open("utils/log.txt", "r+") as file:
            for line in file:
                labels.append(line)
            file.close()
        
        self.set_logs(labels)
        self.upd_logs()
    
    def new_log(self, text, parent):
        
        label = customtkinter.CTkLabel(
                parent,
                text="[LOG]: " + text,
                fg_color="transparent",
                anchor="w",
                font=customtkinter.CTkFont(size=15),
                pady=0,
                height=0
            )
        label.pack(fill="x", padx=10, pady=5)
    
    