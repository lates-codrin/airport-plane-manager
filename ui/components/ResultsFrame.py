import customtkinter as ctk
import os
from PIL import Image
from ui.components.Tooltip import CustomTooltipLabel

class SeatMap(ctk.CTkScrollableFrame):
    def __init__(self,mas,planes=None, rows=6, cols=10,*args, **kwargs):
        super().__init__(mas,*args, **kwargs)

        self.rows = rows
        self.cols = cols
        self.seats = []  # seat buttons
        self.current_seat_start = 1  # seat index
        self.seat_range = 20  # max seats per page
        self.mas = mas
        self.current_plane_index = 0
        self.__planes = planes
        print(self.__planes)
        
        #print(self.__planes)
        self.pack(pady=20, padx=20)
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        large_test_image = ctk.CTkImage(Image.open(os.path.join(image_path, "seatmap.png")), size=(600, 600))
        self.configure(width=1920, height=1080)

        label = ctk.CTkLabel(master=self, text="", image=large_test_image)
        label.grid(row=0, column=0, sticky="ns")


        self.button_frame = ctk.CTkFrame(self, fg_color="#f5f7fd", corner_radius=0, width=120, height=445)
        self.button_frame.grid_propagate(0)
        self.button_frame.grid(row=0, column=0, padx=15, pady=200, sticky="ns")  # Add sticky for proper alignment

        #self.button_frame.place(relwidth=0.099, relheight=0.8)  
        current_plane = self.get_curr_plane()
        passenger_list = current_plane.get_passengers_list()
        self.create_seat_map(passenger_list)
        
        self.next_seats_preview = ctk.CTkButton(
            self,
            width=40,
            text="->",
            compound="left",
            fg_color="transparent",
            border_width=2,
            text_color=("gray10", "#DCE4EE"),
            command=self.show_next_seat_page,
            font=ctk.CTkFont(size=25),
            height=40,
        )
        self.prev_seats_preview = ctk.CTkButton(
            self,
            width=40,
            text="<-",
            compound="left",
            fg_color="transparent",
            border_width=2,
            text_color=("gray10", "#DCE4EE"),
            command=self.show_prev_seat_page,
            font=ctk.CTkFont(size=25),
            height=40,
        )

        # Add navigation buttons under the seat map
        self.navigation_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.navigation_frame.grid(row=1, column=0, pady=10)  # Positioned directly below the seat map



        # Adjust grid configurations for proper alignment and scaling
        

        self.navigation_frame.columnconfigure(0, weight=1)
        self.navigation_frame.columnconfigure(1, weight=1)

        self.flight_info_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.flight_info_frame.grid(row=1, column=0, columnspan=2, pady=5, sticky="n")

        self.flight_info_destination_label = ctk.CTkLabel(
            master=self.flight_info_frame, text="Destination: ", font=ctk.CTkFont(size=20)
        )
        self.flight_info_destination_label.grid(row=0, column=0, padx=10, sticky="w")

        # Modify Exit and Next Plane buttons for proper alignment
        self.exit_preview_btn = ctk.CTkButton(self.master, width = 60, text="[X] Exit Preview", compound="left", fg_color="transparent", 
                                                               border_width=2, text_color=("gray10", "#DCE4EE"), command=self.exit_preview,
                                                               font=ctk.CTkFont(size=25)
                                                               )
        self.next_plane_btn = ctk.CTkButton(self.master, width = 60, text="Next Plane [->]", compound="left", fg_color="transparent", 
                                                               border_width=2, text_color=("gray10", "#DCE4EE"), command=self.show_next_plane,
                                                               font=ctk.CTkFont(size=25)
                                                               )
        self.exit_preview_btn.grid(
            row=1,
            column=0,
            sticky="nw",
            pady=10,
            padx=(20,10),
            in_=self,  # Attach to the main frame
        )
        self.next_plane_btn.grid(
            row=1,
            column=0,
            sticky="ne",
            pady=10,
            padx=(20,10),
            in_=self,  # Attach to the main frame
        )

        

        # end buttons
        
        # Flight name title (centered above the plane)
        self.flight_info_title_label = ctk.CTkLabel(
            master=self,
            text="APM | Flight no. 0",
            font=ctk.CTkFont(size=30, weight="bold"),
        )
        self.flight_info_title_label.grid(row=0, column=0, columnspan=2, pady=10, sticky="n")

        # Flight information (aligned below the title)
        

        self.flight_info_seats_label = ctk.CTkLabel(
            master=self.flight_info_frame, text="Seated: ", font=ctk.CTkFont(size=20)
        )
        self.flight_info_seats_label.grid(row=1, column=0, sticky="w", padx=10)

        self.flight_info_airline_label = ctk.CTkLabel(
            master=self.flight_info_frame, text="Airline: ", font=ctk.CTkFont(size=20)
        )
        self.flight_info_airline_label.grid(row=2, column=0, sticky="w", padx=10)

        self.flight_info_passengers_label = ctk.CTkLabel(
            master=self.flight_info_frame,
            text="Passengers: ",
            font=ctk.CTkFont(size=20),
            justify="left",
        )
        self.flight_info_passengers_label.grid(row=3, column=0, sticky="w", padx=10)

        # Adjust grid configurations for proper alignment
        self.grid_rowconfigure(0, weight=0)  # For the flight title
        self.grid_rowconfigure(1, weight=0)  # For flight info
        self.grid_rowconfigure(2, weight=1)  # For seat map and other content
        self.grid_columnconfigure(0, weight=1)  # Center content horizontally

        # Initialize with the first plane's data
        self.update_labels()
    def show_next_seat_page(self):
        """Show the next page of seats"""
        # Update the seat range to show the next page of seats
        self.current_seat_start += self.seat_range

        # Check if we've reached the end of the list, in which case we stop
        if self.current_seat_start > self.get_curr_plane().get_seats():
            print("You think passengers can board the plane somewhere else, maybe on the wing? No more seats to show!")
            self.current_seat_start=0
            return  # Or reset, wrap around, or show a message

        # Create the seat map for the new range of seats
        current_plane = self.get_curr_plane()
        passenger_list = current_plane.get_passengers_list()
        self.create_seat_map(passenger_list)
        
    def show_prev_seat_page(self):
        """Show the prev page of seats"""
        # Update the seat range to show the next page of seats
    
        self.current_seat_start -= self.seat_range

        # Check if we've reached the end of the list, in which case we stop
        if self.current_seat_start < 0:
            print("What are you, a time traveller! You cannot go back further more!")
            self.current_seat_start=0
            return  # Or reset, wrap around, or show a message

        # Create the seat map for the new range of seats
        current_plane = self.get_curr_plane()
        passenger_list = current_plane.get_passengers_list()
        self.create_seat_map(passenger_list)

    def create_seat_map(self, pass_list):
        # Clear the existing seats
        for seat_row in self.seats:
            for seat in seat_row:
                seat.grid_forget()
        
        # Reinitialize the list to store the new seats
        self.seats = []
        
        # Get the current plane
        current_plane = self.get_curr_plane()
        passenger_list = pass_list

        # Calculate the range of seat numbers to display
        end_seat = self.current_seat_start + self.seat_range - 1
        for row in range(self.get_curr_plane().get_seats()):
            row_seats = []
            for col in range(self.cols):
                seat_number = self.current_seat_start + (row * self.cols + col)
                if seat_number > end_seat:
                    break  # No more seats to show
                if seat_number > self.get_curr_plane().get_seats():
                    break
                
                passenger = passenger_list[seat_number - 1] if seat_number - 1 < len(passenger_list) else None

                # Create the button
                seat_button = ctk.CTkButton(
                    self.button_frame,
                    text=f"{seat_number}",
                    command=lambda num=seat_number, passport=(passenger.get_passport_number() if passenger else None): self.on_seat_click(num, passport),
                    width=40,
                    height=40
                )
                
                # Generate tooltip text based on passenger assignment
                if seat_number <= len(passenger_list):  # Check if a passenger is assigned
                    tooltip_text = (
                        f"Seat {seat_number}:\n"
                        f"Name: {passenger.get_first_name()} {passenger.get_last_name()}\n"
                        f"Passport: {passenger.get_passport_number()}"
                    )
                else:
                    tooltip_text = f"Seat {seat_number}: Unassigned"
                
                # Create a tooltip for the button
                CustomTooltipLabel(anchor_widget=seat_button, text=tooltip_text, hover_delay=100)
                
                # Place the button in the grid
                seat_button.grid(row=row, column=col, padx=10, pady=5)  # Add some padding
                row_seats.append(seat_button)
            self.seats.append(row_seats)

    def update_labels(self):
        # Get the current plane data
        current_plane = self.__planes[self.current_plane_index]

        # Update labels with plane data
        self.flight_info_title_label.configure(
            text=f"APM | Flight no. {current_plane.get_number()}"
        )
        self.flight_info_destination_label.configure(
            text=f"Destination: {current_plane.get_destination()}"
        )
        self.flight_info_seats_label.configure(
            text=f"Seated: {len(current_plane.get_passengers_list())} / {current_plane.get_seats()}"
        )
        self.flight_info_airline_label.configure(
            text=f"Airline: {current_plane.get_airline()}"
        )
        self.flight_info_passengers_label.configure(
    text="Passengers:\n" + "\n".join(
        [
            ", ".join([p.get_first_name() + " " + p.get_last_name() for p in current_plane.get_passengers_list()[i:i+9]])
            for i in range(0, min(len(current_plane.get_passengers_list()), 12), 9)
        ]
    ) + (" [...]" if len(current_plane.get_passengers_list()) > 12 else "")
)


    def show_next_plane(self):
        # Increment the plane index and wrap around if needed
        self.current_plane_index = (self.current_plane_index + 1) % len(self.__planes)
        self.update_labels()
        current_plane = self.get_curr_plane()
        passenger_list = current_plane.get_passengers_list()
        self.create_seat_map(passenger_list)
    

    def get_curr_plane(self):
        return self.__planes[self.current_plane_index]
    
    def on_seat_click(self, seat_number, passport):
        print(f"Seat {seat_number} clicked! Person with passport: ",passport,".")
        self.spawn_seat_editor(seat_number, passport)

    def exit_preview(self):
        self.mas.destroy()


    def spawn_seat_editor(self, seat_number, passport):
        # Despawn any existing seat editor
        if hasattr(self, "seat_editor_frame"):
            self.seat_editor_frame.destroy()

        # Create a new editor for the clicked seat
        self.seat_editor_frame = ctk.CTkFrame(
            self, corner_radius=0, fg_color="#3c3c3c"
        )
        self.seat_editor_frame.place(relx=0.7, rely=0.05, relheight=1, relwidth=0.3)

        # Textboxes for First Name, Last Name, and Passport Number
        self.first_name_textbox = ctk.CTkTextbox(
            master=self.seat_editor_frame, width=300, height=40, corner_radius=5
        )
        self.first_name_textbox.insert("0.0", "First Name")
        self.first_name_textbox.pack(pady=10, padx=20)

        self.last_name_textbox = ctk.CTkTextbox(
            master=self.seat_editor_frame, width=300, height=40, corner_radius=5
        )
        self.last_name_textbox.insert("0.0", "Last Name")
        self.last_name_textbox.pack(pady=10, padx=20)

        self.passport_textbox = ctk.CTkTextbox(
            master=self.seat_editor_frame, width=300, height=40, corner_radius=5
        )
        self.passport_textbox.insert("0.0", "Passport Number")
        self.passport_textbox.pack(pady=10, padx=20)

        # Buttons for Assigning Values
        self.first_name_btn = ctk.CTkButton(
            master=self.seat_editor_frame,
            text="Assign First Name",
            fg_color="transparent",
            border_width=2,
            text_color=("gray10", "#DCE4EE"),
            command=lambda: self.toggle_button(self.first_name_btn),
            font=ctk.CTkFont(size=20),
        )
        self.first_name_btn.pack(pady=10)

        self.last_name_btn = ctk.CTkButton(
            master=self.seat_editor_frame,
            text="Assign Last Name",
            fg_color="transparent",
            border_width=2,
            text_color=("gray10", "#DCE4EE"),
            command=lambda: self.toggle_button(self.last_name_btn),
            font=ctk.CTkFont(size=20),
        )
        self.last_name_btn.pack(pady=10)

        self.passport_btn = ctk.CTkButton(
            master=self.seat_editor_frame,
            text="Assign Passport Number",
            fg_color="transparent",
            border_width=2,
            text_color=("gray10", "#DCE4EE"),
            command=lambda: self.toggle_button(self.passport_btn),
            font=ctk.CTkFont(size=20),
        )
        self.passport_btn.pack(pady=10)

        # "Proceed with Config" Button
        self.proceed_btn = ctk.CTkButton(
            master=self.seat_editor_frame,
            text="Proceed with Config",
            fg_color="blue",
            text_color="white",
            command=lambda: self.proceed_with_config(passport),
            font=ctk.CTkFont(size=20),
        )
        self.proceed_btn.pack(pady=20)

        # Display current seat being edited
        seat_label = ctk.CTkLabel(
            master=self.seat_editor_frame,
            text=f"Editing Seat {seat_number}",
            font=ctk.CTkFont(size=18, weight="bold"),
        )
        seat_label.pack(pady=20)

    ### Helper Method to Toggle Button Colors
    def toggle_button(self, button):
        if button.cget("fg_color") == "transparent":
            button.configure(fg_color="green", text_color="white")  # Activate button
        else:
            button.configure(fg_color="transparent", text_color=("gray10", "#DCE4EE"))  # Deactivate button
    
    def proceed_with_config(self,passport):
        print("proceeding with ", passport)
        # Create a dictionary to hold the activated buttons and their associated text
        config_data = {}

        # Check if buttons are active and fetch text
        if self.first_name_btn.cget("fg_color") == "green":
            first_name = self.first_name_textbox.get("0.0", "end").strip()
            config_data["first name"] = first_name

        if self.last_name_btn.cget("fg_color") == "green":
            last_name = self.last_name_textbox.get("0.0", "end").strip()
            config_data["last name"] = last_name

        if self.passport_btn.cget("fg_color") == "green":
            passport_number = self.passport_textbox.get("0.0", "end").strip()
            config_data["passport number"] = passport_number

        # Print the resulting data and save it to instance variables
        self.saved_first_name = config_data.get("first name", "")
        self.saved_last_name = config_data.get("last name", "")
        self.saved_passport_number = config_data.get("passport number", "")
        print(config_data)
        
        # Example use of saved data (for further operations)
        print(f"Saved First Name: {self.saved_first_name}")
        print(f"Saved Last Name: {self.saved_last_name}")
        print(f"Saved Passport Number: {self.saved_passport_number}")

        print(self.__planes[self.current_plane_index])
        passport_number1 = passport.strip()
        passenger = self.__planes[self.current_plane_index].get_passenger_with_passport_number(passport_number1)
        passenger.set_first_name(self.saved_first_name)
        passenger.set_last_name(self.saved_last_name)
        passenger.set_passport_number(self.saved_passport_number)
        self.update_labels()
        current_plane = self.get_curr_plane()
        passenger_list = current_plane.get_passengers_list()
        self.create_seat_map(passenger_list)

class PlaneExplorer(ctk.CTkToplevel):
    def __init__(self, master,planes = None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        
        self.attributes('-fullscreen', True)
        self.planes=planes
        self.seat_map = SeatMap(self,planes=self.planes, rows=10, cols=2)
        self.title("Seat Map _PRODUCTION")
        self.lift()
        self.focus()
        


# Example usage
'''if __name__ == "__main__":
    app = ctk.CTk()
    app.title("Seat Map _PRODUCTION")
    app.attributes('-fullscreen', True)
    # Create a seat map inside the main window
    seat_map = SeatMap(app, app, rows=10, cols=2)

    app.mainloop()
'''