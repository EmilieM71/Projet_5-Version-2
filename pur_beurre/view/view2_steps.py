from tkinter import Frame, Label, Canvas, Button
from config.config_view import SUBTITLE_FONT, WHITE, TITLE_COLOR, LINE_COLOR


class ViewSteps:
    def __init__(self, root, controller, txt1, txt2, txt3, txt4):
        self.root = root
        self.controller = controller
        self.text_cnx_mysql = txt1
        self.text_db_exist = txt2
        self.text_db_is_create = txt3
        self.text_presence_data = txt4
        self.frame_steps = Frame(root, bg=WHITE)
        self.frame_steps.grid(row=0, column=0, sticky='nesw', padx=5)
        self.can = None

        self.create_widgets()

    def function_button(self):
        if self.text_presence_data == "There is no data in database":
            self.controller.download_data()
        else:
            self.controller.controller_user()

    def create_widgets(self):
        # create title
        title = Label(self.frame_steps,
                      text=" ETAPES DE LANCEMENT DE L'APPLICATION ",
                      font=SUBTITLE_FONT, bg=WHITE, fg=TITLE_COLOR)
        title.grid(row=0, column=0, sticky='ns', pady=5)

        # create line
        line1 = Canvas(self.frame_steps, bd=0, highlightthickness=0, bg=WHITE,
                       height=20)
        line1.create_line((10, 10), (370, 10), fill=LINE_COLOR, width=2)
        line1.grid(row=1, sticky='w')

        # create canvas
        self.can = Canvas(self.frame_steps, bg=WHITE, width=430, height=480)
        self.can.grid(row=2, sticky='ns')
        self.can.create_rectangle((175, 10), (325, 30), width=4,
                                  state='disabled', outline='green')
        self.can.create_text((250, 20), state='disabled',
                             text=" Lancement de l'application ")
        self.can.create_line((250, 30), (250, 45), fill='green', arrow='last',
                             width=4)
        self.can.create_rectangle((175, 45), (325, 65), width=4,
                                  state='disabled', outline='green')
        self.can.create_text((250, 55), state='disabled',
                             text="Connexion à MySQL")
        self.can.create_line((250, 65), (250, 80), fill='green', arrow='last',
                             width=4)
        self.can.create_polygon(
            [(200, 100), (250, 120), (300, 100), (250, 80)], width=4, fill='',
            outline="green")
        self.can.create_text((250, 100), state='disabled', text="Connecté ?")
        arrow_yes_1 = self.can.create_line(160, 100, 200, 100, arrow='first')
        rect_3 = self.can.create_rectangle((110, 90), (160, 110),
                                           state='disabled')
        self.can.create_text((135, 100), state='disabled', text='OUI')  # rect3
        arrow_3 = self.can.create_line((135, 110), (135, 125), arrow='last')
        arrow_no_1 = self.can.create_line((300, 100), (340, 100), arrow='last')
        rect_4 = self.can.create_rectangle((340, 90), (390, 110),
                                           state='disabled')
        self.can.create_text((365, 100), state='disabled', text='NON')  # rect4
        arrow_4 = self.can.create_line((365, 110), (365, 125), arrow='last')
        rect_4b = self.can.create_rectangle((305, 125), (425, 200),
                                            state='disabled')
        self.can.create_text((365, 135), state='disabled',
                             text="Quelque chose ne")  # rect4b line1
        self.can.create_text((365, 153), state='disabled',
                             text="va pas avec votre")  # rect4b line2
        self.can.create_text((365, 171), state='disabled',
                             text="nom d'utilisateur ou")  # rect4b line3
        self.can.create_text((365, 189), state='disabled',
                             text="votre mot de passe")  # rect4b line4
        rect_5 = self.can.create_rectangle((60, 125), (210, 165),
                                           state='disabled')
        self.can.create_text(135, 135, state='disabled',
                             text="Recherche si la base de")  # rect5 line1
        self.can.create_text(135, 153, state='disabled',
                             text="données 'Pur_Beurre' existe")  # rect5 line2
        arrow_5 = self.can.create_line(135, 165, 135, 180, arrow='last')

        polygon_2 = self.can.create_polygon([(85, 200), (135, 220), (185, 200),
                                             (135, 180)], fill='',
                                            outline='black')
        self.can.create_text(135, 200, text='bdd existe ?')  # polygon_2

        if self.text_cnx_mysql == "You are connected to MySQL":
            self.can.itemconfig(arrow_yes_1, fill='green', width=4)
            self.can.itemconfig(rect_3, outline='green', width=4)
            self.can.itemconfig(arrow_3, fill='green', width=4)
            self.can.itemconfig(rect_5, outline='green', width=4)
            self.can.itemconfig(arrow_5, fill='green', width=4)
            self.can.itemconfig(polygon_2, outline='green', width=4)
        elif self.text_cnx_mysql == """Something is wrong with your user name 
        or password""":
            self.can.itemconfig(arrow_no_1, fill='red', width=4)
            self.can.itemconfig(rect_4, outline='red', width=4)
            self.can.itemconfig(arrow_4, fill='red', width=4)
            self.can.itemconfig(rect_4b, outline='red', width=4)

        arrow_yes_2 = self.can.create_line((70, 200), (85, 200), arrow='first')
        rect_6 = self.can.create_rectangle((20, 190), (70, 210),
                                           state='disabled')
        self.can.create_text((45, 200), state='disabled', text='OUI')  # rect6
        arrow_6 = self.can.create_line((45, 210), (45, 310))
        arrow_6b = self.can.create_line((45, 310), (65, 310), arrow='last')

        arrow_no_2 = self.can.create_line((185, 200), (200, 200), arrow='last')
        rect_7 = self.can.create_rectangle((200, 190), (250, 210),
                                           state='disabled')
        self.can.create_text((225, 200), state='disabled', text='NON')  # rect7
        arrow_7 = self.can.create_line((225, 210), (225, 225), arrow='last')
        rect_8 = self.can.create_rectangle((180, 225), (270, 245),
                                           state='disabled')
        self.can.create_text((225, 235), state='disabled',
                             text='Création bdd')  # rect8
        arrow_8 = self.can.create_line((225, 245), (225, 255))
        polygon_3 = self.can.create_polygon([(175, 275), (225, 255),
                                             (275, 275), (225, 295)], fill='',
                                            outline='black')
        self.can.create_text(225, 275, text='bdd créée ?')  # polygon3
        arrow_yes_3 = self.can.create_line((160, 275), (175, 275),
                                           arrow='first')
        rect_9 = self.can.create_rectangle((110, 265), (160, 285),
                                           state='disabled')
        self.can.create_text((135, 275), state='disabled', text='OUI')  # rect9
        arrow_9 = self.can.create_line((135, 285), (135, 300), arrow='last')
        arrow_no_3 = self.can.create_line((275, 275), (290, 275), arrow='last')
        rect_10 = self.can.create_rectangle((290, 265), (340, 285),
                                            state='disabled')
        self.can.create_text((315, 275), state='disabled', text='NON')  #rect10
        arrow_12 = self.can.create_line((315, 285), (315, 300), arrow='last')
        rect_10b = self.can.create_rectangle((240, 300), (390, 340))
        self.can.create_text((315, 310), state='disabled',
                             text="Échec lors de la création")  # rect10b line1
        self.can.create_text((315, 328), state='disabled',
                             text="de la base de données.")  # rect10b line2
        rect_11 = self.can.create_rectangle((60, 300), (210, 320))
        self.can.create_text((135, 310), text='Connexion bdd')  # rect11
        arrow_10 = self.can.create_line((135, 320), (135, 335), arrow='last')
        rect_12 = self.can.create_rectangle((60, 335), (210, 375))
        self.can.create_text((135, 345), state='disabled',
                             text='Recherche la présence de')  # rect12 line1
        self.can.create_text((135, 365), state='disabled',
                             text="données de l'API dans la bdd")  # rect12 line2
        arrow_11 = self.can.create_line((135, 375), (135, 390), arrow='last')
        polygon_4 = self.can.create_polygon([(85, 410), (135, 430), (185, 410),
                                             (135, 390)], fill='',
                                            outline='black')
        self.can.create_text(135, 410, text='Données ?')  # polygon4
        arrow_yes_4 = self.can.create_line((70, 410), (85, 410), arrow='first')
        rect_13 = self.can.create_rectangle((20, 400), (70, 420))
        self.can.create_text((45, 410), text='OUI')  # rect13
        arrow_14 = self.can.create_line((45, 420), (45, 455), arrow='last')

        self.can.create_rectangle((10, 455), (80, 475))  # rect_14
        self.can.create_text((45, 465), text='Se connecter')  # text rect14
        arrow_no_4 = self.can.create_line((185, 410), (200, 410), arrow='last')
        rect_15 = self.can.create_rectangle((200, 400), (250, 420),
                                            state='disabled')
        self.can.create_text((225, 410), text='NON')  # text_rect15
        arrow_13 = self.can.create_line((225, 420), (225, 435), arrow='last')
        rect_16 = self.can.create_rectangle((150, 435), (300, 475))
        self.can.create_text((225, 445), text='Chargement des données')
        # rect16 line1
        self.can.create_text((225, 463), text='avant connexion')
        # rect16 line1

        if self.text_db_exist == "The PurBeurre database exists.":
            self.can.itemconfig(arrow_yes_2, fill='green', width=4)
            self.can.itemconfig(rect_6, outline='green', width=4)
            self.can.itemconfig(arrow_6, fill='green', width=4)
            self.can.itemconfig(arrow_6b, fill='green', width=4)
            self.can.itemconfig(rect_11, outline='green', width=4)
            self.can.itemconfig(arrow_10, fill='green', width=4)
            self.can.itemconfig(rect_12, outline='green', width=4)
            self.can.itemconfig(arrow_11, fill='green', width=4)
            self.can.itemconfig(polygon_4, outline='green', width=4)
        elif self.text_db_exist == "The PurBeurre Database does not exists.":
            self.can.itemconfig(arrow_no_2, fill='green', width=4)
            self.can.itemconfig(rect_7, outline='green', width=4)
            self.can.itemconfig(arrow_7, fill='green', width=4)
            self.can.itemconfig(rect_8, outline='green', width=4)
            self.can.itemconfig(arrow_8, fill='green', width=4)
            self.can.itemconfig(polygon_3, outline='green', width=4)

        if self.text_db_is_create == "The database is created.":
            self.can.itemconfig(arrow_yes_3, fill='green', width=4)
            self.can.itemconfig(rect_9, outline='green', width=4)
            self.can.itemconfig(arrow_9, fill='green', width=4)
            self.can.itemconfig(rect_11, outline='green', width=4)
            self.can.itemconfig(arrow_10, fill='green', width=4)
            self.can.itemconfig(rect_12, outline='green', width=4)
            self.can.itemconfig(arrow_11, fill='green', width=4)
            self.can.itemconfig(polygon_4, outline='green', width=4)
        elif self.text_db_is_create == "Failed creating database.":
            self.can.itemconfig(arrow_no_3, fill='red', width=4)
            self.can.itemconfig(rect_10, outline='red', width=4)
            self.can.itemconfig(arrow_12, fill='red', width=4)
            self.can.itemconfig(rect_10b, outline='red', width=4)

        if self.text_presence_data == "There is no data in database":
            self.can.itemconfig(arrow_no_4, fill='green', width=4)
            self.can.itemconfig(rect_15, outline='green', width=4)
            self.can.itemconfig(arrow_13, fill='green', width=4)
            self.can.itemconfig(rect_16, outline='green', width=4)
            text_button = "Chargement des données de l'API et connexion"

            button = Button(self.frame_steps, bd=2, text=text_button,
                            font=("Arial", 12), bg='#ADD0EC', fg=WHITE,
                            command=self.function_button)
            button.grid(row=13, sticky='ns', pady=5)
        else:
            self.can.itemconfig(arrow_yes_4, fill='green', width=4)
            self.can.itemconfig(rect_13, outline='green', width=4)
            self.can.itemconfig(arrow_14, fill='green', width=4)
            text_button = 'SE CONNECTER'
            button = Button(self.frame_steps, bd=2, text=text_button,
                            font=("Arial", 12), bg='#ADD0EC', fg=WHITE,
                            command=self.function_button)
            button.grid(row=13, sticky='ns', pady=5)
