# import model
from pur_beurre.model.database.user import Users
# import view
from pur_beurre.view.view3_user_login import ViewLogin
# import controller
from pur_beurre.controller.cont_welcome_pur_beurre import ControllerWelcomePB


class ControllerUser:

    def __init__(self, cnx, root):
        self.cnx = cnx
        self.cursor = self.cnx.cursor()
        self.root = root
        self.model = Users(cnx, self.cursor)

        self.open_view_login()

    def open_view_login(self):
        ViewLogin(self.root, self)

    def verify_if_user_exists(self, pseudo, password):
        id_user = self.model.search_if_user_exist(pseudo, password)
        return id_user

    def search_if_pseudo_exist(self, pseudo):
        pseudo = self.model.search_if_pseudo_exist(pseudo)
        print("pseudo : ", pseudo)
        return pseudo

    def create_user(self, pseudo, password, email):
        self.model.create_user(email, pseudo, password)
        print(self.model.user_id)
        id_user = self.model.user_id
        self.controller_welcome_pur_beurre(id_user, pseudo)

    def controller_welcome_pur_beurre(self, id_user, pseudo):
        ControllerWelcomePB(self.cnx, self.root, id_user, pseudo)
