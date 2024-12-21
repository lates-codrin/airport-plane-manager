<p align="center">
    <img width="800" src="https://i.imgur.com/534UkoJ.png" alt="APM Logo">
</p>

<h1 align="center" style="margin-top: 0px;">[✈️] APM - Airport Plane Manager</h1>

<p align="center" >v 1.0.1</p>



## How to run

To run this program:
There might be some scaling issue. They will be fixed in the next version so until then please keep your windows scaling at 100%.

Run this command:
```bash
  python coordinator.py
```


## Features

- Perform CRUD operations on `planes` and `passengers`
- Sort & combine planes by different criterias
- Visualize planes and passengers using the Plane Explorer
- And much more to come!


## Usage/Examples
1. CTk UI: Simply run the program.
2. Console UI:\
   [0] exit -> Exit the application. Eg. : exit | q | stop \
   [1] add [Plane] -> Add a plane or multiple planes to the repository. Eg: add (1,2,red) (3,5,blue) ... \
   [2] get [all | passport | name | sub] -> Gets planes with certain properties. \
   [3] update [index | sort] ->  Replaces plane at index (or by using name_id) with new plane. \
   [4] del [index | name_id | color | all] -> Deletes plane by index (or by name_id). \
   [6] combine -> Combine and print planes by different criteria (type /criteria to see). \



# Program Iterations (Versions)

## Iteration 1

- Created the domain package containing the classes: `MyPlane`, `MyPassenger`.
- Defined simple getters and setters aswell as functions for the classes mentioned above.

## Iteration 2
- Created the infrastructure package containing the repository classes: `PassengerRepository`, `PlaneRepository`
- Created simple getters and setters for these classes, and implemented the functions mentioned on the paper.
- Redefined error handling with a custom class and more checks.

## Iteration 3
- Added Console UI with options for all of the functions mentioned in the paper.
- Added test functions for the domain and repository
- Fixed some bugs


## Iteration 4
- Added CTk UI which includes a plane explorer and a frame for each function.


## Iteration 5
- Improved UI on both sides.
  
## Lessons Learned

bonk


## Authors

- [@lates-codrin](https://github.com/lates-codrin)

## Acknowledgements

 - UI Library used: [Custom TKinter](https://customtkinter.tomschimansky.com/)
 - Icons used: [Flat Icon](https://www.flaticon.com/)
