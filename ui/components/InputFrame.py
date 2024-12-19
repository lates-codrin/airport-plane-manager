import subprocess
import ast
import tkinter
import customtkinter
import os
from PIL import Image


class InputFrame(customtkinter.CTkFrame):
    def __init__(self, master, plane_add_frame,controller, log_frame = None, **kwargs):
        super().__init__(master, **kwargs)
        self.plane_add_frame = plane_add_frame
        self.__controller = controller
        #
        self.log_frame = log_frame
        

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
        self.confirm_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "confirm.png")), size=(200, 200))
        self.cross_mark_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "cross-mark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "cross-mark.png")), size=(20, 20))


        ###
        
        #self.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.radio_var = tkinter.IntVar(value=0)
        #self.place(anchor="center",relx=0.5, rely=0.5)
        self.grid_rowconfigure(2, weight=1)
        self.grid(row=0, column=0, sticky="nsew")
        
        
        self.label_radio_group = customtkinter.CTkLabel(master=self, 
                                                        text="Would you like to read from file `plane_db.txt` or add manualy?:",
                                                        font=customtkinter.CTkFont(size=14, weight="bold"))
        self.label_radio_group.place(anchor="center", relx=0.6, rely=0.5)

        self.image_top = customtkinter.CTkLabel(master=self, 
                                                        text="",
                                                        image=self.confirm_image, compound="bottom")
        
        self.image_top.place(anchor="center", relx=0.2, rely=0.5)

        self.radio_button_1 = customtkinter.CTkRadioButton(master=self, variable=self.radio_var, value=0, text="Manually - From Menu",font=customtkinter.CTkFont(size=14, weight="bold"))
        self.radio_button_1.place(anchor="center", relx=0.4, rely=0.6)

        self.radio_button_2 = customtkinter.CTkRadioButton(master=self, variable=self.radio_var, value=1, text="From file `plane_db.txt`",
                                                           font=customtkinter.CTkFont(size=14, weight="bold"))
        self.radio_button_2.place(anchor="center", relx=0.8, rely=0.6)

        

        self.close_add_planes_button = customtkinter.CTkButton(self, width = 14, text="Cancel Operation", compound="left", fg_color="transparent", 
                                                               border_width=2, text_color=("gray10", "#DCE4EE"), command=self.grid_forget,
                                                               font=customtkinter.CTkFont(size=12),
                                                               image=self.cross_mark_image
                                                               )
        self.close_add_planes_button.place(anchor="center", relx=0.725, rely=0.9357) # did this by hand, was not fun
    
    def get_rad(self):
        return self.radio_var.get()
    def hide(self):
        self.grid_forget()
        self.plane_add_frame.grid_forget()
    @staticmethod
    def readPassengerData():
        """
        Reads passenger data from the specified file.
        Returns a dictionary where the keys are plane IDs and the values are lists of passenger tuples.
        """
        passenger_data = {}
        try:
            with open("infrastructure/database/passenger_db.txt", "r") as file:
                for line in file:
                    line = line.strip()
                    if line.endswith(":"):  # Plane ID line
                        plane_id = int(line.strip(":"))
                        passenger_data[plane_id] = []
                    elif line.startswith("("):  # Passenger data line
                        passenger = eval(line)  # Safely parse the tuple
                        passenger_data[plane_id].append(passenger)
            return passenger_data
        except IOError as err:
            print(str(err))
            return None
        except Exception as e:
            print(str(e))
            return None

    @staticmethod
    def readPlaneData(passenger_data):
        """
        Reads plane data from the specified file and associates it with passenger data.
        Returns a list of planes with their associated passengers.
        """
        planes = []
        try:
            with open("infrastructure/database/plane_db.txt", "r") as file:
                for line in file:
                    line = line.strip()
                    if line.startswith("("):
                        plane_tuple = eval(line)  # yes
                        plane_id = plane_tuple[0]
                        passengers = passenger_data.get(plane_id, [])
                        planes.append({
                            "plane_id": plane_id,
                            "plane_name": plane_tuple[1],
                            "capacity": plane_tuple[2],
                            "destination": plane_tuple[3],
                            "passengers": passengers
                        })
            return planes
        except IOError as err:
            print(str(err))
        except Exception as e:
            print(str(e))
        
    def readPlaneInput(self):
        """
        Reads input for plane and passenger data processing.
        """
        
        # Read passenger data
        print("Reading passenger data...")
        passenger_data = self.readPassengerData()
        if not passenger_data:
            print("Failed to read passenger data. Exiting.")
            return

        # Read plane data
        print("Reading plane data...")
        planes = self.readPlaneData(passenger_data)
        if planes:
            print("Plane and passenger data successfully read.")
        else:
            print("Failed to read plane data.")
        
        return planes

