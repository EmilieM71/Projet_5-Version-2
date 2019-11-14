from tkinter import Frame, Label, Canvas, Button, StringVar
from tkinter.ttk import Combobox
from config.config_view import (WHITE, TITLE_COLOR, LINE_COLOR, SUBTITLE_FONT,
                                LABEL_FONT)


class ViewSelectSubstitute:
    def __init__(self, root, controller, cat_name, list_substitute,
                 pseudo, info_food):

        self.root = root
        self.controller = controller
        self.cat_name = cat_name
        self.list_substitute = list_substitute
        self.frame_select_sub = Frame(root, bg='white')
        self.frame_select_sub.grid(row=0, column=0, sticky='nesw',
                                   padx=5, pady=5)
        self.pseudo = pseudo
        self.info_food = info_food
        self.combo = None
        self.selected_substitute = None
        self.can = None
        self.create_widgets()

    def choice_user(self, event):
        self.selected_substitute = str(self.combo.get())
        return self.selected_substitute

    def validate_substitute(self):
        print(self.selected_substitute)

    def back_choice_cat(self):
        # self.controller.controller_category()
        pass

    def back_choice_food(self):
        # self.controller.controller_category()
        pass

    def back_to_the_menu(self):
        pass

    def create_widgets(self):
        # create title
        title_line1 = Label(self.frame_select_sub,
                            text=" BIENVENUE {} ".format(self.pseudo),
                            font=SUBTITLE_FONT, bg=WHITE, fg=TITLE_COLOR)
        title_line1.grid(row=0, sticky='ns', pady=5)

        # create title
        title = Label(self.frame_select_sub, text="RECHERCHE D'UN SUBSTITUE",
                      font=SUBTITLE_FONT, bg=WHITE, fg=TITLE_COLOR)
        title.grid(row=1, sticky='w', pady=2)

        # Create Button Back to the menu
        button = Button(self.frame_select_sub, bd=2,
                        text="  Menu  ", font=SUBTITLE_FONT,
                        bg='#ADD0EC', fg=WHITE, command=self.back_to_the_menu)
        button.grid(row=1, sticky='e')

        # create line
        line1 = Canvas(self.frame_select_sub, bd=0,
                       highlightthickness=0, bg=WHITE, height=20)
        line1.create_line((10, 10), (400, 10), fill=LINE_COLOR, width=2)
        line1.grid(row=2, sticky='w')

        # create label category
        label_cat = Label(self.frame_select_sub,
                          text=" Category : {}".format(self.cat_name),
                          font=("Arial", 8), bg=WHITE, fg='gray')
        label_cat.grid(row=3, sticky='w', pady=5)

        # Create Button Back to the menu
        button = Button(self.frame_select_sub, bd=2,
                        text="Modifier la catégorie", font=LABEL_FONT,
                        bg='#ADD0EC', fg=WHITE, command=self.back_choice_cat)
        button.grid(row=4, sticky='w', padx=20)

        # create label food
        label_food = Label(self.frame_select_sub,
                           text=" Food : {}".format(self.info_food[1]),
                           font=("Arial", 8), bg=WHITE, fg='gray', width=60)
        label_food.grid(row=5, sticky='w', pady=5)

        # Create Button Back to the menu
        button = Button(self.frame_select_sub, bd=2,
                        text="Modifier l'aliment", font=LABEL_FONT,
                        bg='#ADD0EC', fg=WHITE, command=self.back_choice_food)
        button.grid(row=6, sticky='w', padx=20)

        # create line
        line2 = Canvas(self.frame_select_sub, bd=0,
                       highlightthickness=0, bg=WHITE, height=20)
        line2.create_line((10, 10), (400, 10), fill=LINE_COLOR, width=2)
        line2.grid(row=7, sticky='w')

        # create subtitle : Select a substitute
        subtitle = Label(self.frame_select_sub,
                         text=" Selectionner un substitue: : ",
                         font=SUBTITLE_FONT, bg=WHITE, fg=TITLE_COLOR)
        subtitle.grid(row=8, sticky='ns', pady=5)

        # Create combobox category
        list_substitute = []
        for substitute in self.list_substitute:
            print(substitute[0][1])
            list_substitute.append(substitute[0][1])
        control_variable = StringVar()
        self.combo = Combobox(self.frame_select_sub, height=20,
                              textvariable=control_variable, width=40)
        self.combo.grid(row=9, sticky='w', padx=20)
        self.combo['values'] = list_substitute  # Values list
        self.combo.current(0)  # Choosing the current value
        # Action triggered by a selection in the list
        self.combo.bind('<<ComboboxSelected>>', self.choice_user)

        # Create Button Validate
        button = Button(self.frame_select_sub, bd=2,
                        text="Comparer", font=SUBTITLE_FONT,
                        bg='#ADD0EC', fg=WHITE,
                        command=self.validate_substitute)
        button.grid(row=10, sticky='e', pady=20)

        # Create Button Validate
        button = Button(self.frame_select_sub, bd=2,
                        text="Enregistrer", font=SUBTITLE_FONT,
                        bg='#ADD0EC', fg=WHITE,
                        command=self.validate_substitute)
        button.grid(row=11, sticky='e', pady=20)

        x0_col0 = 5
        x1_col0 = 205
        col_center_0 = ((x1_col0 - x0_col0) / 2) + x0_col0
        x0_col1 = x1_col0
        x1_col1 = 585
        col_center_1 = ((x1_col1 - x0_col1) / 2) + x0_col1
        x0_col2 = x1_col1
        x1_col2 = 965
        col_center_2 = ((x1_col2 - x0_col2) / 2) + x0_col2
        # create canvas
        self.can = Canvas(self.frame_select_sub, bg=WHITE, width=970,
                          height=610)
        self.can.grid(row=0, column=1, rowspan=12, sticky='w', padx=5)

        self.can.create_rectangle((x0_col1, 5), (x1_col1, 25),
                                  state='disabled', disabledfill='#ADD0EC')
        self.can.create_text((col_center_1, 15), state='disabled',
                             text=" Aliment ", fill=WHITE)
        self.can.create_rectangle((x0_col2, 5), (x1_col2, 25),
                                  state='disabled', disabledfill='#ADD0EC')
        self.can.create_text((col_center_2, 15), state='disabled',
                             text=" Substitue ", fill=WHITE)

        self.can.create_rectangle((x0_col0, 25), (x1_col0, 65),
                                  state='disabled', disabledfill='#ADD0EC')
        self.can.create_text((col_center_0, 45), state='disabled', text="Nom",
                             fill=WHITE)
        self.can.create_rectangle((x0_col1, 25), (x1_col1, 65),
                                  state='disabled')
        self.can.create_text((col_center_1, 45), state='disabled',
                             text=self.info_food[1], width=380)
        self.can.create_rectangle((x0_col2, 25), (x1_col2, 65),
                                  state='disabled')
        self.can.create_text((col_center_2, 45), state='disabled', text="",
                             width=350)

        self.can.create_rectangle((x0_col0, 65), (x1_col0, 205),
                                  state='disabled', disabledfill='#ADD0EC')
        self.can.create_text((col_center_0, 135), state='disabled',
                             text="Liste d'ingrédients ",
                             fill=WHITE)
        self.can.create_rectangle((x0_col1, 65), (x1_col1, 205),
                                  state='disabled')
        self.can.create_text((col_center_1, 135), state='disabled',
                             text=self.info_food[4], width=380)
        self.can.create_rectangle((x0_col2, 65), (x1_col2, 205),
                                  state='disabled')
        self.can.create_text((col_center_2, 135), state='disabled', text="",
                             width=350)

        self.can.create_rectangle((x0_col0, 205), (x1_col0, 225),
                                  state='disabled', disabledfill='#ADD0EC')
        self.can.create_text((col_center_0, 215), state='disabled', width=220,
                             text="Présence d'huile de palme", fill=WHITE)
        self.can.create_rectangle((x0_col1, 205), (x1_col1, 225))
        # create label value palm_oil
        if self.info_food[5] == '' or self.info_food[5] is None:
            self.can.create_text((col_center_1, 215), text="NON")
        else:
            self.can.create_text((col_center_1, 215), text="OUI", fill='red')
        self.can.create_rectangle((x0_col2, 205), (x1_col2, 225))
        self.can.create_text((col_center_2, 215), text="", width=160)

        self.can.create_rectangle((x0_col0, 225), (x1_col0, 265),
                                  state='disabled', disabledfill='#ADD0EC')
        text_allergen = "Substances provoquant allergies ou intolérances"
        self.can.create_text((col_center_0, 245), state='disabled', width=200,
                             text=text_allergen, fill=WHITE)
        self.can.create_rectangle((x0_col1, 225), (x1_col1, 265))
        self.can.create_text((col_center_1, 245), state='disabled',
                             text=self.info_food[6], width=350)
        self.can.create_rectangle((x0_col2, 225), (x1_col2, 265))
        self.can.create_text((col_center_2, 245), text="", width=350)

        self.can.create_rectangle((x0_col0, 265), (x1_col2, 285),
                                  state='disabled', disabledfill='#ADD0EC')
        text = "Informations nutritionnelles : Valeurs pour 100g ou 100ml"
        self.can.create_text((col_center_1, 275), state='disabled', width=900,
                             text=text, fill=WHITE)

        self.can.create_rectangle((x0_col0, 285), (x1_col0, 325),
                                  state='disabled', disabledfill='#ADD0EC')
        self.can.create_text((col_center_0, 305), state='disabled', width=100,
                             text="Energie", fill=WHITE)
        self.can.create_rectangle((x0_col1, 285), (x1_col1, 325))
        self.can.create_text((col_center_1, 295), text=self.info_food[7])
        self.can.create_text((col_center_1, 315), text=self.info_food[8])
        self.can.create_rectangle((x0_col2, 285), (x1_col2, 325))
        self.can.create_text((col_center_2, 295), text="", width=160)
        self.can.create_text((col_center_2, 315), text="", width=160)

        self.can.create_rectangle((x0_col0, 325), (x1_col0, 365),
                                  state='disabled', disabledfill='#ADD0EC')
        self.can.create_text((col_center_0, 335), state='disabled', width=350,
                             text="Matières grasses / Lipide", fill=WHITE)
        self.can.create_text((col_center_0, 355), state='disabled', width=350,
                             text="      dont acides gras saturés", fill=WHITE)
        self.can.create_rectangle((x0_col1, 325), (x1_col1, 365))
        self.can.create_text((col_center_1, 335), text=self.info_food[9])
        self.can.create_text((col_center_1, 355), text=self.info_food[10])
        self.can.create_rectangle((x0_col2, 325), (x1_col2, 365))
        self.can.create_text((col_center_2, 335), text="", width=160)
        self.can.create_text((col_center_2, 355), text="", width=160)

        self.can.create_rectangle((x0_col0, 365), (x1_col0, 405),
                                  state='disabled', disabledfill='#ADD0EC')
        self.can.create_text((col_center_0, 375), state='disabled', width=350,
                             text="Glucides                      ", fill=WHITE)
        self.can.create_text((col_center_0, 395), state='disabled', width=350,
                             text="      dont sucres", fill=WHITE)
        self.can.create_rectangle((x0_col1, 365), (x1_col1, 405))
        self.can.create_text((col_center_1, 375), text=self.info_food[11])
        self.can.create_text((col_center_1, 395), text=self.info_food[12])
        self.can.create_rectangle((x0_col2, 365), (x1_col2, 405))
        self.can.create_text((col_center_2, 375), text="")
        self.can.create_text((col_center_2, 395), text="")

        self.can.create_rectangle((x0_col0, 405), (x1_col0, 425),
                                  state='disabled', disabledfill='#ADD0EC')
        self.can.create_text((col_center_0, 415), state='disabled', width=350,
                             text="Protéines                     ", fill=WHITE)
        self.can.create_rectangle((x0_col1, 405), (x1_col1, 425))
        self.can.create_text((col_center_1, 415), text=self.info_food[13])
        self.can.create_rectangle((x0_col2, 405), (x1_col2, 425))
        self.can.create_text((col_center_2, 415), text="")

        self.can.create_rectangle((x0_col0, 425), (x1_col0, 465),
                                  state='disabled', disabledfill='#ADD0EC')
        self.can.create_text((col_center_0, 435), state='disabled', width=350,
                             text="Sel                           ", fill=WHITE)
        self.can.create_text((col_center_0, 455), state='disabled', width=350,
                             text="      sodium", fill=WHITE)
        self.can.create_rectangle((x0_col1, 425), (x1_col1, 465))
        self.can.create_text((col_center_1, 435), text=self.info_food[14])
        self.can.create_text((col_center_1, 455), text=self.info_food[15])
        self.can.create_rectangle((x0_col2, 425), (x1_col2, 465))
        self.can.create_text((col_center_2, 435), text="")
        self.can.create_text((col_center_2, 455), text="")

        self.can.create_rectangle((x0_col0, 465), (x1_col0, 515),
                                  state='disabled', disabledfill='#ADD0EC')
        self.can.create_text((col_center_0, 475), state='disabled', width=350,
                             text="Score nutritionnel - France   ", fill=WHITE)
        self.can.create_text((col_center_0, 500), state='disabled', width=350,
                             text="      nutriscore", fill=WHITE)
        self.can.create_rectangle((x0_col1, 465), (x1_col1, 515))
        self.can.create_text((col_center_1, 475), text=self.info_food[16])
        self.can.create_text((col_center_1, 500),
                             text=self.info_food[2])  # logo nutriscore
        self.can.create_rectangle((x0_col2, 465), (x1_col2, 515))
        self.can.create_text((col_center_2, 475), text="")
        self.can.create_text((col_center_2, 500), text="")  # logo nutriscore

        self.can.create_rectangle((x0_col0, 515), (x1_col0, 565),
                                  state='disabled', disabledfill='#ADD0EC')
        self.can.create_text((col_center_0, 540), state='disabled', width=350,
                             text="Groupe Nova                   ", fill=WHITE)
        self.can.create_rectangle((x0_col1, 515), (x1_col1, 565))
        self.can.create_text((col_center_1, 540), text="")
        # logo NOVA
        self.can.create_rectangle((x0_col2, 515), (x1_col2, 565))
        self.can.create_text((col_center_2, 540), text="")
        # logo NOVA

        self.can.create_rectangle((x0_col0, 565), (x1_col0, 605),
                                  state='disabled', disabledfill='#ADD0EC')
        self.can.create_text((col_center_0, 585), state='disabled', width=350,
                             text="url OpenFoodFacts             ", fill=WHITE)
        self.can.create_rectangle((x0_col1, 565), (x1_col1, 605))
        self.can.create_text((col_center_1, 585), text=self.info_food[3],
                             width=350)
        self.can.create_rectangle((x0_col2, 565), (x1_col2, 605))
        self.can.create_text((col_center_2, 585), text="", width=350)
