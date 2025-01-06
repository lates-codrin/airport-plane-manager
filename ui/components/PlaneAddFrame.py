import customtkinter
from PIL import Image
import os
class PlaneAddFrame(customtkinter.CTkFrame):

    def __init__(self, master, controller, **kwargs):
        super().__init__(master, **kwargs)
        #7th
        #self.seventh_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="#161617")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        # header
        self.plane_count = 0
        self.__controller = controller

        ###

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "airport.png")), size=(80, 80))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "hangar.png")), size=(200, 200))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "binoculars.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "plane_lookup.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "plane_lookup.png")), size=(30, 30))
        self.add_plane_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "plane_add.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "plane_add.png")), size=(30, 30))
        self.plane_settings_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "plane_settings.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "plane_settings.png")), size=(30, 30))
        self.plane_delete = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "plane_delete.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "plane_delete.png")), size=(30, 30))
        self.plane_sort = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "plane_sort.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "plane_sort.png")), size=(30, 30))
        self.plane_combine = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "plane_combine.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "plane_combine.png")), size=(30, 30))
        self.large_plane_garages = customtkinter.CTkImage(Image.open(os.path.join(image_path, "hangar.png")), size=(200, 200))

        ###


        self.__create_widgets()
    
    def __create_widgets(self):
        self.navigation_frame_label1 = customtkinter.CTkLabel(
            self, 
            text=f"  Airport - {self.plane_count} Planes", 
            image=self.large_plane_garages,
            compound="top", 
            font=customtkinter.CTkFont(size=15, weight="bold")
        )
        self.navigation_frame_label1.place(anchor="center", relx=0.5, rely=0.25)
        self.textbox = customtkinter.CTkTextbox(master=self, width=400, corner_radius=0)
        self.textbox.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
        self.textbox.insert("0.0", """0:
("Bart", "Simpson", "219392389329822")
("Homer", "Simpson", "2193900281329822")
("Marge", "Angellica-Simpson", "219222389302822")

1:
("Romeo", "Bartholomeu", "110392389329822")
("Andrew", "McCullin", "1103900281329822")
("AaMichael", "Drewson", "110222389302822")
("Aaylin", "Simpson", "111222389302822")""")

        self.main_button_1 = customtkinter.CTkButton(
            master=self,
            text="Assign Passenger(s)", 
            fg_color="transparent", 
            border_width=2, 
            text_color=("gray10", "#DCE4EE"),
            width=400,
            command=self.assign_passengers
        )
        self.main_button_1.grid(row=2, column=0, padx=(10, 20), pady=(0, 10), sticky="ew")

        self.textbox2 = customtkinter.CTkTextbox(master=self, width=400, corner_radius=0)
        self.textbox2.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)
        self.textbox2.insert("0.0", """(0,"Delta Airlines", 84, "Australia")
(1,"Spirit Airlines", 84, "United Kingdom")""")

        self.main_button_2 = customtkinter.CTkButton(
            master=self,
            text="Assign Planes(s)", 
            fg_color="transparent", 
            border_width=2, 
            text_color=("gray10", "#DCE4EE"),
            width=400,
            command=self.assign_planes
        )
        self.main_button_2.grid(row=2, column=1, padx=(10, 20), pady=(0, 10), sticky="ew")

    def assign_passengers(self):
        if self.main_button_1.cget("fg_color") == ('#00A36C', '#00A36C'):
             self.main_button_1.configure(fg_color="transparent", hover_color="#7393B3")
             self.main_button_1.update()
        else: 
            self.main_button_1.configure(fg_color=("#00A36C","#00A36C"), hover_color=("#00A36C","#00A36C"))

        if self.main_button_2.cget("fg_color") == ("#00A36C","#00A36C"):
            print("both down!", self.main_button_1.cget("fg_color"))
            ###
            
            self.grid(row=0, column=1, sticky="nsew")
            self.confirm_frame = customtkinter.CTkFrame(self, fg_color="#3c3c3c", width=600, height = 600)
            self.confirm_frame.place(anchor="center", relx=0.5, rely=0.7)
            self.main_button_1.configure(state="disabled")
            self.main_button_2.configure(state="disabled")
            self.label = customtkinter.CTkLabel(master=self.confirm_frame,text="Would you like to proceed with the \ninserted information?",font=customtkinter.CTkFont(size=20, weight="bold"))

        
            self.label.grid(row=0, column=1, padx=20,pady=(20,20))
            self.confirm_button = customtkinter.CTkButton(master=self.confirm_frame, font=customtkinter.CTkFont(size=15, weight="bold"),text="Confirm", compound="left", 
                                                          fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), command=self.confirm_add)
            self.confirm_button.grid(row=1, column=0, padx=(20,20), pady=20,sticky = "nswe")
                
            self.cancel_button = customtkinter.CTkButton(master=self.confirm_frame,font=customtkinter.CTkFont(size=15, weight="bold"), text="Cancel", compound="left", 
                                                         fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), command=self.cancel_add)
            self.cancel_button.grid(row=1, column=4, padx=(20,20), pady=20, sticky = "nswe")

            ###


    def confirm_add(self):
        self.main_button_1.configure(state="normal")
        self.main_button_2.configure(state="normal")
        print("You confirmed add.")
        passenger_data = {}
        passengers_textbox = self.textbox.get(0.0,customtkinter.END)
        for line in passengers_textbox.splitlines():
            line = line.strip()
            if line.endswith(":"):
                plane_id = int(line.strip(":"))
                passenger_data[plane_id] = []
            elif line.startswith("("):
                passenger = eval(line)
                passenger_data[plane_id].append(passenger)
            
        planes = []
        planes_textbox = self.textbox2.get(0.0,customtkinter.END)
        for line in planes_textbox.splitlines():
            line = line.strip()
            if line.startswith("("):
                plane_tuple = eval(line)  # yes
                plane_id = plane_tuple[0]
                passengers = passenger_data.get(plane_id, [])
                self.plane_count += 1
                planes.append({
                    "plane_id": plane_id,
                    "plane_name": plane_tuple[1],
                    "capacity": plane_tuple[2],
                    "destination": plane_tuple[3],
                    "passengers": passengers
                })
        self.__controller.addPlane(planes)
        self.navigation_frame_label1.configure(text=f"  Airport - {self.plane_count} Planes")
        self.confirm_frame.destroy()
        self.main_button_2.configure(fg_color="transparent", hover_color="#7393B3")
        self.main_button_1.configure(fg_color="transparent", hover_color="#7393B3")
    def cancel_add(self):
        self.main_button_1.configure(state="normal")
        self.main_button_2.configure(state="normal")
        print("cancel")
        self.confirm_frame.destroy()
        self.main_button_2.configure(fg_color="transparent", hover_color="#7393B3")
        self.main_button_1.configure(fg_color="transparent", hover_color="#7393B3")
    def assign_planes(self):
        if self.main_button_2.cget("fg_color") == ("#00A36C","#00A36C"):
             self.main_button_2.configure(fg_color="transparent", hover_color="#7393B3")
        else: self.main_button_2.configure(fg_color=("#00A36C","#00A36C"),hover_color=("#00A36C","#00A36C"))
        if self.main_button_1.cget("fg_color") == ("#00A36C","#00A36C"):
            ###
            
            self.grid(row=0, column=1, sticky="nsew")
            self.confirm_frame = customtkinter.CTkFrame(self, fg_color="#3c3c3c", width=600, height = 600)
            self.confirm_frame.grid(row=1,column=0,padx=(100,100), pady=(100,100))

            self.label = customtkinter.CTkLabel(master=self.confirm_frame,text="Would you like to proceed with the \ninserted information?",font=customtkinter.CTkFont(size=20, weight="bold"))

        
            self.label.grid(row=0, column=1, padx=20,pady=(20,20))
            self.confirm_button = customtkinter.CTkButton(master=self.confirm_frame, font=customtkinter.CTkFont(size=15, weight="bold"),text="Confirm", compound="left", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), command=self.confirm_add)
            self.confirm_button.grid(row=1, column=0, padx=(20,20), pady=20,sticky = "nswe")
                
            self.cancel_button = customtkinter.CTkButton(master=self.confirm_frame,font=customtkinter.CTkFont(size=15, weight="bold"), text="Cancel", compound="left", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), command=self.cancel_add)
            self.cancel_button.grid(row=1, column=4, padx=(20,20), pady=20, sticky = "nswe")
            self.update()

            ###