# import model
from pur_beurre.model.database.category_food import CategoryFood
# import controller
from pur_beurre.controller.cont_food import ControllerFood


class ControllerCategoryFood:

    def __init__(self, cnx, root, id_user, id_cat, name_cat, cont_cat, pseudo):
        self.cnx = cnx
        self.cursor = self.cnx.cursor()
        self.root = root
        self.id_user = id_user
        self.id_cat = id_cat
        self.name_cat = name_cat
        self.controller_cat = cont_cat
        self.pseudo = pseudo
        self.model = CategoryFood(cnx, self.cursor)

        self.recovering_product_list_for_selected_category()

    def recovering_product_list_for_selected_category(self):
        list_id_food = self.model.recovering_list_id_food(self.id_cat)
        self.controller_food(list_id_food, self.pseudo)

    def controller_food(self, list_id_food, pseudo):
        ControllerFood(self.cnx, self.root, self.id_user,
                       self.id_cat, self.name_cat, list_id_food,
                       self.controller_cat, pseudo)

