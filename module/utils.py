import os
import re
import sys

def clear():
    os.system('cls')

def is_allow_number(user_input):
    allow_pattern = r'^[1-6]{1}$'
    try:
        if re.match(allow_pattern, user_input):
            return True
        else:
            return False
        
    except:
        return False

def exit():
    print()
    print("[*] 게임을 종료 합니다.")
    sys.exit()