
import customtkinter

from ui.components.NavigationFrame import NavigationFrame
from ui.components.PlaneAddFrame import PlaneAddFrame
from ui.components.HomeFrame import HomeFrame
from ui.components.InitImages import InitImages
from ui.components.UpdateFrame import UpdateFrame

#from utils.Logger import Logger


# vineri 10 ian next psy course
# 17 ian examen
class PlaneUI(customtkinter.CTk):
    def __init__(self, controller = None):
        super().__init__()
        self.__controller = controller

        self.title("APM - Airport Plane Manager v1.0.1")
        self.geometry("1200x550")
        self.resizable(False, False)
        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.iconbitmap(r'ui\components\test_images\airport.ico')
        self.images = InitImages()

        self.__create_widgets()
        
        
    
    def __create_widgets(self):
        self.home_frame = HomeFrame(master=self, controller=self.__controller)
        self.plane_add_frame = PlaneAddFrame(master=self, controller=self.__controller)
        
        self.update_frame = UpdateFrame(master=self,
                                        controller=self.__controller
                                        )
        self.navigation_frame = NavigationFrame(master=self, 
                                                home_frame=self.home_frame, 
                                                plane_add_frame=self.plane_add_frame, 
                                                controller=self.__controller,
                                                images=self.images,
                                                update_frame=self.update_frame
                                                )
        #self.update_frame.show()


'''if __name__ == "__main__":
    app = App()
    app.mainloop()'''
