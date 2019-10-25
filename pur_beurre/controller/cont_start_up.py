from tkinter import *
# import model
from pur_beurre.model.database.manage_db import ManageDatabase
# import view
from pur_beurre.view.main_window import MainWindow


class ControllerStartUp:
    def __init__(self, root):
        self.model = ManageDatabase()
        self.view = MainWindow(root, self)
        self.open_view1_welcome()

    def open_view1_welcome(self):
        self.view.open_view1_welcome()

    def open_view2_steps(self):
        self.model.connection_mysql()
        text1 = self.model.text_connect_mysql
        text2 = self.model.text_connect_db
        text3 = self.model.text_search_if_db_exist
        text4 = self.model.text_db_is_create
        self.view.open_view2_steps(text1, text2, text3, text4)
