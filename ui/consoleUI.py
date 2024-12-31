import subprocess
import ast
class PlaneUI(object):
    def __init__(self, controller):
        self.__controller = controller

    #--------------------------- Option Printer Function ----------------------------
    @staticmethod
    def printMenu():
        menu_commands = {
            '0': """\n\t"[0] exit" -> Exit the application.\n\t\t Usage: exit | q | stop""",
            '1': """\n\t"[1] add [Plane]" -> Add a plane or multiple planes to the repository.\n\t\t Usage: add (1,2,red) (3,5,blue) ...""",
            '2': """\n\t"[2] get [all | passport | name | sub]" -> Gets planes with certain properties.\n\t\t\t Usage: get all \n\t\t\t get index 1 \n""",
            '3': """\n\t"[3] update [index | sort]" ->  Replaces plane at index (or by using name_id) with new plane.\n\t\t Usage: update 1 newvec""",
            '4': """\n\t"[4] del [index | name_id | color | all]" -> Deletes plane by index (or by name_id).\n\t\t Usage: del 1""",
            '5': """\n\t"[6] combine" -> Combine and print planes by different criteria (type /criteria to see).\n\t\t Usage: combine"""
        }
        for cmd in menu_commands:
            print(menu_commands[cmd])

    #--------------------------- Command and Arguments Parser ----------------------------
    def parseInput(self, user_input):
        """Parse input to determine the command and its arguments."""
        commands_map = {
            "0": "exit",
            "1": "add",
            "2": "get",
            "3": "update",
            "4": "del",
            "5": "combine"
        }

        if user_input.strip() in commands_map:
            return commands_map[user_input.strip()], user_input.strip()
        
        parts = user_input.strip().split(maxsplit=1)
        command = parts[0]
        arguments = parts[1] if len(parts) > 1 else ""
        return command, arguments

    #--------------------------- Actual command handler ----------------------------
    def handleCommand(self, command, arguments):
        """Handle specific commands based on parsed input."""
        if command in ["0", "exit", "q", "stop", "break", "python", "python3", "python2"]:
            return "Exiting..."
        
        if command in ["1", "add"]:
            plane = self.readPlaneInput()
            self.__controller.addPlane(plane)

        elif command in ["2", "get"]:
            choice = self.getPlanes(arguments)
            return PlaneUI.displayAnswer(str(self.__controller.getPlanes(choice)), command)
        
        elif command in ["3", "update"]:
            choice = self.updatePlane(arguments)
            
            p = self.__controller.updatePlane(choice)
            return PlaneUI.displayAnswer(p, command)

        elif command in ["4", "del"]:
            choice = self.deletePlane(arguments)
            p = self.__controller.deletePlane(choice)
            return PlaneUI.displayAnswer(p, command)

        elif command in["5", "combine", "group"]:
            choice = self.groupPlanes(arguments)
            p = self.__controller.groupPlanes(choice)

            for group in p:
                print(f"\n\n\n>>>>>>>>>>>>>>>>>> Generated passenger group <<<<<<<<<<<<<<<<<<<\n", group, f"\n>>>>>>>>>>>>>>>>>>> End of passenger group <<<<<<<<<<<<<<<<<<<<<")
                #PlaneUI.displayAnswer(p, command)
            #return 
        else:
            raise Exception("Invalid command.")
        
        return PlaneUI.displayAnswer("", command)

    # ---------------- Visualizing errors and answers for commands ----------------
    @staticmethod
    def displayError(message):
        """Display error messages in a consistent format."""
        new = f"\n[⚡] [ERROR] {message}\n\tPlease try again.\n"
        return str(new)
    
    @staticmethod
    def displayAnswer(message, command):
        """Display answers in a consistent format."""
        if message == "":
            new = f"\n[✅] Sucessfully ran command `{command}`. \n"
        else:
            new = f"\n[✅] Sucessfully ran command `{command}`. \n\n[ANSWER] {message}\n"
        return str(new)
    # ------------------------------------------------------------------------------

    # -------------------------------- Read ---------------------------------
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
            print(PlaneUI.displayError(err))
            return None
        except Exception as e:
            print(PlaneUI.displayError(e))
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
            print(PlaneUI.displayError(err))
        except Exception as e:
            print(PlaneUI.displayError(e))

    @staticmethod
    def readPlaneInput():
        """
        Reads input for plane and passenger data processing.
        """
        confirmation = input("You're about to read from file. Did you insert data in both `plane_db.txt` and `passenger_db.txt`? [Y/N] ").strip()
        if confirmation not in ["Y", "Yes", "YES", "1"]:
            print("Operation cancelled.")
            return
        
        # Read passenger data
        print("Reading passenger data...")
        passenger_data = PlaneUI.readPassengerData()
        if not passenger_data:
            print("Failed to read passenger data. Exiting.")
            return

        # Read plane data
        print("Reading plane data...")
        planes = PlaneUI.readPlaneData(passenger_data)
        if planes:
            print("Plane and passenger data successfully read:")
            for plane in planes:
                print(f"Plane {plane['plane_id']} ({plane['plane_name']}):")
                print(f"  Destination: {plane['destination']}")
                print(f"  Capacity: {plane['capacity']}")
                print(f"  Passengers: {plane['passengers']}")
        else:
            print("Failed to read plane data.")
        
        return planes
        
    # ------------------------------------------------------------------------------
    @staticmethod
    def getPlanes(arguments):
        """Handles both cases for 'get' command."""
        if arguments.strip() == "2":
            command = input("Enter command [all | index | extra]: ").strip()

            if command == "all":
                return command, []
            
            elif command == "index":
                index = int(input("Enter index: "))
                return command, index
            
            elif command == "extra":
                option = int(input("Here are some extra options: \n \t [1] Get planes that have passengers with passport numbers starting with the same 3 letters. \n \t [2] Get passengers from a given plane for which the first name or last name contain a string given as parameter. [3] Get plane/planes where there is a passenger with given name."))
                op = None
                if option in [2,3]:
                    op = input("\n Enter string: ")
                    
                return option, op

            else:
                raise ValueError(f"Unknown 'get' command: {command}")
        else:
            parts = arguments.split()
            if not parts:
                raise ValueError("No arguments provided for 'get' command.")
            
            command = parts[0]
            if command == "all":
                return command, []
            elif command == "index":
                return command, int(parts[1])
            
            else:
                raise ValueError(f"Unknown 'get' command argument: {command}")

    # -------------------------------------------------------------------------------

    @staticmethod
    def updatePlane(arguments):
        if arguments.strip() in ["3", "update"]:
            command = input("Enter update criteria [index]: ").strip()
            if command == "index":
                index = int(input("Enter index to update: "))
                temp_file = "plane_data.txt"
                vector = {
                    "number": 123,
                    "airline": "Placeholder Airline",
                    "seats": 180,
                    "destination": "Placeholder Destination",
                    "passengers_list": [
                        ("Bart", "Simpson", "110392389329822"),
                        ("Lorem", "Ipsum", "1103900281329822"),
                    ]
                }
                with open(temp_file, "w") as file:
                    file.write(f"{vector['number']}\n")
                    file.write(f"{vector['airline']}\n")
                    file.write(f"{vector['seats']}\n")
                    file.write(f"{vector['destination']}\n")
                    file.write(f"{vector['passengers_list']}\n")

                process = subprocess.Popen(["notepad", temp_file])

                process.wait()

                with open(temp_file, "r") as file:
                    lines = file.readlines()

                try:
                    updated_vector = {
                        "number": int(lines[0].strip()),
                        "airline": lines[1].strip(),
                        "seats": int(lines[2].strip()),
                        "destination": lines[3].strip(),
                        "passengers_list": ast.literal_eval(lines[4].strip())
                    }
                    print("Vector successfully updated!")
                    return (command, index, updated_vector)

                except (IndexError, ValueError, SyntaxError) as e:
                    print(f"Error parsing file content: {e}")
                    return f"Error parsing file content: {e}"
            elif command == "sort":
                criteria = int(input("How would you like to sort the plane repository? \n \t [1] By number of passengers abroad. \n \t [2] By number of passengers with first name. \n \t [3] By concatenation of number of passengers and destination.\n"))
                sub = None
                if criteria == 2:
                    sub = input("Enter the starting substring of the first name: ")
                
                return command, criteria, sub

                

    # -------------------------------------------------------------------------------
    @staticmethod
    def deletePlane(arguments):
        """Handles both cases for 'delete' command."""
        if arguments.strip() == "4":
            command = input("Enter delete criteria [index | all]: ").strip()

            if command == "index":
                index = int(input("Enter index: "))
                return "index", index

            elif command == "all":
                return "all", None

            else:
                raise ValueError(f"Unknown 'delete' command: {command}")
    
        else:
            raise ValueError("Invalid delete command.")

    # -------------------------------------------------------------------------------
    @staticmethod
    def groupPlanes(arguments):
        """Handles both cases for 'groupPlanes' command."""
        if arguments.strip() == "5":
            command = input("Enter grouping criteria [1 | 2]: \n\t[1] k-passengers - Same plane different last names. \n\t[2] k-planes - Same destination different airline.").strip()

            if command == "1":
                k = int(input("Enter k: "))
                return "k-passengers", int(k)

            elif command == "2":
                k = int(input("Enter k: "))
                return "k-planes", int(k)

            else:
                raise ValueError(f"Unknown 'group' command: {command}")
    
        else:
            raise ValueError("Invalid group command.")

    def mainMenu(self):
        error, result = "", ""
        while True:
            self.printMenu()
            user_input = input(f"{error}{result}Enter a command number or full command: ")
            result = ""
            try:
                command, arguments = self.parseInput(user_input)
                result = self.handleCommand(command, arguments)
                if result == "Exiting...":
                    print(result)
                    break

                error = ""
            except Exception as err:
                error = PlaneUI.displayError(err)
                continue
