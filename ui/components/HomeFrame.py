import customtkinter
import os
from PIL import Image
from ui.components.ResultsFrame import PlaneExplorer
from ui.components.ErrorFrame import ErrorFrame

class HomeFrame(customtkinter.CTkFrame):

    def __init__(self, master, controller, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(4, weight=1)
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "hangar.png")), size=(200, 200))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "binoculars.png")), size=(20, 20))
        self.__controller = controller
        self.__create_widgets()
        
    def __create_widgets(self):
        self.navigation_frame_label1 = customtkinter.CTkLabel(self, text=f"  Airport - {self.__controller.getPlanes(("count",[]))} Planes", image=self.large_test_image,
                                                             compound="top", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.navigation_frame_label1.grid(row=0, column=1, padx=20, pady=20)
        
        self.view_planes_button = customtkinter.CTkButton(self, command=self.view_all_planes,text="View All Planes", image=self.image_icon_image, compound="left", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.view_planes_button.grid(row=1, column=0, padx=20, pady=20)

   # Get planes that have passengers with passport numbers starting with the same 3 letters.
        self.btn_view_planes_by_passport_prefix = customtkinter.CTkButton(
            self, text="View All Planes", image=self.image_icon_image, compound="left", 
            fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), 
            command=self.view_all_planes_with_passport_number
        )
        self.btn_view_planes_by_passport_prefix.grid(row=2, column=0, padx=20, pady=20)

        # Label for "Get planes that have passengers with passport numbers starting with the same 3 letters."
        self.lbl_planes_by_passport_prefix = customtkinter.CTkLabel(
            self, text="  Get planes that have passengers with passport numbers\n starting with the same 3 letters.",
            compound="left", font=customtkinter.CTkFont(size=15, weight="bold")
        )
        self.lbl_planes_by_passport_prefix.grid(row=2, column=1, padx=20, pady=20)

        ###################################

        # Get planes with passenger name
        self.btn_view_planes_by_name = customtkinter.CTkButton(
            self, command=self.view_all_planes_with_name_click_event, text="View All Planes", 
            image=self.image_icon_image, compound="left", fg_color="transparent", 
            border_width=2, text_color=("gray10", "#DCE4EE")
        )
        self.btn_view_planes_by_name.grid(row=4, column=0, padx=20, pady=20)

        self.lbl_planes_by_name = customtkinter.CTkLabel(
            self, text="  Get passengers from a given plane for which the first\n name or last name contain a string given as parameter.",
            compound="left", font=customtkinter.CTkFont(size=15, weight="bold")
        )
        self.lbl_planes_by_name.grid(row=3, column=1, padx=20, pady=20)

        ###################################

        # Get passengers by blah blah
        self.btn_view_planes_with_passenger_name = customtkinter.CTkButton(
            self, command=self.view_all_with_name_click_event, text="View Passengers", 
            image=self.image_icon_image, compound="left", fg_color="transparent", 
            border_width=2, text_color=("gray10", "#DCE4EE")
        )
        self.btn_view_planes_with_passenger_name.grid(row=3, column=0, padx=20, pady=20)

        self.lbl_planes_with_passenger_name = customtkinter.CTkLabel(
            self, text="  Get plane/planes where there is a passenger with a given name.",
            compound="left", font=customtkinter.CTkFont(size=15, weight="bold")
        )
        self.lbl_planes_with_passenger_name.grid(row=4, column=1, padx=20, pady=20)

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Enter plane id (index), e.g '0'")
        self.entry.grid(row=1, column=1, columnspan=2, padx=(20, 20), pady=(20, 20), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(master=self,text="Find Plane(s)", 
                                                     fg_color="transparent",
                                                       border_width=2, 
                                                       text_color=("gray10", "#DCE4EE"),
                                                       command=self.submit_entry
                                                       )
        self.main_button_1.grid(row=1, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")
    
    def submit_entry(self):
        '''print(self.__controller.getPlanes(("index",int(self.entry.get())
                                           )
                                          )
              )'''
        try:
            ok = self.entry.get()
            pr = int(ok)
            lst = []
            lst.append(self.__controller.getPlanes(("index", pr)))
            self.plane_explorer = PlaneExplorer(self,planes = lst)
            self.plane_explorer.after(10, self.plane_explorer.lift)
            self.plane_explorer.after(20, self.plane_explorer.focus)
        except Exception as err:
            err = ErrorFrame(master=self, err=err)
            print("Error")
    def view_all_with_name_click_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a name or part of a name:", title="APM - Airport Plane Manager")
        st =  dialog.get_input()
        if st:
            print(self.__controller.getPlanes((2,st)))


    def view_all_planes_with_name_click_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a name:", title="APM - Airport Plane Manager")
        st =  dialog.get_input()

        if st:
            print(self.__controller.getPlanes((3,st)))
            planes = self.__controller.getPlanes((3,st))
            
            self.plane_explorer = PlaneExplorer(self,planes = planes)
            self.plane_explorer.after(10, self.plane_explorer.lift)
            self.plane_explorer.after(20, self.plane_explorer.focus)
    
    
    def view_all_planes_with_passport_number(self):
        try:
            print(self.__controller.getPlanes((1,None)))
            planes = self.__controller.getPlanes((1,None))
            self.plane_explorer = PlaneExplorer(self,planes = planes)
            self.plane_explorer.after(10, self.plane_explorer.lift)
            self.plane_explorer.after(20, self.plane_explorer.focus)
        except Exception as err:
            err = ErrorFrame(master=self, err=err)
            err.after(10, err.lift)
            err.after(20, err.focus)
            print("Error")

        
    
    def view_all_planes(self):
        planes = self.__controller.getPlanes(("all", []))
        if len(planes) == 0 :
            err = ErrorFrame(master=self, err="No planes inside repository.")
            err.after(10, err.lift)
            err.after(20, err.focus)
            print("Error")
        else:
            self.plane_explorer = PlaneExplorer(self,planes)
            self.plane_explorer.after(10, self.plane_explorer.lift)
            self.plane_explorer.after(20, self.plane_explorer.focus)
        #hoice = self.__controller.getPlanes(("all", ""))
        #print(choice)

    def update_label_text(self):
        self.navigation_frame_label1.configure(text=f"  Airport - {self.__controller.getPlanes(("count",[]))} Planes")
        self.navigation_frame_label1.update()