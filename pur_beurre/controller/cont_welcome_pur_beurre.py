# import model

# import view
from pur_beurre.view.view4_pur_beurre_welcome import ViewPurBeurreWelcome
# import controller
from pur_beurre.controller.cont_category import ControllerCategory


class ControllerWelcomePB:

    def __init__(self, cnx, root, id_user, pseudo):
        self.cnx = cnx
        self.cursor = self.cnx.cursor()
        self.root = root
        self.id_user = id_user
        self.pseudo = pseudo
        self.model = None

        self.open_view4_pur_beurre_welcome()

    def open_view4_pur_beurre_welcome(self):
        ViewPurBeurreWelcome(self.root, self, self.pseudo)

    def controller_category(self, pseudo):
        ControllerCategory(self.cnx, self.root, self.id_user, pseudo)
