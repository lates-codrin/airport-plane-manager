from PIL import Image
import customtkinter
import os

class InitImages():
    def __init__(self):
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

        self.log_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "file-edit.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "file-edit.png")), size=(30, 30))
    def get_logo_image(self):
        return self.logo_image
    
    def get_log_image(self):
        return self.log_image
    
    def get_large_test_image(self):
        return self.large_test_image

    def get_image_icon_image(self):
        return self.image_icon_image

    def get_home_image(self):
        return self.home_image

    def get_add_plane_image(self):
        return self.add_plane_image

    def get_plane_settings_image(self):
        return self.plane_settings_image

    def get_plane_delete_image(self):
        return self.plane_delete

    def get_plane_sort_image(self):
        return self.plane_sort

    def get_plane_combine_image(self):
        return self.plane_combine

    def get_large_plane_garages_image(self):
        return self.large_plane_garages