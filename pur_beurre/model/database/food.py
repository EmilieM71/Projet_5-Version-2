class Food:

    def __init__(self, cnx, cursor):
        self.cnx = cnx
        self.cursor = cursor
        self.id_food = None
        self.name = None
        self.nutriscore = None
        self.url = None
        self.ingredient = None
        self.palm_oil = None
        self.allergen = None
        self.energy_100g = None
        self.energy = None
        self.fat_100g = None
        self.saturated_fat_100g = None
        self.carbohydrates_100g = None
        self.sugars_100g = None
        self.proteins_100g = None
        self.salt_100g = None
        self.sodium_100g = None
        self.nutrition_score_fr_100g = None
        self.nova_group_100g = None
        self.text_presence_data = None
        self.presence_food = False

    def create(self, id_food, name_food, nutriscore_food, url_food,
               ingredient, palm_oil, allergen, energy_100g, energy, fat_100g,
               saturated_fat_100g, carbohydrates_100g, sugars_100g,
               proteins_100g, salt_100g, sodium_100g, nutrition_score_fr_100g,
               nova_group_100g):
        """This feature allows you to create a line in the food table and
        returns the code
        :param id_food: str
        :param name_food: str
        :param nutriscore_food: str
        :param url_food: str
        :param ingredient: str
        :param palm_oil: str
        :param allergen: str
        :param energy_100g: str
        :param energy: str
        :param fat_100g: str
        :param saturated_fat_100g: str
        :param carbohydrates_100g: str
        :param sugars_100g: str
        :param proteins_100g: str
        :param salt_100g: str
        :param sodium_100g: str
        :param nutrition_score_fr_100g: int
        :param nova_group_100g: int
        """
        # product = [id:0, name:1, nutriscore:5, url:6,
        #  ingredient:7, palm_oil:8, allergen:9, energy_100g:10,
        # energy:11, fat_100g:12, saturated_fat_100g:13,
        # carbohydrates_100g:14, sugars_100g:15, proteins_100g:16,
        # salt_100g:17, sodium_100g:18, nutrition_score_fr_100g:19,
        # nova_group_100g:20]
        self.cursor = self.cnx.cursor()
        # 1- Create a line in the food table
        # 1.1- Storage of the INSERT statement (SQL) in a variable
        add_food = ("INSERT INTO food "
                    "(id, name, nutriscore, url, ingredient, palm_oil, "
                    "allergen, energy_100g, energy, fat_100g, "
                    "saturated_fat_100g, carbohydrates_100g, sugars_100g, "
                    "proteins_100g, salt_100g, sodium_100g, "
                    "nutrition_score_fr_100g, nova_group_100g)"
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,"
                    "%s, %s, %s, %s, %s, %s)"
                    "ON DUPLICATE KEY UPDATE id=id")
        # 1.2- Storage data in a variable
        data_food = (id_food, name_food, nutriscore_food, url_food,
                     ingredient, palm_oil, allergen, energy_100g, energy,
                     fat_100g, saturated_fat_100g, carbohydrates_100g,
                     sugars_100g, proteins_100g, salt_100g, sodium_100g,
                     nutrition_score_fr_100g, nova_group_100g)

        # 1.3- Insert new category
        self.cursor.execute(add_food, data_food)

        self.id_food = self.cursor.lastrowid
        self.cnx.commit()

    def search_if_data(self):
        """   """
        query = "SELECT id FROM food "
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        if not rows:
            # Graphical interface with Tkinter
            self.text_presence_data = "There is no data in database"
            # Mode console
            # print("There is no data in database")
            return self.presence_food
        else:
            # Graphical interface with Tkinter
            self.text_presence_data = "There is data in database"
            # Mode console
            # print("There is data in database")
            self.presence_food = True
            return self.presence_food

    def get_id(self, name_food):
        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT id FROM food "
                 "WHERE name = %s")
        # Execute SELECT statement (SQL)
        self.cursor.execute(query, (name_food,))
        rows = self.cursor.fetchall()
        if not rows:
            return
        else:
            for row in rows:
                self.id_food = str(row[0])
                return self.id_food

    def search_if_food_exist(self, code):
        """ This function search if the food already exists in the database"""

        # Storage of the SELECT statement (SQL) in a variable
        query = ("SELECT * FROM food "
                 "WHERE id = %s")
        # Execute SELECT statement (SQL)
        self.cursor.execute(query, (code, ))
        rows = self.cursor.fetchall()
        print(rows)
        if not rows:
            return
        else:
            return rows[0]

    def recover_list_food_name_from_list_id_food(self, list_id_food):
        list_name_food = []
        for id_food in list_id_food:
            # Storage of the SELECT statement (SQL) in a variable
            query = ("SELECT name FROM food "
                     "WHERE id = %s")
            # Execute SELECT statement (SQL)
            self.cursor.execute(query, (id_food,))
            rows = self.cursor.fetchall()
            for row in rows:
                id_name_food = row[0]
                list_name_food.append(id_name_food)
        return list_name_food

    def substitute_research(self, list_id_food):
        list_substitute = []
        for id_food in list_id_food:
            # Storage of the SELECT statement (SQL) in a variable
            query = ("SELECT * FROM food "
                     "WHERE id = %s and nutriscore = 'a'")
            # Execute SELECT statement (SQL)
            self.cursor.execute(query, (id_food,))
            rows = self.cursor.fetchall()
            if rows:
                list_substitute.append(rows)
        return list_substitute
