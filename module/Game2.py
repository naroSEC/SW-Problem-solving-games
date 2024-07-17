import os
import sys
import random
from colorama import Fore, Style

def shuffle_dict(dic):
    items = list(dic.items())
    random.shuffle(items)

    return dict(items)

def start():
    exam_dict = init()
    display(exam_dict)

def display(exam_dict):
    clear()
    user_input_shuffle_apply = input("문제 랜덤 모드를 적용하시겠습니까? y/n: ").strip().upper()
    if (user_input_shuffle_apply == "Y" or not user_input_shuffle_apply):
        exam_dict = shuffle_dict(exam_dict)

    edit_exam_dict = exam_dict.copy()
    total_exam_count = len(exam_dict)
    correct_answer = 0
    cnt = 0

    for index, (key, value) in enumerate(exam_dict.items()):
        cnt+=1
        clear()
        print(f"[ 총 문제: {total_exam_count} / {Fore.CYAN}남은 문제:{Fore.RESET} {total_exam_count - cnt} ]")
        print()
        print(f"[ {index + 1}번 문제 ]")
        print(f"아래 코드에는 어떠한 구현단계 보안 약점이 존재하는지 입력하시오.")
        print()
        print(value["question"])
        print()

        while True:
            user_input_answer = input("정답 입력: ").strip().replace(" ", "").upper()
            break
        
        answer = value["answer"].replace(" ", "").upper()

        if(user_input_answer == answer):
            del edit_exam_dict[key]
            correct_answer += 1
            print()
            print(f"{Fore.BLUE}[*] 정답입니다.{Fore.RESET}")
            
        else:
            print()
            print(f"{Fore.LIGHTRED_EX}[*] 오답입니다.{Fore.RESET}")
            print()
            print(f"{Fore.LIGHTYELLOW_EX}정답: {value['answer']}{Fore.RESET}")
        
        print()
        input("Please press Enter for the next question.: INPUT Enter ")

    clear()
    print(f"[ 총 문제 개수 : {total_exam_count}개\n맞춘 문제 개수 : {Fore.BLUE}{correct_answer}{Fore.RESET}개\n틀린 문제 개수 {Fore.LIGHTRED_EX}{total_exam_count - correct_answer}{Fore.RESET}개 ]")
    print()
    
    if (total_exam_count != correct_answer):
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
    question_list = getQuestion()
    answer_list = getAnswer()

    exam_dict = {}
    for index, value in enumerate(question_list):
        exam_dict[index+1] = {
            "question": question_list[index],
            "answer": answer_list[index]
        }
    
    return exam_dict

def getPath(fileName):
    dirPath = os.path.dirname(os.path.abspath(__file__))
    filePath = os.path.join(dirPath, f"data2/{fileName}")

    return filePath

def getQuestion():
    filePath = getPath("문제.txt")

    with open(filePath, 'r', encoding='utf-8') as file:
        questions = file.read()
        questions_split = questions.split('======================================================')
        question_list = [question.strip() for question in questions_split if question.strip()]

    return question_list

def getAnswer():
    filePath = getPath("정답.txt")

    with open(filePath, 'r', encoding='utf-8') as file:
        answer_list = [answer.strip() for answer in file.readlines()]
    
    return answer_list

def clear():
    os.system('cls')

if __name__=="__main__":
    start()