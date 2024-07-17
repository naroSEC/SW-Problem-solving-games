import os
import sys
import random
import json
import copy
from colorama import Fore, Style

def start():
    exam_dict = init()
    display(exam_dict)

def display(exam_dict):
    clear()
    user_input_shuffle_apply = input("문제 랜덤 모드를 적용하시겠습니까? y/n: ").strip().upper()
    if (user_input_shuffle_apply == "Y" or not user_input_shuffle_apply):
        exam_dict = shuffle_dict(exam_dict)

    edit_exam_dict = copy.deepcopy(exam_dict)
    total_exam_count = len(exam_dict)
    correct_count = 0
    cnt = 0
    
    for index, (question, answer) in enumerate(exam_dict.items()):
        cnt += 1
        clear()
        print(f"[ 총 문제: {total_exam_count} / {Fore.CYAN}남은 문제:{Fore.RESET} {total_exam_count - cnt} ]")
        print()
        print(f"[ {index + 1}번 문제 ]")
        print(f"구현단계 보안약점 {Fore.YELLOW}{question}{Fore.RESET}에 해당하는 대분류 항목명을 작성하시오.")
        print()

        while True:
            user_input_answer = input(f"정답 입력: ").strip().replace(" ", "").upper()
            break
        
        temp_answer = answer.strip().replace(" ", "").upper()

        if temp_answer == user_input_answer:
            del edit_exam_dict[question]
            correct_count+=1
            print()
            print(f"{Fore.BLUE}[*] 정답입니다.{Fore.RESET}")
        else:
            print()
            print(f"{Fore.LIGHTRED_EX}[*] 오답입니다.{Fore.RESET}")
            print()
            print(f"{Fore.LIGHTYELLOW_EX}정답: {answer}{Fore.RESET}")

        input("Please press Enter for the next question.: INPUT Enter ")

    clear()
    print(f"[ 총 문제 개수 : {total_exam_count}개\n맞춘 문제 개수 : {Fore.BLUE}{correct_count}{Fore.RESET}개\n틀린 문제 개수 {Fore.LIGHTRED_EX}{total_exam_count - correct_count}{Fore.RESET}개 ]")
    print()
    
    if (total_exam_count != correct_count):
        user_input_regame = input("오답 풀이를 시작하시겠습니까? (Y/N): ").upper()

        if (user_input_regame == "Y" or not user_input_regame):
            display(edit_exam_dict)
        else:
            pass

    else:
        print("모든 정답을 맞추셨습니다!")
        input("시작 화면으로 이동하니다. 엔터를 입력해주세요.")
        pass

def init():
    parsed_question = getExam()
    exam_dic = {item: key for key, value in parsed_question.items() for item in value}
    
    return exam_dic

def shuffle_dict(dic):
    items = list(dic.items())
    random.shuffle(items)

    return dict(items)

def getExam():
    filePath = getPath("구현단계.json")

    with open(filePath, 'r', encoding='utf-8') as file:
        parsed_question = json.load(file)

    return parsed_question


def getPath(fileName):
    dirPath = os.path.dirname(os.path.abspath(__file__))
    filePath = os.path.join(dirPath, f"data4/{fileName}")

    return filePath

def clear():
    os.system('cls')

if __name__=="__main__":
    start()