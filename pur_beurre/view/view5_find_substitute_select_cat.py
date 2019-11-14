from tkinter import Frame, Label, Canvas, Button, StringVar
from tkinter.ttk import Combobox
from config.config_view import (WHITE, TITLE_COLOR, LINE_COLOR, SUBTITLE_FONT,
                                LABEL_FONT)
from config.config_db import CATEGORY


class ViewSelectCategory:
    def __init__(self, root, controller, pseudo):

        self.root = root
        self.root.geometry("1400x620-20+20")
        self.controller = controller
        self.frame_select_cat = Frame(root, bg='white')
        self.frame_select_cat.grid(row=0, column=0, sticky='nesw', padx=5,
                                   pady=5)
        self.pseudo = pseudo
        self.combo = None
        self.selected_category = None
        self.create_widgets()

    def choice_user(self, event):
        self.selected_category = str(self.combo.get())
        return self.selected_category

    def validate_category(self):
        self.controller.id_selected_category(self.selected_category,
                                             self.pseudo)

    def back_to_the_menu(self):
        pass

    def create_widgets(self):
        # create title
        title_line1 = Label(self.frame_select_cat,
                            text=" BIENVENUE {} ".format(self.pseudo),
                            font=SUBTITLE_FONT, bg=WHITE, fg=TITLE_COLOR)
        title_line1.grid(row=0, sticky='ns', pady=5)

        # create title
        title = Label(self.frame_select_cat, text="RECHERCHE D'UN SUBSTITUE",
                      font=SUBTITLE_FONT, bg=WHITE, fg=TITLE_COLOR)
        title.grid(row=1, sticky='w', pady=2)

        # create line
        line1 = Canvas(self.frame_select_cat, bd=0,
                       highlightthickness=0, bg=WHITE, height=20)
        line1.create_line((10, 10), (400, 10), fill=LINE_COLOR, width=2)
        line1.grid(row=2, sticky='w')

        # create subtitle : Select a category:
        subtitle = Label(self.frame_select_cat,
                         text=" Sélectionner une catégorie : ",
                         font=("Arial", 10), bg=WHITE, fg=TITLE_COLOR)
        subtitle.grid(row=3, sticky='w', pady=2, padx=20)

        # Create combobox category
        control_variable = StringVar()
        self.combo = Combobox(self.frame_select_cat, height=25,
                              textvariable=control_variable, width=35)
        self.combo.grid(row=4, sticky='w', padx=20)
        self.combo['values'] = CATEGORY 	# Values list
        self.combo.current(0)  # Choosing the current value
        # Action triggered by a selection in the list
        self.combo.bind('<<ComboboxSelected>>', self.choice_user)

        # Create Button Validate
        button = Button(self.frame_select_cat, bd=2,
                        text="VALIDER", font=LABEL_FONT,
                        bg='#ADD0EC', fg=WHITE, command=self.validate_category)
        button.grid(row=4, sticky='e', pady=20)

        # Create Button Back to the menu
        button = Button(self.frame_select_cat, bd=2,
                        text="MENU", font=LABEL_FONT,
                        bg='#ADD0EC', fg=WHITE, command=self.back_to_the_menu)
        button.grid(row=1, sticky='e')
