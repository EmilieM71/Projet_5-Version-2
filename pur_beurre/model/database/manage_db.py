from mysql import connector
from mysql.connector import errorcode

from config.config_db import HOST, USER, PASSWORD, DB_NAME


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
        self.text_connect_db = None
        self.text_search_if_db_exist = None
        self.text_db_is_create = None

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

        except connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                # Graphical interface with Tkinter
                self.text_connect_mysql = "Something is wrong with your " \
                                          "user name or password"
                # Mode console
                print("Something is wrong with your user name or password")

    def connection_db(self, cnx):
        self.cursor = cnx.cursor()
        try:
            self.cursor.execute("USE {}".format(DB_NAME))
            # Graphical interface with Tkinter
            self.text_search_if_db_exist = "The {} database exists." \
                .format(DB_NAME)
            self.text_connect_db = "You are connected to {} Database" \
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
            self.cursor.close()
            return self.cnx

    def create_db(self, cnx):
        pass
