import customtkinter
import tkinter

class SortWindow(customtkinter.CTkToplevel):
    def __init__(self, master, controller,log_window, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.geometry("800x300")
        self.__controller = controller
        self.log_window = log_window
        self.cr()

    def cr(self):
        self.label = customtkinter.CTkLabel(self, text="APM - Sort Planes", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.label.place(anchor="center", relx=0.5, rely=0.2)

        self.radio_var = tkinter.IntVar(value=2)

        self.radio_button_1 = customtkinter.CTkRadioButton(master=self, variable=self.radio_var, value=0, text="By number of passengers abroad.", 
                                                           command=self.rad_b_1)
        self.radio_button_1.place(anchor="center", relx=0.3, rely=0.4)

        self.radio_button_2 = customtkinter.CTkRadioButton(master=self, variable=self.radio_var, value=1, text="By number of passengers with first name.",
                                                           command=self.cr_2)
        self.radio_button_2.place(anchor="center", relx=0.7, rely=0.4)

        self.radio_button_3 = customtkinter.CTkRadioButton(master=self, variable=self.radio_var, value=2, text="By concatenation of number of passengers and destination.",
                                                           command=self.rad_b_3)
        self.radio_button_3.place(anchor="center", relx=0.45, rely=0.6)

        self.configure(fg_color="#1c1c1d")
        self.after(10, self.lift)

    def show_confirm_frame(self, confirm_action, cancel_action):
        self.confirm_frame = customtkinter.CTkFrame(self)
        self.confirm_frame.place(relx=0.5, rely=0.5, anchor="center")

        label = customtkinter.CTkLabel(master=self.confirm_frame, text="Would you like to proceed?", font=customtkinter.CTkFont(size=20, weight="bold"))
        label.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 10))

        confirm_button = customtkinter.CTkButton(master=self.confirm_frame, text="Confirm", font=customtkinter.CTkFont(size=15, weight="bold"), 
                                                 command=lambda: [confirm_action(), self.confirm_frame.destroy()])
        confirm_button.grid(row=1, column=0, padx=20, pady=20, sticky="nswe")

        cancel_button = customtkinter.CTkButton(master=self.confirm_frame, text="Cancel", font=customtkinter.CTkFont(size=15, weight="bold"), 
                                                command=lambda: [cancel_action(), self.confirm_frame.destroy()])
        cancel_button.grid(row=1, column=1, padx=20, pady=20, sticky="nswe")

    def cr_2(self):
        dialog = customtkinter.CTkInputDialog(text="Type in first name:", title="APM - Lates Codrin Gabriel")
        fr = dialog.get_input()
        
        def confirm_action():
            self.__controller.updatePlane(("sort", 2, str(fr)))

        def cancel_action():
            print("Action canceled")

        self.show_confirm_frame(confirm_action, cancel_action)

    def rad_b_1(self):
        def confirm_action():
            self.__controller.updatePlane(("sort", 1, []))

        def cancel_action():
            print("Action canceled")

        self.show_confirm_frame(confirm_action, cancel_action)

    def rad_b_3(self):
        def confirm_action():
            self.__controller.updatePlane(("sort", 3, []))

        def cancel_action():
            print("Action canceled")

        self.show_confirm_frame(confirm_action, cancel_action)
