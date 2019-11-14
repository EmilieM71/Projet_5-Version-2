# import model
from pur_beurre.model.database.category import Category
# import view
from pur_beurre.view.view5_find_substitute_select_cat import ViewSelectCategory
# import controller
from pur_beurre.controller.cont_cat_food import ControllerCategoryFood


class ControllerCategory:

    def __init__(self, cnx, root, id_user, pseudo):
        self.cnx = cnx
        self.cursor = self.cnx.cursor()
        self.root = root
        self.id_user = id_user
        self.model = Category(cnx, self.cursor)

        self.open_view_select_cat(pseudo)

    def open_view_select_cat(self, pseudo):
        ViewSelectCategory(self.root, self, pseudo)

    def id_selected_category(self, selected_category, pseudo):
        id_cat = self.model.get_id(selected_category)
        self.controller_category_food(id_cat, selected_category, pseudo)

    def controller_category_food(self, id_cat, name_cat, pseudo):
        ControllerCategoryFood(self.cnx, self.root, self.id_user,
                               id_cat, name_cat, self, pseudo)
