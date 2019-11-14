from tkinter import Frame, Label, Canvas, Entry, Button, messagebox
import re
import hashlib
from config.config_view import (WHITE, TITLE_COLOR, LINE_COLOR, SUBTITLE_FONT,
                                BLACK, LABEL_FONT)


class ViewLogin:
    def __init__(self, root, controller):

        self.root = root
        self.controller = controller
        self.frame_login = Frame(root, bg='white')
        self.frame_login.grid(row=0, column=0, sticky='nesw',
                              padx=5, pady=5)
        # Entry for login
        self.message = None
        self.e_pseudo_login = None
        self.e_password_login = None
        # Entry for create an account
        self.message2 = None
        self.e_pseudo2 = None
        self.e_password2 = None
        self.info_password = None
        self.e_email = None

        self.create_widgets()

    @staticmethod
    def b_info_password():
        messagebox.showinfo("Informations pour la création du mot de passe",
                            "Le mot de passe doit comporter au moins :\n"
                            "- une minuscule\n"
                            "- une majuscule\n"
                            "- un chiffre\n"
                            "- un caractère spéciale.\n"
                            "Il doit contenir entre 6 et 15 caractères et "
                            "aucun caractère d'espace blanc n'est autorisé.\n",
                            default='ok', icon='info')

    def function_b_login(self):
        pseudo = self.e_pseudo_login.get()
        password = self.e_password_login.get()
        password_encryption = self.password_encryption(password)

        id_user = self.controller.verify_if_user_exists(pseudo,
                                                        password_encryption)
        # If the user does not exists: displays a message indicating that the
        # user does not exists (to log in or create an account)
        if not id_user:
            self.message['text'] = "L'utilisateur n'existe pas. "
            self.message['bg'] = "#F6BABA"
            self.message['fg'] = "red"
            self.e_pseudo_login.delete(0, 255)
            self.e_password_login.delete(0, 255)

        # Else (user exist)  open view pur Beurre welcome
        else:
            self.controller.controller_welcome_pur_beurre(id_user, pseudo)

    @staticmethod
    def checks_email(email):
        if email == '':
            return False
        else:
            motif = r"^[a-zA-Z0-9_\-]+(\.[a-zA-Z0-9_\-]+)*@[a-zA-Z0-9_\-]+" \
                    r"(\.[a-zA-Z0-9_\-]+)*(\.[a-zA-Z]{2,6})$"
            return re.match(motif, email) is not None

    @staticmethod
    def check_password(password):
        if password == '':
            return False
        else:
            motif = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\W)[a-zA-Z0-9\S]" \
                    r"{6,15}$"
            return re.match(motif, password) is not None

    @staticmethod
    def password_encryption(password2):
        password = hashlib.sha256(password2.encode())
        return password.hexdigest()

    def b_create_account(self):
        pseudo2 = self.e_pseudo2.get()
        password2 = self.e_password2.get()
        # check if the password is compliant
        check_password = self.check_password(password2)
        if not check_password:
            self.message2['text'] = "Mot de passe incorrect . "
            self.message2['bg'] = "#F6BABA"
            self.message2['fg'] = "red"
            self.e_password2.delete(0, 255)
            return
        # Hache le mot-de-passe
        password = self.password_encryption(password2)

        email = self.e_email.get()
        # check if the email is compliant
        check_email = self.checks_email(email)
        if not email or not check_email:
            self.message2['text'] = "Adresse mail incorrecte "
            self.message2['bg'] = "#F6BABA"
            self.message2['fg'] = "red"
            self.e_email.delete(0, 255)
            return
        # Check if the pseudo exists
        pseudo = self.controller.search_if_pseudo_exist(pseudo2)
        # If the user exists: displays a message indicating that the user
        # exists, and asks to choose another nickname
        if pseudo:
            self.message2['text'] = "Ce pseudo existe déjà. " \
                                    "Choississez un autre pseudo"
            self.message2['bg'] = "#F6BABA"
            self.message2['fg'] = "red"
            self.e_pseudo2.delete(0, 255)
            self.e_password2.delete(0, 255)
        # Else create a new user
        else:
            self.controller.create_user(pseudo2, password, email)

    def create_widgets(self):
        # create title
        title = Label(self.frame_login, text=" SE CONNECTER",
                      font=SUBTITLE_FONT, bg=WHITE, fg=TITLE_COLOR)
        title.grid(row=0, sticky='ns', pady=2, padx=10)

        # create line
        line1 = Canvas(self.frame_login, bd=0, highlightthickness=0,
                       bg=WHITE, height=20)
        line1.create_line((10, 10), (370, 10), fill=LINE_COLOR, width=2)
        line1.grid(row=1, sticky='w', padx=5, pady=20)

        # message : Erreur
        self.message = Label(self.frame_login, text=None, font=LABEL_FONT,
                             bg=WHITE, fg=BLACK)
        self.message.grid(row=2, sticky='ns', padx=20, pady=5)
        # create label Pseudo
        pseudo = Label(self.frame_login, text=" Pseudo : ",
                       font=LABEL_FONT, bg=WHITE, fg=BLACK)
        pseudo.grid(row=3, sticky='w', padx=20, pady=5)

        # create Entry Pseudo
        self.e_pseudo_login = Entry(self.frame_login, font=LABEL_FONT,
                                    bg='#E5E3E3')
        self.e_pseudo_login.grid(row=3, sticky='e', padx=2, pady=5)

        # create label Password
        password = Label(self.frame_login, text=" Mot de passe : ",
                         font=LABEL_FONT, bg=WHITE, fg=BLACK)
        password.grid(row=4, sticky='w', padx=20, pady=5)

        # create Entry Pseudo
        self.e_password_login = Entry(self.frame_login, font=LABEL_FONT,
                                      bg='#E5E3E3', show='*')
        self.e_password_login.grid(row=4, sticky='e', padx=2, pady=5)

        # create button LOG IN
        b_login = Button(self.frame_login, bd=2, text="Se connecter",
                         font=SUBTITLE_FONT, bg='#ADD0EC', fg=WHITE,
                         command=self.function_b_login)
        b_login.grid(row=5, sticky='ns', padx=15, pady=15)

        # create line
        line2 = Canvas(self.frame_login, bd=0, highlightthickness=0,
                       bg=WHITE, height=20)
        line2.create_line((10, 10), (370, 10), fill=LINE_COLOR, width=2)
        line2.grid(row=6, sticky='w')

        # create label New user
        subtitle = Label(self.frame_login, text=" Nouvel utilisateur ",
                         font=SUBTITLE_FONT, bg=WHITE, fg=TITLE_COLOR)
        subtitle.grid(row=7, sticky='ns', padx=2, pady=10)

        # message: this pseudo already exists, choose another pseudo
        self.message2 = Label(self.frame_login, text=None, font=LABEL_FONT,
                              bg=WHITE, fg=BLACK)
        self.message2.grid(row=8, sticky='ns', padx=20, pady=5)

        # create label Pseudo
        pseudo2 = Label(self.frame_login, text=" Pseudo : ",
                        font=LABEL_FONT, bg=WHITE, fg=BLACK)
        pseudo2.grid(row=9, sticky='w', padx=20, pady=5)

        # create Entry Pseudo
        self.e_pseudo2 = Entry(self.frame_login, font=LABEL_FONT, bg='#E5E3E3')
        self.e_pseudo2.grid(row=9, sticky='e', padx=2, pady=5)

        # create label Password
        password2 = Label(self.frame_login, text=" Mot de passe : ",
                          font=LABEL_FONT, bg=WHITE, fg=BLACK)
        password2.grid(row=10, sticky='w', padx=20, pady=5)

        # create Entry Pseudo
        self.e_password2 = Entry(self.frame_login, font=LABEL_FONT,
                                 bg='#E5E3E3', show='*')
        self. e_password2.grid(row=10, sticky='e', padx=2, pady=5)

        # create button info password
        self.info_password = Button(self.frame_login, bd=2, text=" ? ",
                                    font=("Arial", 8), bg='gray', fg=WHITE,
                                    command=self.b_info_password)
        self.info_password.grid(row=10, sticky='e')

        # create label Password
        email = Label(self.frame_login, text=" Email : ",
                      font=LABEL_FONT, bg=WHITE, fg=BLACK)
        email.grid(row=11, sticky='w', padx=20, pady=5)

        # create Entry Pseudo
        self.e_email = Entry(self.frame_login, font=LABEL_FONT, bg='#E5E3E3')
        self.e_email.grid(row=11, sticky='e', padx=2, pady=5)

        # create button create an account
        b_create_account = Button(self.frame_login, bd=2,
                                  text="Créer un compte",
                                  font=SUBTITLE_FONT, bg='#ADD0EC', fg=WHITE,
                                  command=self.b_create_account)
        b_create_account.grid(row=12, sticky='ns', padx=15, pady=15)
