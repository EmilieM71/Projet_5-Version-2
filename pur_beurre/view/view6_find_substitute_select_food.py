from tkinter import Frame, Label, Canvas, Button, StringVar
from tkinter.ttk import Combobox
from config.config_view import (WHITE, TITLE_COLOR, LINE_COLOR, SUBTITLE_FONT,
                                LABEL_FONT)


class ViewSelectFood:
    def __init__(self, root, controller, list_food, cat_name, pseudo):

        self.root = root
        self.controller = controller
        self.list_food = list_food
        self.cat_name = cat_name
        self.pseudo = pseudo
        self.frame_select_food = Frame(root, bg='white')
        self.frame_select_food.grid(row=0, sticky='nesw', padx=5, pady=5)
        self.combo = None
        self.selected_food = None
        self.can = None
        self.info_food = None
        self.create_widgets()

    def choice_user(self, event):
        self.selected_food = str(self.combo.get())
        return self.selected_food

    def see_food_information(self):
        self.info_food = self.controller.displays_food_information(
            self.selected_food)
        self.create_news_widgets(self.info_food)
        return self.info_food

    def validate_food(self):
        self.info_food = self.controller.displays_food_information(
            self.selected_food)
        self.controller.substitute_research(self.pseudo, self.cat_name,
                                            self.info_food)

    def back_choice_cat(self):
        self.controller.controller_category(self.pseudo)

    def back_to_the_menu(self):
        pass

    def create_widgets(self):
        # create title
        title_line1 = Label(self.frame_select_food,
                            text=" BIENVENUE {} ".format(self.pseudo),
                            font=SUBTITLE_FONT, bg=WHITE, fg=TITLE_COLOR)
        title_line1.grid(row=0, sticky='ns', pady=5)

        # create title
        title = Label(self.frame_select_food, text="RECHERCHE D'UN SUBSTITUE",
                      font=SUBTITLE_FONT, bg=WHITE, fg=TITLE_COLOR)
        title.grid(row=1, sticky='w', pady=2)

        # Create Button Back to the menu
        button = Button(self.frame_select_food, bd=2,
                        text="MENU", font=LABEL_FONT,
                        bg='#ADD0EC', fg=WHITE, command=self.back_to_the_menu)
        button.grid(row=1, sticky='e')

        # create line
        line1 = Canvas(self.frame_select_food, bd=0,
                       highlightthickness=0, bg=WHITE, height=20)
        line1.create_line((10, 10), (400, 10), fill=LINE_COLOR, width=2)
        line1.grid(row=2, sticky='w')

        # create label category
        label_cat = Label(self.frame_select_food,
                          text=" Catégorie : {}".format(self.cat_name),
                          font=("Arial", 8), bg=WHITE, fg='gray')
        label_cat.grid(row=3, sticky='w', pady=5)

        # Create Button Back to the menu
        button = Button(self.frame_select_food, bd=2,
                        text="Modifier la catégorie", font=LABEL_FONT,
                        bg='#ADD0EC', fg=WHITE, command=self.back_choice_cat)
        button.grid(row=4, sticky='w')

        # create subtitle : Select a food
        subtitle = Label(self.frame_select_food,
                         text="Sélectionner un aliment : ", font=LABEL_FONT,
                         bg=WHITE, fg=TITLE_COLOR)
        subtitle.grid(row=5, sticky='w', pady=20)

        # Create combobox category
        control_variable = StringVar()
        self.combo = Combobox(self.frame_select_food, height=20,
                              textvariable=control_variable, width=40)
        self.combo.grid(row=6, sticky='w', padx=20)
        self.combo['values'] = self.list_food  # Values list
        self.combo.current(0)  # Choosing the current value
        # Action triggered by a selection in the list
        self.combo.bind('<<ComboboxSelected>>', self.choice_user)

        # Create Button Validate
        button = Button(self.frame_select_food, bd=2,
                        text="Voir", font=LABEL_FONT, fg=WHITE,
                        bg='#ADD0EC', command=self.see_food_information)
        button.grid(row=6, sticky='e')

        # Create Button Validate
        button = Button(self.frame_select_food, bd=2,
                        text="Valider", font=LABEL_FONT,
                        bg='#ADD0EC', fg=WHITE, command=self.validate_food)
        button.grid(row=7, sticky='e')

    def create_news_widgets(self, info):

        x0_col0 = 5
        x1_col0 = 205
        col_center_0 = ((x1_col0-x0_col0)/2)+x0_col0
        x0_col1 = x1_col0
        x1_col1 = 585
        col_center_1 = ((x1_col1 - x0_col1)/2)+x0_col1
        # create canvas
        self.can = Canvas(self.frame_select_food, bg=WHITE, width=970,
                          height=610)
        self.can.grid(row=0, column=1, rowspan=10, sticky='w', padx=5)

        self.can.create_rectangle((x0_col1, 5), (x1_col1, 25),
                                  state='disabled', disabledfill='#ADD0EC')
        self.can.create_text((col_center_1, 15), state='disabled',
                             text=" Aliment ", fill=WHITE)

        self.can.create_rectangle((x0_col0, 25), (x1_col0, 65),
                                  state='disabled', disabledfill='#ADD0EC')
        self.can.create_text((col_center_0, 45), state='disabled', text="Nom",
                             fill=WHITE)
        self.can.create_rectangle((x0_col1, 25), (x1_col1, 65),
                                  state='disabled')
        self.can.create_text((col_center_1, 45), state='disabled',
                             text=info[1], width=380)

        self.can.create_rectangle((x0_col0, 65), (x1_col0, 205),
                                  state='disabled', disabledfill='#ADD0EC')
        self.can.create_text((col_center_0, 135), state='disabled',
                             text="Liste d'ingrédients ",
                             fill=WHITE)
        self.can.create_rectangle((x0_col1, 65), (x1_col1, 205),
                                  state='disabled')
        self.can.create_text((col_center_1, 135), state='disabled',
                             text=info[4], width=380)

        self.can.create_rectangle((x0_col0, 205), (x1_col0, 225),
                                  state='disabled', disabledfill='#ADD0EC')
        self.can.create_text((col_center_0, 215), state='disabled', width=220,
                             text="Présence d'huile de palme", fill=WHITE)
        self.can.create_rectangle((x0_col1, 205), (x1_col1, 225))
        # create label value palm_oil
        if info[5] == '' or info[5] is None:
            self.can.create_text((col_center_1, 215), text="NON")
        else:
            self.can.create_text((col_center_1, 215), text="OUI", fill='red')

        self.can.create_rectangle((x0_col0, 225), (x1_col0, 265),
                                  state='disabled', disabledfill='#ADD0EC')
        text_allergen = "Substances provoquant allergies ou intolérances"
        self.can.create_text((col_center_0, 245), state='disabled', width=200,
                             text=text_allergen, fill=WHITE)
        self.can.create_rectangle((x0_col1, 225), (x1_col1, 265))
        self.can.create_text((col_center_1, 245), state='disabled',
                             text=info[6], width=350)
        self.can.create_rectangle((x0_col0, 265), (x1_col1, 285),
                                  state='disabled', disabledfill='#ADD0EC')
        text = "Informations nutritionnelles : Valeurs pour 100g ou 100ml"
        self.can.create_text(((x1_col1-x0_col0)/2, 275), state='disabled',
                             width=900, text=text, fill=WHITE)

        self.can.create_rectangle((x0_col0, 285), (x1_col0, 325),
                                  state='disabled', disabledfill='#ADD0EC')
        self.can.create_text((col_center_0, 305), state='disabled', width=100,
                             text="Energie", fill=WHITE)
        self.can.create_rectangle((x0_col1, 285), (x1_col1, 325))
        self.can.create_text((col_center_1, 295), text=info[7])
        self.can.create_text((col_center_1, 315), text=info[8])

        self.can.create_rectangle((x0_col0, 325), (x1_col0, 365),
                                  state='disabled', disabledfill='#ADD0EC')
        self.can.create_text((col_center_0, 335), state='disabled', width=350,
                             text="Matières grasses / Lipide", fill=WHITE)
        self.can.create_text((col_center_0, 355), state='disabled', width=350,
                             text="      dont acides gras saturés", fill=WHITE)
        self.can.create_rectangle((x0_col1, 325), (x1_col1, 365))
        self.can.create_text((col_center_1, 335), text=info[9])
        self.can.create_text((col_center_1, 355), text=info[10])

        self.can.create_rectangle((x0_col0, 365), (x1_col0, 405),
                                  state='disabled', disabledfill='#ADD0EC')
        self.can.create_text((col_center_0, 375), state='disabled', width=350,
                             text="Glucides                      ", fill=WHITE)
        self.can.create_text((col_center_0, 395), state='disabled', width=350,
                             text="      dont sucres", fill=WHITE)
        self.can.create_rectangle((x0_col1, 365), (x1_col1, 405))
        self.can.create_text((col_center_1, 375), text=info[11])
        self.can.create_text((col_center_1, 395), text=info[12])

        self.can.create_rectangle((x0_col0, 405), (x1_col0, 425),
                                  state='disabled', disabledfill='#ADD0EC')
        self.can.create_text((col_center_0, 415), state='disabled', width=350,
                             text="Protéines                     ", fill=WHITE)
        self.can.create_rectangle((x0_col1, 405), (x1_col1, 425))
        self.can.create_text((col_center_1, 415), text=info[13])

        self.can.create_rectangle((x0_col0, 425), (x1_col0, 465),
                                  state='disabled', disabledfill='#ADD0EC')
        self.can.create_text((col_center_0, 435), state='disabled', width=350,
                             text="Sel                           ", fill=WHITE)
        self.can.create_text((col_center_0, 455), state='disabled', width=350,
                             text="      sodium", fill=WHITE)
        self.can.create_rectangle((x0_col1, 425), (x1_col1, 465))
        self.can.create_text((col_center_1, 435), text=info[14])
        self.can.create_text((col_center_1, 455), text=info[15])

        self.can.create_rectangle((x0_col0, 465), (x1_col0, 515),
                                  state='disabled', disabledfill='#ADD0EC')
        self.can.create_text((col_center_0, 475), state='disabled', width=350,
                             text="Score nutritionnel - France   ", fill=WHITE)
        self.can.create_text((col_center_0, 500), state='disabled', width=350,
                             text="      nutriscore", fill=WHITE)
        self.can.create_rectangle((x0_col1, 465), (x1_col1, 515))
        self.can.create_text((col_center_1, 475), text=info[16])
        self.can.create_text((col_center_1, 500), text=info[2])  # logo nutriscore

        self.can.create_rectangle((x0_col0, 515), (x1_col0, 565),
                                  state='disabled', disabledfill='#ADD0EC')
        self.can.create_text((col_center_0, 540), state='disabled', width=350,
                             text="Groupe Nova                   ", fill=WHITE)
        self.can.create_rectangle((x0_col1, 515), (x1_col1, 565))
        self.can.create_text((col_center_1, 540), text="")
        # logo NOVA

        self.can.create_rectangle((x0_col0, 565), (x1_col0, 605),
                                  state='disabled', disabledfill='#ADD0EC')
        self.can.create_text((col_center_0, 585), state='disabled', width=350,
                             text="url OpenFoodFacts             ", fill=WHITE)
        self.can.create_rectangle((x0_col1, 565), (x1_col1, 605))
        self.can.create_text((col_center_1, 585), text=info[3], width=350)
