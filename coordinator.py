""" Task: -
    Author: Lates Codrin-Gabriel (codrin.lates@stud.ubbcluj.ro)
    Date: 19.12.2024 10:47 AM
    Iteration: -

    Version history will be made public after assignment goes past due.
    https://github.com/-
"""


from domain.plane.plane import MyPlane
from domain.passenger.passenger import MyPassenger
from infrastructure.passengers.passengerRepository import passengerRepository
from infrastructure.planes.planeRepository import planeRepository
from domain.plane.planeValidator import PlaneValidator
from ui.console2 import PlaneUI as ConsolePlaneLauncher

from application.planeController import PlaneController
from ui.other import PlaneUI as UserInterfacePlaneLauncher
def start():
    #crearte the repo
    repo = planeRepository()
    

    #create controller, and validator
    vector_validator = PlaneValidator()
    controller = PlaneController(repo, vector_validator)

    #create ui

    '''choice = input("You're currently using the CONSOLE configuration. \nWould you like to instead launch the USER INTERFACE - apm? [Y/N]: ")
    if choice.lower() == "y":
        ui = UserInterfacePlaneLauncher(controller)
        ui.mainloop()
    elif choice.lower()=="n":
        ui = ConsolePlaneLauncher(controller)
        ui.mainMenu()
    else:
        print("\n Not a valid option.")'''
    ui = UserInterfacePlaneLauncher(controller)
    ui.mainloop()
start()