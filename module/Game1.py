import os
import sys
from colorama import Fore, Style

def start():
    examDic = init()
    display(examDic)

def display(examDic):
    editExamDic = examDic.copy()
    totalExam = len(examDic)
    correctAnswer = 0
    cnt = 0

    for index, (key, value) in enumerate(examDic.items()):
        cnt += 1
        clear()
        print(f"[ 총 문제: {totalExam} / {Fore.CYAN}남은 문제:{Fore.RESET} {totalExam - cnt} ]")
        print()
        print(f"[ {index + 1}번 문제 ]")
        print(f"설계 항목 {Fore.LIGHTMAGENTA_EX}{key}{Fore.RESET}에 해당하는 보안약점을 입력하세요.")
        print()

        count = len(value)

        while True:
            userInputAnswers = []
            if (count > 1):
                print(f"정답 {count}개\n각각 입력해주세요.")
                print()
                for i in range(count):
                    userInputAnswers.append(input(f"{i+1}번 째 정답 입력: ").strip().replace(" ", "").upper())
                break

            else:
                print(f"정답 {count}개")
                userInputAnswers.append(input("정답 입력: ").strip().replace(" ", "").upper())
                break
        
        if(len(set(userInputAnswers) & set(value)) == count):
            del editExamDic[key]
            correctAnswer += 1
            print()
            print(f"{Fore.BLUE}[*] 정답입니다.{Fore.RESET}")
            
        else:
            print()
            print(f"{Fore.LIGHTRED_EX}[*] 오답입니다.{Fore.RESET}")
            print()
            print(f"{Fore.LIGHTYELLOW_EX}정답: {value}{Fore.RESET}")
        
        print()
        input("Please press Enter for the next question.: INPUT Enter ")

    clear()
    print(f"[ 총 문제 개수 : {totalExam}개\n맞춘 문제 개수 : {Fore.BLUE}{correctAnswer}{Fore.RESET}개\n틀린 문제 개수 {Fore.LIGHTRED_EX}{totalExam - correctAnswer}{Fore.RESET}개 ]")
    print()
    
    if (totalExam != correctAnswer):
        reGame = input("오답 풀이를 시작하시겠습니까? (Y/N): ").upper()

        if (reGame == "Y" or not reGame):
            display(editExamDic)
        else:
            pass

    else:
        print("모든 정답을 맞추셨습니다!")
        input("시작화면으로 이동합니다. 엔터를 입력해주세요.")
        pass

def init():
    questionList = getQuestion()
    answerList = getAnswer()

    examDic = {}
    for index, value in enumerate(questionList):
        examDic[questionList[index]] = answerList[index]
    
    return examDic

def getPath(fileName):
    dirPath = os.path.dirname(os.path.abspath(__file__))
    filePath = os.path.join(dirPath, f"data1/{fileName}")

    return filePath

def getQuestion():
    filePath = getPath("문제.txt")

    with open(filePath, 'r', encoding='utf-8') as file:
        questionList = [line.strip() for line in file.readlines()]
    
    return questionList


def getAnswer():
    filePath = getPath("정답.txt")

    with open(filePath, 'r', encoding='utf-8') as file:
        answerList = [line.strip() for line in file.readlines()]
        convertToIndividualList = [[answer.replace(" ", "").upper()] for answer in answerList]

        convertedAnswerList = []
        for item in convertToIndividualList:
            sublist = item[0].split('/')
            if len(sublist) > 1:
                convertedAnswerList.append(sublist)
            else:
                convertedAnswerList.append(item)

    return convertedAnswerList

def clear():
    os.system('cls')

if __name__=="__main__":
    start()