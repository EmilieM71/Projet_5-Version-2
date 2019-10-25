from pur_beurre.view.view1_welcome import ViewWelcome
from pur_beurre.view.view2_steps import ViewSteps


class MainWindow:
    """ This class takes in parameter: the main window and the controller """

    def __init__(self, root, cont_start_up):
        self.root = root
        self.controller = cont_start_up
        self.parameter_root_window()

    def parameter_root_window(self):
        """ this method is responsible for defining the characteristics
        of my main window with:
        - title
        # icon
        - size and location
        - minimum size"""
        self.root.title("Pure butter application")
        self.root.geometry("450x600-20+20")
        self.root.minsize(450, 600)

    def open_view1_welcome(self):
        ViewWelcome(self.root, self.controller)

    def open_view2_steps(self, text1, text2, text3, text4):
        ViewSteps(self.root, self.controller, text1, text2, text3, text4)
