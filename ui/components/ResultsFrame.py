import customtkinter as ctk
import os
from PIL import Image
from ui.components.Tooltip import CustomTooltipLabel

class SeatMap(ctk.CTkScrollableFrame):
    def __init__(self,mas,planes=None, rows=6, cols=10,*args, **kwargs):
        super().__init__(mas,*args, **kwargs)

        self.rows = rows
        self.cols = cols
        self.seats = []  # Store references to seat buttons
        self.current_seat_start = 1  # Initial seat range starting at seat 1
        self.seat_range = 20  # Number of seats to show per "page" (20 seats per page)
        self.mas = mas
        self.current_plane_index = 0
        self.__planes = planes
        print(self.__planes)
        
        #print(self.__planes)
        self.pack(pady=20, padx=20)
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        large_test_image = ctk.CTkImage(Image.open(os.path.join(image_path, "seatmap.png")), size=(900, 900))
        self.configure(width=1920, height=1080)

        label = ctk.CTkLabel(master=self, text="", image=large_test_image)
        label.grid(row=0, column=0)


        self.button_frame = ctk.CTkFrame(self, fg_color="#f5f7fd", corner_radius=0, width=150)  
        self.button_frame.grid_propagate(0)
        self.button_frame.grid(row=0,ipadx=20, ipady=5)
        #self.button_frame.place(relwidth=0.099, relheight=0.8)  
        current_plane = self.get_curr_plane()
        passenger_list = current_plane.get_passengers_list()
        self.create_seat_map(passenger_list)
        
        self.next_seats_preview = ctk.CTkButton(self.master, width = 60, text="->", compound="left", fg_color="transparent", 
                                                               border_width=2, text_color=("gray10", "#DCE4EE"), command=self.show_next_seat_page,
                                                               font=ctk.CTkFont(size=25)
                                                               )
        self.next_seats_preview.place(relx=0.255,rely=0.80)

        self.prev_seats_preview = ctk.CTkButton(self.master, width = 60, text="<-", compound="left", fg_color="transparent", 
                                                               border_width=2, text_color=("gray10", "#DCE4EE"), command=self.show_prev_seat_page,
                                                               font=ctk.CTkFont(size=25)
                                                               )
        self.prev_seats_preview.place(relx=0.20,rely=0.80)
        
        # we do le buttons muahahaha
        self.exit_preview_btn = ctk.CTkButton(self.master, width = 60, text="Exit Preview", compound="left", fg_color="transparent", 
                                                               border_width=2, text_color=("gray10", "#DCE4EE"), command=self.exit_preview,
                                                               font=ctk.CTkFont(size=25)
                                                               )
        self.exit_preview_btn.place(relx=0.80,rely=0.95)

        self.next_plane_btn = ctk.CTkButton(self.master, width = 60, text="Next Plane", compound="left", fg_color="transparent", 
                                                               border_width=2, text_color=("gray10", "#DCE4EE"), command=self.show_next_plane,
                                                               font=ctk.CTkFont(size=25)
                                                               )
        self.next_plane_btn.place(relx=0.90,rely=0.95)

        

        # end buttons
        
        # Labels
        self.flight_info_title_label = ctk.CTkLabel(
            master=self,
            text="APM | Flight no. 0",
            font=ctk.CTkFont(size=30, weight="bold"),
        )
        self.flight_info_title_label.place(relx=0.7, rely=0.05)

        self.flight_info_destination_label = ctk.CTkLabel(
            master=self, text="Destination: ", font=ctk.CTkFont(size=20)
        )
        self.flight_info_destination_label.place(relx=0.52, rely=0.1)

        self.flight_info_seats_label = ctk.CTkLabel(
            master=self, text="Seated: ", font=ctk.CTkFont(size=20)
        )
        self.flight_info_seats_label.place(relx=0.52, rely=0.15)

        self.flight_info_airline_label = ctk.CTkLabel(
            master=self, text="Airline: ", font=ctk.CTkFont(size=20)
        )
        self.flight_info_airline_label.place(relx=0.52, rely=0.2)

        self.flight_info_passengers_label = ctk.CTkLabel(
            master=self, text="Passengers: ", font=ctk.CTkFont(size=20)
        )
        self.flight_info_passengers_label.place(relx=0.52, rely=0.25)


        self.separator_frame = ctk.CTkFrame(
            self, corner_radius=0, fg_color="#3c3c3c"
        )
        self.separator_frame.place(relx=0.5, rely=0.05, relheight=1, relwidth=0.001)

        # Initialize with the first plane's data
        self.update_labels()
    def show_next_seat_page(self):
        """Show the next page of seats"""
        # Update the seat range to show the next page of seats
        self.current_seat_start += self.seat_range

        # Check if we've reached the end of the list, in which case we stop
        if self.current_seat_start > self.get_curr_plane().get_seats():
            print("You think passengers can board the plane somewhere else, maybe on the wing? No more seats to show!")
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
                
                # Create the button
                seat_button = ctk.CTkButton(
                    self.button_frame,
                    text=f"{seat_number}",
                    command=lambda num=seat_number: self.on_seat_click(num),
                    width=50,
                    height=50
                )
                
                # Generate tooltip text based on passenger assignment
                if seat_number <= len(passenger_list):  # Check if a passenger is assigned
                    passenger = passenger_list[seat_number - 1]  # Passenger assignment (0-indexed)
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
                seat_button.grid(row=row, column=col, padx=25, pady=5)  # Add some padding
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
            ", ".join([p.get_first_name() + " " + p.get_last_name() for p in current_plane.get_passengers_list()[i:i+6]])
            for i in range(0, len(current_plane.get_passengers_list()), 6)
        ]
    )
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
    
    def on_seat_click(self, seat_number):
        print(f"Seat {seat_number} clicked!")
        self.spawn_seat_editor()

    def exit_preview(self):
        self.mas.destroy()


    def spawn_seat_editor(self):
        seat_editor_frame = ctk.CTkFrame(
            self, corner_radius=0, fg_color="#3c3c3c"
        )
        seat_editor_frame.place(relx=0.7, rely=0.05, relheight=1, relwidth=20)

        self.textbox = ctk.CTkTextbox(master=self, width=400, corner_radius=0)
        self.textbox.place(relx=0.79, rely=0.1, relheight=0.07, relwidth=0.2)
        self.textbox.insert("0.0","Bart Simpson")

        self.first_name_btn = ctk.CTkButton(
            master=self,
            text="Assign First Name", 
            fg_color="transparent", 
            border_width=2, 
            text_color=("gray10", "#DCE4EE"),
            width=400,
            command=lambda: print("clic")
        )
        self.first_name_btn.place(relx=0.71, rely=0.1, relheight=0.07, relwidth=0.07)

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