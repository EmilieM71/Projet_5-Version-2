# import model
from pur_beurre.model.database.food import Food
# import view
from pur_beurre.view.view6_find_substitute_select_food import ViewSelectFood
from pur_beurre.view.view7_find_substitute_select_sub import ViewSelectSubstitute
# import controller


class ControllerFood:

    def __init__(self, cnx, root, id_user, id_cat, name_cat, list_id_food,
                 cont_cat, pseudo):
        self.cnx = cnx
        self.cursor = self.cnx.cursor()
        self.root = root
        self.id_user = id_user
        self.id_cat = id_cat
        self.name_cat = name_cat
        self.cont_cat = cont_cat
        self.list_id_food = list_id_food
        self.model = Food(cnx, self.cursor)
        self.view = None

        self.recover_list_food_name_from_list_id_food(list_id_food, pseudo)

    def recover_list_food_name_from_list_id_food(self, list_id_food, pseudo):
        list_food = \
            self.model.recover_list_food_name_from_list_id_food(list_id_food)
        self.open_view_select_food(list_food, pseudo)

    def open_view_select_food(self, list_food, pseudo):
        self.view = ViewSelectFood(self.root, self, list_food, self.name_cat,
                                   pseudo)
        return self.view

    def controller_category(self, pseudo):
        self.cont_cat.open_view_select_cat(pseudo)

    def displays_food_information(self, selected_food):
        id_food = self.model.get_id(selected_food)
        # Display information about selected food
        info = self.model.search_if_food_exist(id_food)
        return info

    def substitute_research(self, pseudo, cat_name, info_food):
        list_substitute = self.model.substitute_research(self.list_id_food)
        self.open_view7(pseudo, cat_name, info_food, list_substitute)

    def open_view7(self, pseudo, cat_name, info_food, list_substitute):
        ViewSelectSubstitute(self.root, self, cat_name, list_substitute,
                             pseudo, info_food)

