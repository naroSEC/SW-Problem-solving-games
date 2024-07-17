from module import Game1
from module import Game2
from module import Game3
from module import Game4
from module import Game5
from module import Game6

def start(user_input_select):
    if user_input_select == "1":
        Game1.start()
    if user_input_select == "2":
        Game2.start()
    if user_input_select == "3":
        Game3.start()
    if user_input_select == "4":
        Game4.start()
    if user_input_select == "5":
        Game5.start()
    if user_input_select == "6":
        Game6.start()