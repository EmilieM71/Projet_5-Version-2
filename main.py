from tkinter import Tk
# Import dans controller du controller qui lance l'applivcation
from pur_beurre.controller.cont_start_up import ControllerStartUp


if __name__ == "__main__":
    # Create window (an object of the Tk class of tkinter)
    root = Tk()

    # Create controller object
    app = ControllerStartUp(root)

    # Running the mainloop method allows:
    # - enter the main loop
    # - keep my root window visible
    # - to maintain the program in court, until the closing of the window
    root.mainloop()
    # If the window is closed, you exit the main loop, and the program stops.
