from tkinter import Frame, Label, Canvas, Button
from config.config_view import WHITE, TITLE_COLOR, LINE_COLOR, SUBTITLE_FONT


class ViewPurBeurreWelcome:
    def __init__(self, root, controller, pseudo):

        self.root = root
        self.controller = controller
        self.pseudo = pseudo
        self.frame_pur_beurre_welcome = Frame(root, bg='white')
        self.frame_pur_beurre_welcome.grid(row=0, column=0, sticky='nesw',
                                           padx=5, pady=5)
        self.create_widgets()

    def find_substitute(self):
        self.controller.controller_category(self.pseudo)

    def review_substitute(self):
        pass

    def create_widgets(self):
        # create title
        title_line1 = Label(self.frame_pur_beurre_welcome,
                            text=" BIENVENUE {} ".format(self.pseudo),
                            font=SUBTITLE_FONT, bg=WHITE, fg=TITLE_COLOR)
        title_line1.grid(row=0, sticky='ns', pady=5)

        title_line2 = Label(self.frame_pur_beurre_welcome,
                            text=" DANS L'APPLICATION PUR BEURRE ",
                            font=SUBTITLE_FONT, bg=WHITE, fg=TITLE_COLOR)
        title_line2.grid(row=1, sticky='ns', pady=5)

        # create line
        line1 = Canvas(self.frame_pur_beurre_welcome, bd=0,
                       highlightthickness=0, bg=WHITE, height=20)
        line1.create_line((10, 10), (400, 10), fill=LINE_COLOR, width=2)
        line1.grid(row=2, sticky='w')

        # What do you want to do?
        label = Label(self.frame_pur_beurre_welcome,
                      text="Que voulez-vous faire ?", font=SUBTITLE_FONT,
                      bg=WHITE, fg=TITLE_COLOR)
        label.grid(row=3, sticky='w', pady=20, padx=20)

        #   1. Find a substitute.
        button1 = Button(self.frame_pur_beurre_welcome, bd=2,
                         text="Rechercher un substitue", font=SUBTITLE_FONT,
                         bg='#ADD0EC', fg=WHITE, command=self.find_substitute)
        button1.grid(row=4, sticky='ns', pady=20)

        #   2. Review substitutes.
        button2 = Button(self.frame_pur_beurre_welcome, bd=2,
                         text="Voir vos substitues", font=SUBTITLE_FONT,
                         bg='#ADD0EC', fg=WHITE,
                         command=self.review_substitute)
        button2.grid(row=5, sticky='ns', pady=20)
