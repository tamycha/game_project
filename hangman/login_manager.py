class Login:
    def __init__(self,cor_id, cor_pw, attempts=3):
        self.cor_id=cor_id
        self.cor_pw=cor_pw
        self.attempts=attempts

    def login (self):
        for i in range(self.attempts):
            id=input("ID를 입력하세요: ")
            pw=input("PASSWORD를 입력하세요: ")

            if id==self.cor_id and pw==self.cor_pw:
                print("로그인이 되었습니다.")
                return True

            else:
                print( f"다시 시도하십시오. 남은 기회 {3-i}회")      
        print("로그인 3회 실패로 프로그램을 종료합니다.")
        return False