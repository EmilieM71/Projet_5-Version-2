from tkinter import Frame, Label, Canvas, Button, Entry
from config.config_view import (TITLE_FONT, WHITE, TITLE_COLOR, LINE_COLOR,
                                SUBTITLE_FONT, BLACK, TEXT_FONT)


class ViewWelcome:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.frame_welcome = Frame(root, bg='white')
        self.frame_welcome.grid(row=0, column=0, sticky='nesw',
                                padx=20, pady=20)
        self.info = None
        self.button_ok1 = None
        self.create_user = None
        self.user = None
        self.sql_stmt = None
        self.button_ok2 = None

        self.create_widgets()

    def function_button_ok2(self):
        new_text = "Vous avez créé un utilisateur de démo."
        self.create_user.config(text=new_text, fg='gray')
        self.user.destroy()
        self.sql_stmt.destroy()
        self.button_ok2.destroy()
        # create line
        line3 = Canvas(self.frame_welcome, bd=0, highlightthickness=0,
                       bg=WHITE, height=20)
        line3.create_line((10, 10), (370, 10), fill=LINE_COLOR, width=2)
        line3.grid(row=10, sticky='w')

        # create subtitle 2
        subtitle2 = Label(self.frame_welcome,
                          text=" Cliquez sur le bouton de votre choix : ",
                          font=SUBTITLE_FONT, bg=WHITE, fg=BLACK)
        subtitle2.grid(row=11, sticky='w')

        # create line
        line4 = Canvas(self.frame_welcome, bd=0, highlightthickness=0,
                       bg=WHITE, height=20)
        line4.create_line((10, 10), (370, 10), fill=LINE_COLOR, width=2)
        line4.grid(row=12, sticky='w')

        # create button 1
        text_button1 = " Lancez l'application   "
        button1 = Button(self.frame_welcome, bd=2, text=text_button1,
                         font=("Arial", 20), bg='#ADD0EC', fg=WHITE,
                         command=self.function_button1)
        button1.grid(row=13, sticky='ns', pady=10)

        # create button 1
        text_button2 = "            Quitter           "
        button2 = Button(self.frame_welcome, bd=2, text=text_button2,
                         font=("Arial", 20), bg='#ADD0EC', fg=WHITE,
                         command=self.function_leave)
        button2.grid(row=14, sticky='ns', pady=10)

    def function_button_ok1(self):
        new_text = "Vous avez MySQL version 8 installer sur votre ordinateur."
        self.info.config(text=new_text, fg='gray')
        self.button_ok1.destroy()
        self.create_new_widgets()

    def create_new_widgets(self):
        # create text for create user mysql for use the application
        text_info_user = " Maintenant, vous devez créer l'utilisateur démo : "
        self.create_user = Label(self.frame_welcome, text=text_info_user,
                                 font=TEXT_FONT, bg=WHITE, fg=BLACK)
        self.create_user.grid(row=5, sticky='w', pady=10)

        text_create_user = "Connectez-vous à MySQL et entrez le script SQL " \
                           "suivant"
        self.user = Label(self.frame_welcome, text=text_create_user,
                          font=TEXT_FONT, bg=WHITE, fg=BLACK)
        self.user.grid(row=6, sticky='w')

        # create text : statements sql for create user
        text_sql_stmt = """
        1   CREATE USER 'student_OC'@'localhost' IDENTIFIED BY '123abc';
        2   GRANT ALL PRIVILEGES ON PurBeurre.* TO 'student'@'localhost';
                """
        self.sql_stmt = Label(self.frame_welcome, text=text_sql_stmt,
                              font=TEXT_FONT, bg=BLACK, fg=WHITE, pady=2)
        self.sql_stmt.grid(row=7, sticky='w')

        self.button_ok2 = Button(self.frame_welcome, bd=2, text=" OK ",
                                 font=("Arial", 10), bg='#ADD0EC',
                                 fg=WHITE, command=self.function_button_ok2)
        self.button_ok2.grid(row=9, sticky='ns', pady=10)

    def function_button1(self):
        self.frame_welcome.destroy()
        self.controller.open_view2_steps()

    def function_leave(self):
        self.root.destroy()

    def create_widgets(self):
        # create title
        title = Label(self.frame_welcome, text=" BIENVENUE ", font=TITLE_FONT,
                      bg=WHITE, fg=TITLE_COLOR)
        title.grid(row=0, sticky='ns', pady=5)

        # create line
        line1 = Canvas(self.frame_welcome, bd=0, highlightthickness=0,
                       bg=WHITE, height=20)
        line1.create_line((10, 10), (400, 10), fill=LINE_COLOR, width=2)
        line1.grid(row=1, sticky='w')

        # create subtitle
        subtitle1 = Label(self.frame_welcome, text=" Informations : ",
                          font=SUBTITLE_FONT, bg=WHITE, fg=BLACK)
        subtitle1.grid(row=2, sticky='w')

        # create line
        line2 = Canvas(self.frame_welcome, bd=0, highlightthickness=0,
                       bg=WHITE, height=20)
        line2.create_line((10, 10), (400, 10), fill=LINE_COLOR, width=2)
        line2.grid(row=3, sticky='w')

        # create text : information to know before launching the application
        text_info = """\
        Pour utiliser cette application, vous devez avoir MySQL version 8 
        installé. Cliquez sur OK, si MySQL Version 8 est installée, sinon 
        fermez l'application et installez MySQL"""

        self.info = Label(self.frame_welcome, text=text_info, font=TEXT_FONT,
                          bg=WHITE, fg=BLACK, justify='left')
        self.info.grid(row=4, sticky='w')

        self.button_ok1 = Button(self.frame_welcome, bd=2, text="OK",
                                 font=("Arial", 10), bg='#ADD0EC', fg=WHITE,
                                 command=self.function_button_ok1)
        self.button_ok1.grid(row=5, sticky='ns', pady=10)
