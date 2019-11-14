from pur_beurre.view.view1_welcome import ViewWelcome
from pur_beurre.view.view2_steps import ViewSteps
from pur_beurre.view.view3_user_login import ViewLogin


class MainWindow:
    """ This class takes in parameter: the main window and the controller.
    It has methods to set the window and to open the different views of
    the application"""

    def __init__(self, root, cont_start_up):
        self.root = root
        self.controller = cont_start_up
        self.parameter_root_window()
        self.text_cnx_mysql = None
        self.text_search_if_db_exist = None
        self.text_db_is_create = None
        self.text_presence_data = None
        self.view2 = None

    def parameter_root_window(self):
        """ this method is responsible for defining the characteristics
        of my main window with:
        - title
        # icon
        - size and location
        - minimum size"""
        self.root.title("Application Pur Beurre")
        self.root.geometry("450x600-20+20")
        self.root.minsize(450, 600)
        self.root['bg'] = 'white'

    def open_view1_welcome(self):
        """ This method opens the view 1: welcome """
        ViewWelcome(self.root, self.controller)

    def open_view2_steps(self, txt1, txt2, txt3, txt4):
        """ This method opens the view 2: steps before launch """
        self.text_cnx_mysql = txt1
        self.text_search_if_db_exist = txt2
        self.text_db_is_create = txt3
        self.text_presence_data = txt4
        self.view2 = ViewSteps(self.root, self.controller, self.text_cnx_mysql,
                               self.text_search_if_db_exist,
                               self.text_db_is_create, self.text_presence_data)

    def open_view3_login(self):
        ViewLogin(self.root, self.controller)
