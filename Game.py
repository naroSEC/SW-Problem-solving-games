from module import utils
from module import service
from colorama import Fore, Style
import textwrap

def game_start():
    while True:
        utils.clear()
        init_print = f'''
        [{Fore.LIGHTYELLOW_EX} SW 보안약점 진단원 게임 Start! {Fore.RESET}]
        
        1. (설계단계) 보안 설계 기준 - 보안 약점 제거 기준 매핑 문제\n
        2. (구현단계) 취약한 소스코드 - 보안 약점 항목명 매핑 문제\n
        3. (설계단계) 대분류 항목 - 보안 설계 기준 매핑 문제\n
        4. (구현단계) 대분류 항목 - 보안 약점 제거 기준 매핑 문제\n
        5. 객관식, 단답형 대비 용어 부록 문제\n
        6. (구현단계) 취약한 소스코드 - 보안 약점 항목명 매핑 문제(심화버전)

        {Fore.RED}exit{Fore.RESET} - 게임종료\n
        '''
        print(textwrap.dedent(init_print))
        print("학습할 문제 풀이 게임 번호를 입력해주세요.")
        user_input_select = input("입력: ").strip()

        if utils.is_allow_number(user_input_select):
            service.start(user_input_select)
        else:
            if user_input_select == "exit":
                utils.exit()
            print()
            input(f"{Fore.LIGHTRED_EX}허용되지 않는 문자를 입력하셨습니다. 문제 번호만 입력해주세요.{Fore.RESET}")
            pass


if __name__ == "__main__":
    game_start()
