from tkinter import messagebox
from config.config_db import CATEGORY
# import model
from pur_beurre.model.database.manage_db import ManageDatabase
# import view
from pur_beurre.view.view import MainWindow

from pur_beurre.controller.cont_user import ControllerUser


class ControllerStartUp:
    def __init__(self, root):
        self.model = ManageDatabase()
        self.view = MainWindow(root, self)
        self.root = root
        self.open_view1_welcome()
        self.view2 = None
        self.texts = []
        self.cnx = None
        self.txt_cnx_mysql = None
        self.txt_db_exist = None
        self.txt_db_create = None
        self.txt_data = None

    def open_view1_welcome(self):
        # -> main_window (VIEW)
        self.view.open_view1_welcome()

    def open_view2_steps(self):
        # -> manage_db (MODEL)
        self.cnx = self.model.connection_mysql()

        self.txt_cnx_mysql = self.model.text_connect_mysql
        self.txt_db_exist = self.model.text_search_if_db_exist
        self.txt_db_create = self.model.text_db_is_create
        self.txt_data = self.model.text_insert_data_api
        # -> main_window (VIEW)
        self.view.open_view2_steps(self.txt_cnx_mysql, self.txt_db_exist,
                                   self.txt_db_create, self.txt_data)

    def update_data(self):
        pass

    def download_data(self):
        for x, cat in enumerate(CATEGORY):
            print("chargement des données de la catégorie ", cat)
            self.model.download_api_data(cat)
            self.model.insert_data_in_tables(self.cnx, self.model.products[x],
                                             cat, (x+1))
        self.controller_user()

    def controller_user(self):
        ControllerUser(self.cnx, self.root)
