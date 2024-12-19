import customtkinter

class ErrorFrame(customtkinter.CTkToplevel):
    def __init__(self, master, err, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.geometry("800x300")
        self.err = err
        self.show_confirm_frame()

    def show_confirm_frame(self):
        self.confirm_frame = customtkinter.CTkFrame(self)
        self.confirm_frame.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor="center")

        label = customtkinter.CTkLabel(
            master=self.confirm_frame, 
            text=f"[⚡] Error encountered:\n {self.err}", 
            font=customtkinter.CTkFont(size=20, weight="bold")
        )
        label.pack(pady=(100,0))

        # Centering the button
        confirm_button = customtkinter.CTkButton(
            master=self.confirm_frame, 
            text="Confirm", 
            font=customtkinter.CTkFont(size=15, weight="bold"), 
            command=lambda: self.destroy()
        )
        confirm_button.pack(pady=(10,20))
