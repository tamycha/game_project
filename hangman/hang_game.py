import random
class HangGame:
    def __init__(self, life=10):
        self.words = ["python","apple","banana","school","computer"]
        self.target = random.choice(self.words)
        self.used=[]
        self.life=life
        self.slide =["_"]*len(self.target)

    def game(self):
        while True:
            print(self.target) #정답확인
            guess=input("알파벳 입력: ").lower()
            
            if not guess.isalpha() or len(guess)!=1:
                print("한 글자만 입력하시오.")
                continue 
            
            if guess in self.used:
                print("이미 입력한 글자입니다.")
                continue
            self.used.append(guess)
            found=False 


            for i in range (len(self.target)): 
                if self.target[i]==guess: 
                    self.slide[i]=guess
                    found = True

            if found==False: 
                    self.life-=1
            self.condition(guess) #condition을 실행하기 위해 필수임/ 나는 이걸 안부름.

            if "_" not in self.slide or self.life == 0:
                break


    def condition(self, guess):
        print()
        print(" ".join(self.slide))
        print(f"남은 기회: {self.life}")
        print(f"입력한 글자: {self.used}")

    def result(self):
        while True:
            if "_" not in self.slide:
                print("승리하셨습니다.")
                break
            elif self.life==0:
                print("패배하셨습니다.")
                print("정답:", self.target)
                break