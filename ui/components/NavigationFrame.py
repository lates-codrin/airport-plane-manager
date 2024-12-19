import customtkinter
from ui.components.InputFrame import InputFrame
from ui.components.SortComponent import SortWindow
from ui.components.LogFrame import LogWindow
from ui.components.CombineFrame import CombineFrame

class NavigationFrame(customtkinter.CTkFrame):

    def __init__(self, master, home_frame, plane_add_frame,controller,images, update_frame, **kwargs):
        super().__init__(master, **kwargs)
        self.home_frame = home_frame
        self.plane_add_frame = plane_add_frame
        self.__controller = controller
        self.__images = images
        self.update_frame = update_frame
        self.log_window = None

        self.prompt = InputFrame(master=self.master, plane_add_frame=self.plane_add_frame, controller=self.__controller, log_frame = self.log_window)
        self.sort_window = None
        self.prompt.grid_forget()
        # 

        #


        #self = customtkinter.CTkFrame(self, corner_radius=0, fg_color="#1c1c1d")
        self.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(11, weight=1)

        self.__create_widgets()
    
    def __create_widgets(self):

        self.navigation_frame_label = customtkinter.CTkLabel(self, text="  Airport Plane Manager", 
                                                             image=self.__images.get_logo_image(),
                                                            compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.separator_frame = customtkinter.CTkFrame(self, corner_radius=0, 
                                                      fg_color="#3c3c3c",width=200, height=3)
        self.separator_frame.grid(row=0, column=0, sticky="ew", pady=(100, 0))

        self.home_button = customtkinter.CTkButton(self, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                image=self.__images.get_home_image(), anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self, corner_radius=0, height=45, border_spacing=10, text="Add Plane(s)",
                                                    fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                    image=self.__images.get_add_plane_image(), anchor="w", command=self.open_input_dialog_event)
        self.frame_2_button.grid(row=3, column=0, sticky="ew")

        self.separator_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="#3c3c3c",width=200, height=3)
        self.separator_frame.grid(row=4, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self, corner_radius=0, height=40, border_spacing=10, text="Update Plane(s)",
                                                    fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                    image=self.__images.get_plane_settings_image(), anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=2, column=0, sticky="ew")

        self.frame_4_button = customtkinter.CTkButton(self, corner_radius=0, height=40, border_spacing=10, text="Delete Plane(s)",
                                                    fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                    image=self.__images.get_plane_delete_image(), anchor="w", command=self.frame_4_button_event)
        self.frame_4_button.grid(row=5, column=0, sticky="ew")

        self.frame_5_button = customtkinter.CTkButton(self, corner_radius=0, height=40, border_spacing=10, text="Sort Plane(s)",
                                                    fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                    image=self.__images.get_plane_sort_image(), anchor="w", command=self.frame_5_button_event)
        self.frame_5_button.grid(row=6, column=0, sticky="ew")

        self.combine_frames_button = customtkinter.CTkButton(self, corner_radius=0, height=40, border_spacing=10, text="Combine Plane(s)",
                                                    fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                    image=self.__images.get_plane_combine_image(), anchor="w", command=self.combine_frames_button_event)
        self.combine_frames_button.grid(row=7, column=0, sticky="ew")

        self.logs_button = customtkinter.CTkButton(self, corner_radius=0, height=40, border_spacing=10, text="Open Logs",
                                                    fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                    image=self.__images.get_log_image(), anchor="w", command=self.log_button_event)
        self.logs_button.grid(row=8, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event,fg_color=("#18a3ff", "#18a3ff"), button_color=("#18a3ff", "#18a3ff"), button_hover_color=("#18a3ff","#18a3ff"))
        self.appearance_mode_menu.grid(row=9, column=0, padx=20, pady=20, sticky="s")
        self.select_frame_by_name("home")
    
    
    def open_input_dialog_event(self):
        self.prompt.grid(row=0, column=1, sticky="nsew")

        self.view_planes_button = customtkinter.CTkButton(self.prompt, text="Proceed", 
                                                          image=self.__images.get_image_icon_image(), 
                                                          compound="left", 
                                                          fg_color="transparent", 
                                                          border_width=2, 
                                                          text_color=("gray10", "#DCE4EE"), 
                                                          command=self.open_add_plane_frame_event,
                                                          font=customtkinter.CTkFont(size=12))
        self.view_planes_button.place(anchor="center", relx=0.9, rely=0.9357)
        self.prompt.update()
        
        
    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)
    ####

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")
        self.frame_4_button.configure(fg_color=("gray75", "gray25") if name == "frame_4" else "transparent")
        self.frame_5_button.configure(fg_color=("gray75", "gray25") if name == "frame_5" else "transparent")
        self.combine_frames_button.configure(fg_color=("gray75", "gray25") if name == "frame_6" else "transparent")
        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
            self.home_frame.update_label_text()
        else:
            self.home_frame.grid_forget()

        if name == "frame_3":
            self.update_frame.grid(row=0, column=1, sticky="nsew")
            self.home_frame.update_label_text()
        else:
            self.update_frame.grid_forget()
        
        if name == "update_frame":
            self.plane_add_frame.grid(row=0, column=1, sticky="nsew")
            self.home_frame.update_label_text()
        else:
            self.plane_add_frame.grid_forget()


    def open_add_plane_frame_event(self):
        if self.prompt.get_rad() == 1:
            planes = self.prompt.readPlaneInput()
            self.__controller.addPlane(planes)
            self.select_frame_by_name("home")
            self.prompt.grid_forget()
        else:
            self.select_frame_by_name("update_frame")
            self.prompt.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")


    def frame_4_button_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in the ID of the plane you want to delete:", title="APM - Lates Codrin Gabriel")
        
        inp = dialog.get_input()
        if inp == "all":
            success = self.__controller.deletePlane((inp, []))
        elif inp != None:
            success = self.__controller.deletePlane(("index",int(inp)))
        else:
            print("Cancelled delete action.")

    def frame_5_button_event(self):
        if self.sort_window is None or not self.sort_window.winfo_exists():
            self.sort_window = SortWindow(self, self.__controller, self.log_window)
            self.sort_window.after(10, self.sort_window.lift)
        else:
            self.sort_window.after(20, self.sort_window.focus)

    def combine_frames_button_event(self):
        ok = CombineFrame(master=self, controller=self.__controller)

    def frame_7_button_event(self):
        print("placeholder")

    def log_button_event(self):
        labels = []
        with open("utils/log.txt", "r+") as file:
            for line in file:
                labels.append(line)
            file.close()
        if self.log_window is None or not self.log_window.winfo_exists():
            self.log_window = LogWindow(master=self.master, controller=self.__controller, logs=labels)
        else:
            # Update logs if the window already exists
            self.log_window.set_logs(labels)
        
        # Show the window
        self.log_window.show()

