from .set import ADMIN_ID, ADMIN_PASSWORD
from .login_manager import Login
from .hang_game import HangGame

class App:
    def __init__(self):
        self.login_manager= Login(ADMIN_ID, ADMIN_PASSWORD)

    def print_menu(self):
        print()
        print("1. 게임 시작")
        print("2. 랭킹 보기")
        print("3. 게임 종료")

    def input_number(self):
        num = int(input("메뉴를 선택하세요."))
        while True:
                if type(num)==int: #이건 단순히 숫자 아닌 걸 걸러내기위한 쓴 while문
                     return num
                else:
                    print("숫자만 입력하세요.")

    def run(self):
        if not self.login_manager.login():
            return
       
    
        while True:
            self.print_menu()
            num=self.input_number()
            if num == 1:
                game = HangGame()
                game.game() #게임을 불러오겠다. #게임 자체를 실행시키는 단축키가 없어서 game.game() 추가     
            elif num == 2:
                pass        
            elif num == 3:
                print("프로그램을 종료합니다.")
                break    
            else:
                print("잘못된 메뉴입니다.") 