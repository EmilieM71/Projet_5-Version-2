from tkinter import Frame, Label, Canvas, Button
from config.config_view import SUBTITLE_FONT, WHITE, TITLE_COLOR, LINE_COLOR


class ViewSteps:
    def __init__(self, root, controller, text1, text2, text3, text4):
        self.root = root
        self.controller = controller
        self.text_cnx_mysql = text1
        self.text_db_is_create = text2
        self.text_search_if_db_exist = text3
        self.text_step4 = text4
        self.frame_steps = Frame(root, bg=WHITE)
        self.frame_steps.grid(row=0, column=0, sticky='nesw', padx=10, pady=10)

        self.create_widgets()

    def function_button(self):
        pass

    def create_widgets(self):
        # create title
        title = Label(self.frame_steps,
                      text=" STEPS TO LAUNCH THE APPLICATION ",
                      font=SUBTITLE_FONT, bg=WHITE, fg=TITLE_COLOR)
        title.grid(row=0, column=0, sticky='ns', pady=5)

        # create line
        line1 = Canvas(self.frame_steps, bd=0, highlightthickness=0, bg=WHITE,
                       height=20)
        line1.create_line((10, 10), (370, 10), fill=LINE_COLOR, width=2)
        line1.grid(row=1, sticky='w')

        # create text
        canvas = Canvas(self.frame_steps, bg=WHITE, width=400, height=480)
        canvas.grid(row=2, sticky='ns')
        canvas.create_rectangle(125, 10, 285, 30, fill='', state='disabled',
                                width=4, outline='green')
        canvas.create_text(210, 20, state='disabled',
                           text=" Launch the application ")
        canvas.create_line((210, 30), (210, 50), fill='green', arrow='last',
                           width=4)
        canvas.create_rectangle(160, 50, 260, 90, fill='', state='disabled',
                                width=4, outline='green')
        canvas.create_text(210, 60, state='disabled',
                           text="Connection")
        canvas.create_text(210, 78, state='disabled',
                           text="to MySQL")

        canvas.create_line((210, 90), (210, 100), fill='green', width=4)
        line1_connect_mysql_ok = canvas.create_line((135, 100), (212, 100),
                                                    fill=LINE_COLOR)
        line1_pb_connect_mysql = canvas.create_line((208, 100), (285, 100),
                                                    fill=LINE_COLOR)
        line2_connect_mysql_ok = canvas.create_line((135, 100), (135, 120),
                                                    fill=LINE_COLOR,
                                                    arrow='last')
        line2_pb_connect_mysql = canvas.create_line((285, 100), (285, 120),
                                                    fill=LINE_COLOR,
                                                    arrow='last')
        rect_cnx_mysql_ok = canvas.create_rectangle(80, 120, 190, 160, fill='',
                                                    state='disabled')

        canvas.create_text(135, 130, state='disabled',
                           text="You are connected")
        canvas.create_text(135, 148, state='disabled',
                           text="to MySQL")

        rect_pb_cnx_mysql = canvas.create_rectangle(235, 120, 335, 245,
                                                    fill='', state='disabled')
        canvas.create_text(285, 130, text="You are not ")
        canvas.create_text(285, 148, text="connected to")
        canvas.create_text(285, 166, text="MySQL : ")
        canvas.create_text(285, 184, text="something is")
        canvas.create_text(285, 202, text="wrong with")
        canvas.create_text(285, 220, text="your user name")
        canvas.create_text(285, 238, text="or your password")

        line3_cnx_mysql_ok = canvas.create_line((135, 160), (135, 180),
                                                fill=LINE_COLOR, arrow='last')
        rect2_cnx_mysql_ok = canvas.create_rectangle(85, 180, 185, 240,
                                                     fill='', state='disabled')
        canvas.create_text(135, 190, state='disabled',
                           text="connection to")
        canvas.create_text(135, 208, state='disabled',
                           text="the 'PurBeurre'")
        canvas.create_text(135, 226, state='disabled',
                           text="database")
        line4_cnx_mysql_ok = canvas.create_line((135, 240), (135, 250),
                                                fill=LINE_COLOR)

        if self.text_cnx_mysql == "You are connected to MySQL":
            canvas.itemconfig(line1_connect_mysql_ok, fill="green", width=4)
            canvas.itemconfig(line2_connect_mysql_ok, fill="green", width=4)
            canvas.itemconfig(rect_cnx_mysql_ok, outline='green', width=4)
            canvas.itemconfig(line3_cnx_mysql_ok, fill="green", width=4)
            canvas.itemconfig(rect2_cnx_mysql_ok, outline='green', width=4)
            canvas.itemconfig(line4_cnx_mysql_ok, fill="green", width=4)
        elif self.text_cnx_mysql == "":
            canvas.itemconfig(line1_pb_connect_mysql, fill="red", width=4)
            canvas.itemconfig(line2_pb_connect_mysql, fill="red", width=4)
            canvas.itemconfig(rect_pb_cnx_mysql, fill="red", width=4)

        line1_db_exist = canvas.create_line((60, 250), (137, 250),
                                            fill=LINE_COLOR)
        line2_db_exist = canvas.create_line((60, 250), (60, 270),
                                            fill=LINE_COLOR, arrow='last')
        rect_db_exist = canvas.create_rectangle(10, 270, 110, 325, fill='',
                                                state='disabled')
        canvas.create_text(60, 280, state='disabled',
                           text="The 'PurBeurre'")
        canvas.create_text(60, 298, state='disabled',
                           text="database exists")

        line1_db_not_exist = canvas.create_line((133, 250), (210, 250),
                                                fill=LINE_COLOR)
        line2_db_not_exist = canvas.create_line((210, 250), (210, 270),
                                                fill=LINE_COLOR, arrow='last')
        rect_db_not_exist = canvas.create_rectangle(160, 270, 260, 325,
                                                    fill='', state='disabled')
        canvas.create_text(210, 280, state='disabled',
                           text="The 'PurBeurre'")
        canvas.create_text(210, 298, state='disabled',
                           text="database does")
        canvas.create_text(210, 316, state='disabled',
                           text="not exists.")
        line3_db_exist = canvas.create_line((60, 325), (60, 412),
                                            fill=LINE_COLOR)
        line4_db_exist = canvas.create_line((58, 410), (137, 410),
                                            fill=LINE_COLOR)
        line5_db_exist = canvas.create_line((135, 408), (135, 430),
                                            fill=LINE_COLOR, arrow='last')
        line3_db_not_exist = canvas.create_line((210, 325), (210, 335),
                                                fill=LINE_COLOR)
        line4_db_not_exist = canvas.create_line((210, 335), (210, 345),
                                                fill=LINE_COLOR, arrow='last')
        print("self.text_search_if_db_exist : ", self.text_search_if_db_exist)
        if self.text_search_if_db_exist == "The PurBeurre database exists.":
            canvas.itemconfig(line1_db_exist, fill='green', width=4)
            canvas.itemconfig(line2_db_exist, fill='green', width=4)
            canvas.itemconfig(rect_db_exist, outline='green', width=4)
            canvas.itemconfig(line3_db_exist, fill='green', width=4)
            canvas.itemconfig(line4_db_exist, fill='green', width=4)
            canvas.itemconfig(line5_db_exist, fill='green', width=4)
        elif self.text_search_if_db_exist == \
                "The PurBeurre Database does not exists.":
            canvas.itemconfig(line1_db_not_exist, fill='green', width=4)
            canvas.itemconfig(line2_db_not_exist, fill='green', width=4)
            canvas.itemconfig(rect_db_not_exist, outline='green', width=4)
            canvas.itemconfig(line3_db_not_exist, fill='green', width=4)
            canvas.itemconfig(line3_db_not_exist, fill='green', width=4)
            canvas.itemconfig(line4_db_not_exist, fill='green', width=4)

        line1_not_create_db = canvas.create_line((210, 335), (320, 335),
                                                 fill=LINE_COLOR)
        line2_not_create_db = canvas.create_line((320, 335), (320, 345),
                                                 fill=LINE_COLOR, arrow='last')
        rect_not_create_db = canvas.create_rectangle(270, 345, 370, 400,
                                                     fill='', state='disabled')
        canvas.create_text(320, 355, state='disabled',
                           text="Failed creating")
        canvas.create_text(320, 372, state='disabled',
                           text="database.")

        if self.text_db_is_create == "The 'PurBeurre' database is created":
            print("")
            canvas.itemconfig(line5_db_exist, fill='green', width=4)
        elif self.text_db_is_create == "Failed creating database.":
            canvas.itemconfig(line1_not_create_db, fill='red', width=4)
            canvas.itemconfig(line2_not_create_db, fill='red', width=4)
            canvas.itemconfig(rect_not_create_db, outline='red', width=4)

        rect_db_create = canvas.create_rectangle(160, 345, 260, 400, fill='',
                                                 state='disabled')
        canvas.create_text(210, 355, state='disabled',
                           text="The 'PurBeurre'")
        canvas.create_text(210, 373, state='disabled',
                           text="database is")
        canvas.create_text(210, 391, state='disabled',
                           text="created")

        if self.text_db_is_create == "The database is created":
            canvas.itemconfig(rect_db_create, outline='green', width=4)

        canvas.create_line((210, 400), (210, 410), fill=LINE_COLOR)
        canvas.create_line((135, 410), (210, 410), fill=LINE_COLOR)
        # canvas.create_line((135, 410), (135, 430), fill=LINE_COLOR,
        #                    arrow='last')
        canvas.create_rectangle(70, 430, 200, 470, fill='', state='disabled')
        canvas.create_text(135, 440, state='disabled',
                           text="You are connected")
        canvas.create_text(135, 458, state='disabled',
                           text="to 'PurBeurre' Database")
        button = Button(self.frame_steps, bd=2, text="OK",
                        font=("Arial", 10), bg='#ADD0EC', fg=WHITE,
                        command=self.function_button)
        button.grid(row=13, sticky='ns', pady=5)
