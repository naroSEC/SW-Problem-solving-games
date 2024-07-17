import os
import sys
import random
import json
import copy
import re
import textwrap
from colorama import Fore, Style

def shuffle_dict(dic):
    items = list(dic.items())
    random.shuffle(items)

    return dict(items)

def start():
    exam_dict, input_TF = init()
    display(exam_dict, input_TF)

def display(exam_dict, input_TF):
    edit_exam_dict = copy.deepcopy(exam_dict)
    total_exam_count = len(exam_dict)
    correct_answer = 0
    cnt = 0

    for index, (key, value) in enumerate(exam_dict.items()):
        question = value["question"]
        vuln = value["vuln"]
        ft_positive = value["TFpositive"]
        gudie = value["guide"]
        cnt+=1

        clear()
        print(f"[ 총 문제: {total_exam_count} / {Fore.CYAN}남은 문제:{Fore.RESET} {total_exam_count - cnt} ]")
        print()
        print(f"[ {index + 1}번 문제 ]")
        print(f"아래 코드에는 어떠한 구현단계 보안 약점이 존재하는지 입력하시오.")
        print()
        print(question)
        print()

        user_input_vuln = input("* 보안약점 입력: ").strip().replace(" ", "").upper()

        if input_TF:
            user_input_ft = input("* 정/오탐 입력: ").strip().replace(" ", "").upper()
            convert_ft = ft_positive.strip()

        convert_vuln = vuln.replace(" ", "").upper()

        if (input_TF and convert_vuln == user_input_vuln and convert_ft == user_input_ft):
            del edit_exam_dict[key]
            correct_answer += 1
            print()
            print(f"{Fore.BLUE}[*] 정답입니다.{Fore.RESET}")
        
        elif (not input_TF and convert_vuln == user_input_vuln):
            del edit_exam_dict[key]
            correct_answer += 1
            print()
            print(f"{Fore.BLUE}[*] 정답입니다.{Fore.RESET}")

        else:
            print()
            print(f"{Fore.LIGHTRED_EX}[*] 오답입니다.{Fore.RESET}")
            print()
            print(f"{Fore.LIGHTYELLOW_EX}정답: {vuln}{Fore.RESET}")

        print(f"{Fore.GREEN}[*] 참고 보안약점 진단 가이드 페이지: {gudie} Page{Fore.RESET}")
        print()
        input("Please press Enter for the next question.: INPUT Enter ")

    clear()
    print(f"[ 총 문제 개수 : {total_exam_count}개\n맞춘 문제 개수 : {Fore.BLUE}{correct_answer}{Fore.RESET}개\n틀린 문제 개수 {Fore.LIGHTRED_EX}{total_exam_count - correct_answer}{Fore.RESET}개 ]")
    print()
    
    if (total_exam_count != correct_answer):
        user_input_regame = input("오답 풀이를 시작하시겠습니까? (Y/N): ").upper()

        if (user_input_regame == "Y" or not user_input_regame):
            display(edit_exam_dict, input_TF)
        else:
            pass

    else:
        print("모든 정답을 맞추셨습니다!")
        input("시작 화면으로 이동하니다. 엔터를 입력해주세요.")
        pass

def init():
    user_input_filter = setGameFilter()
    user_input_split = setGameSplit()
    shuffle_apply = setGameRandom()
    exam_dict = getExam()
    exam_dict = getFilter(exam_dict, user_input_filter)
    
    if user_input_filter == "3":
        input_TF = True
    else:
        input_TF = False

    if shuffle_apply:
        exam_dict = shuffle_dict(exam_dict)
    
    if user_input_split != "5":
        exam_dict = getSplit(exam_dict, user_input_split)

    return exam_dict, input_TF

def setGameFilter():
    while True:
        clear()
        print_mode = '''
        게임 모드를 선택해주세요.

        [1] 정탐 문제 풀기\n
        [2] 오탐 문제 풀기\n
        [3] 정/오탐 모든 문제 풀기
        '''
        print(textwrap.dedent(print_mode))

        user_input_filter = input("번호 입력: ").strip()
        if not validate(user_input_filter, 1):
            input(f"{Fore.LIGHTRED_EX}허용되지 않는 문자를 입력하셨습니다. 정확한 번호를 입력해주세요.{Fore.RESET}")
            continue
        else:
            return user_input_filter

def setGameSplit():
    while True:
        clear()
        print_split = '''
        문제는 총 4개의 세트가 준비되어 있습니다. 몇 번 세트 문제를 푸시겠습니까?

        [1] 1번 세트\n
        [2] 2번 세트\n
        [3] 3번 세트\n
        [4] 4번 세트\n
        [5] 모든 세트(문제 양이 많음)
        '''
        print(textwrap.dedent(print_split))
        user_input_split = input("번호 입력: ").strip()

        if not validate(user_input_split, 2):
            input(f"{Fore.LIGHTRED_EX}허용되지 않는 문자를 입력하셨습니다. 정확한 번호를 입력해주세요.{Fore.RESET}")
            continue
        else:
            return user_input_split

def setGameRandom():
    clear()
    user_input_shuffle_apply = input("문제 랜덤 모드를 적용하시겠습니까? y/n: ").strip().upper()
    if (user_input_shuffle_apply == "Y" or not user_input_shuffle_apply):
        return True
    else:
        return False

def getFilter(exam_dict, user_input_mode):
    if user_input_mode == "1":
        filtered_dict = {key: value for key, value in exam_dict.items() if value["TFpositive"] == "정탐"}

    elif user_input_mode == "2":
        filtered_dict = {key: value for key, value in exam_dict.items() if value["TFpositive"] == "오탐"}

    else:
        return exam_dict

    return filtered_dict

def getSplit(exam_dict, user_input_split):
    total_numbers = len(exam_dict)
    division = 4
    chunk_size = total_numbers // division
    remainder = total_numbers % division

    split_exam_dicts = []
    exam_dict_keys = list(exam_dict.keys())

    start_index = 0
    for i in range(division):
        end_index = start_index + chunk_size
        if i < remainder:
            end_index += 1
        split_dict  = {key: exam_dict[key] for key in exam_dict_keys[start_index:end_index]}
        split_exam_dicts.append(split_dict)
        start_index = end_index

    return split_exam_dicts[int(user_input_split) -1]

def validate(validate_number, validate_mode):
    allow_filter_pattern = r'^[1-3]{1}$'
    allow_split_pattern = r'^[1-5]{1}$'

    try:
        if re.match(allow_filter_pattern, validate_number) and validate_mode == 1:
            return True
        elif re.match(allow_split_pattern, validate_number) and validate_mode == 2:
            return True
        else:
            return False
        
    except:
        return False

def getPath(fileName):
    dirPath = os.path.dirname(os.path.abspath(__file__))
    filePath = os.path.join(dirPath, f"data6/{fileName}")

    return filePath

def getExam():
    filePath = getPath("exam.json")

    with open(filePath, 'r', encoding='utf-8') as file:
        parsed_question = json.load(file)

    return parsed_question

def clear():
    os.system('cls')

if __name__=="__main__":
    start()