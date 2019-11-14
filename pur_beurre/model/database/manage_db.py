from mysql import connector
from mysql.connector import errorcode

from config.config_db import HOST, USER, PASSWORD, DB_NAME, PATH_FILE
from pur_beurre.model.api.api_data_collection import ApiDataCollection
from pur_beurre.model.database.food import Food
from pur_beurre.model.database.category import Category
from pur_beurre.model.database.category_food import CategoryFood
from pur_beurre.model.database.brand import Brand
from pur_beurre.model.database.food_brand import FoodBrand
from pur_beurre.model.database.store import Store
from pur_beurre.model.database.food_store import FoodStore


class ManageDatabase:
    """ class to manage the database
            - Connection to MySQL
            - Connect database DB_NAME if exist, elif create DB
            - Create database
            - exit connection. """

    def __init__(self):
        self.cnx = None
        self.cursor = None
        self.text_connect_mysql = None
        self.text_search_if_db_exist = None
        self.text_db_is_create = None
        self.text_insert_data_api = None
        self.products = []

    def download_api_data(self, category):
        """ """
        # Creating an object for class ApiDataCollection
        data_api = ApiDataCollection()  # Data from api

        # Recover openFoodFacts API data
        data_api.import_products(category)
        data_api.clean_data(data_api.products)
        self.products.append(data_api.all_products)

        return self.products

    def insert_data_in_tables(self, cnx, products, cat, id_cat):

        # # Creating a cursor object
        cursor = cnx.cursor()

        # Creating an object for each class
        food_table = Food(cnx, cursor)  # Table food
        cat_table = Category(cnx, cursor)  # Table category
        cat_food_table = CategoryFood(cnx, cursor)  # table category_food
        brand_table = Brand(cnx, cursor)  # table brand
        food_brand_table = FoodBrand(cnx, cursor)  # table food_brand
        store_table = Store(cnx, cursor)  # Table store
        food_store_table = FoodStore(cnx, cursor)  # Table food_store

        # Insert data into the corresponding tables
        # Insert category in table category)
        cat_table.create_category(id_cat, cat)
        for product in products:
            if product[0] == "" or product[1] == "" or product[1] is None:
                return
            else:
                if product[5] is None:
                    product[5] = ''
                food_table.create(product[0], product[1], product[5],
                                  product[6], product[7], product[8],
                                  product[9], product[10], product[11],
                                  product[12], product[13], product[14],
                                  product[15], product[16], product[17],
                                  product[18], product[19], product[20])
                id_food = product[0]

                # Insert id_food and id_cat in table category_food
                cat_food_table.create_category_food(id_cat, id_food)
                # Insert brand in brand table
                if product[4] != "" and product[4] is not None:
                    if product[4].find(",") == -1:
                        # Search if the brand already exists in  database
                        # and if not exist, insert name in table brand
                        brand_table.search_if_brand_exist(product[4])
                        id_brand = brand_table.brand_id
                        # Insert id_food and id_brand in food_brand table
                        food_brand_table.search_if_food_brand_exist(
                            id_food, id_brand)
                    else:
                        for brand in product[4].split(","):
                            # Search if the brand already exists in  database
                            # and if not exist, insert name in table brand
                            brand_table.search_if_brand_exist(brand)
                            id_brand = brand_table.brand_id
                            # Insert id_food and id_brand in food_brand table
                            food_brand_table.search_if_food_brand_exist(
                                id_food, id_brand)
                else:
                    # Insert store in store table
                    if product[3] != "":
                        for store in product[3].split(","):
                            store_table.search_if_store_exist(store)
                            id_store = store_table.store_id
                            # Insert id_food and id_store in food_brand table
                            food_store_table.search_if_food_store_exist(
                                id_food, id_store)

        cursor.close()

        # Graphical interface with Tkinter
        # self.text_insert_data_api = "The data was inserted into the '{]' " \
        #                             "database".format(DB_NAME)
        # Mode console
        print("The data was inserted into the 'PurBeurre' database")

    def search_presence_api_data_in_database(self, cnx):
        """ """
        cursor = cnx.cursor()
        food_table = Food(cnx, cursor)  # Table food
        food_table.search_if_data()
        self.text_insert_data_api = food_table.text_presence_data

    def create_db(self, cnx):
        """ Create database PurBeurre if not exist"""
        self.cursor = cnx.cursor()
        try:
            # Opening the file containing the SQL script
            sql_file = open(PATH_FILE, 'r')
            # Read file
            sql_text = sql_file.read()
            sql_stmts = sql_text.split(';')
            for s in sql_stmts:
                self.cursor.execute(s)
            # Graphical interface with Tkinter
            self.text_db_is_create = "The database is created."
            # Mode console
            print("The database is created")
            # Make sure db is committed
            self.cnx.commit()

        except connector.Error as err:
            # Graphical interface with Tkinter
            self.text_db_is_create = "Failed creating database."
            # Mode console
            print("Failed creating database: {}".format(err))
            exit(1)

        else:
            self.cursor.close()
            return cnx

    def connection_db(self, cnx):
        """ """
        self.cursor = cnx.cursor()
        try:
            self.cursor.execute("USE {}".format(DB_NAME))
            # Graphical interface with Tkinter
            self.text_search_if_db_exist = "The {} database exists." \
                .format(DB_NAME)
            # Mode console
            print("You are connected to {} Database".format(DB_NAME))

        except connector.Error:
            # Graphical interface with Tkinter
            self.text_search_if_db_exist = "The {} Database does not exists." \
                .format(DB_NAME)
            # Mode console
            print("Database {} does not exists.".format(DB_NAME))
            # Create database 'PurBeurre'
            self.create_db(cnx)

        else:
            # searches for OpenFoodFact API data in the database
            self.search_presence_api_data_in_database(cnx)
            self.cursor.close()
            return self.cnx

    def connection_mysql(self):
        """ this function is responsible for connecting to mysql with the
        demo profile:
        - HOST = 'localhost'
        - USER = 'student_OC'
        - PASSWORD = '123abc'
        """

        # connection MySQL
        config = {
            'host': HOST,
            'user': USER,
            'password': PASSWORD
        }
        try:
            # connection to MySQL
            self.cnx = connector.connect(**config)
            # Graphical interface with Tkinter
            # (text to display in the steps view)
            self.text_connect_mysql = "You are connected to MySQL"
            # Mode console
            print("You are connected to MySQL")
            # connection to database 'PurBeurre'
            self.connection_db(self.cnx)
            self.search_presence_api_data_in_database(self.cnx)
            return self.cnx

        except connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                # Graphical interface with Tkinter
                self.text_connect_mysql = "Something is wrong with your " \
                                          "user name or password"
                # Mode console
                print("Something is wrong with your user name or password")

    def __exit__(self):
        """ """
        self.cnx.close()
        print("")
