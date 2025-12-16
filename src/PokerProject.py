import random
import time
import os
import datetime

# --- 색상 코드 ---
class Color:
    RED = '\033[91m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

# --- 카드 클래스 ---
class TrumpCard:
    SHAPES = ['♠️', '♥️', '♣️', '♦️']
    NUMBERS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    
    def __init__(self, shape, number):
        self.shape = shape
        self.number = number
        self.power = self.NUMBERS.index(number)

    def __str__(self):
        text = f"[{self.shape}{self.number}]"
        if self.shape in ['♥️', '♦️']:
            return f"{Color.RED}{text}{Color.RESET}"
        return f"{Color.BLUE}{text}{Color.RESET}"

# --- 카드 덱 클래스 ---
class CardPack:
    def __init__(self):
        self.cards = []
        for s in TrumpCard.SHAPES:
            for n in TrumpCard.NUMBERS:
                self.cards.append(TrumpCard(s, n))
        self.shuffle_cards()

    def shuffle_cards(self):
        random.shuffle(self.cards)

    def pick_one(self):
        return self.cards.pop() if self.cards else None

# --- 족보 판독기 ---
class RuleMaster:
    @staticmethod
    def check_score(cards):
        num_list = sorted([c.power for c in cards], reverse=True)
        shape_list = [c.shape for c in cards]
        
        # 숫자 빈도수 체크 (Counter 미사용)
        count_dict = {}
        for n in num_list:
            count_dict[n] = count_dict.get(n, 0) + 1
        
        counts = sorted(count_dict.values(), reverse=True)
        is_flush = (len(set(shape_list)) == 1)
        
        is_straight = False
        if len(set(num_list)) == 5:
            if max(num_list) - min(num_list) == 4:
                is_straight = True
            # A, 2, 3, 4, 5 (Baby Straight) 예외 처리는 생략

        if is_straight and is_flush: return (900, num_list), f"{Color.YELLOW}⚡ 스트레이트 플러시{Color.RESET}"
        if counts == [4, 1]: return (800, num_list), f"{Color.YELLOW}💣 포카드{Color.RESET}"
        if counts == [3, 2]: return (700, num_list), "🏠 풀하우스"
        if is_flush: return (600, num_list), "🌊 플러시"
        if is_straight: return (500, num_list), "📏 스트레이트"
        if counts == [3, 1, 1]: return (400, num_list), "트리플"
        if counts == [2, 2, 1]: return (300, num_list), "투 페어"
        if counts == [2, 1, 1, 1]: return (200, num_list), "원 페어"
        return (100, num_list), "하이 카드"

# --- 게이머 클래스 ---
class Gamer:
    def __init__(self, nickname, start_gold=1000):
        self.nickname = nickname
        self.my_cards = []
        self.gold = start_gold

    def get_card(self, pack, count=1):
        for _ in range(count):
            self.my_cards.append(pack.pick_one())

    def show(self):
        card_str = " ".join(map(str, self.my_cards))
        return f"{self.nickname} 패: {card_str}"

    def sort_cards(self):
        self.my_cards.sort(key=lambda x: x.power)

# --- 메인 게임 엔진 ---
class PokerApp:
    RECORD_DIR = "game_records"
    RECORD_FILE = "history.txt"

    def __init__(self):
        self.pack = None
        self.me = Gamer(f"{Color.GREEN}나(User){Color.RESET}", 1000)
        self.com = Gamer("알파고", 1000)
        self.pot_money = 0
        
        # 기록용 폴더 자동 생성
        if not os.path.exists(self.RECORD_DIR):
            os.makedirs(self.RECORD_DIR)
            print(f"📂 기록 저장을 위한 '{self.RECORD_DIR}' 폴더가 생성되었습니다.")

    def write_history(self, winner_name, win_amount):
        """결과를 텍스트 파일에 이어쓰기(append)"""
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        path = os.path.join(self.RECORD_DIR, self.RECORD_FILE)
        
        log_line = f"[{now}] 승리: {winner_name:<8} | 획득: {win_amount:>4}원 | 내 잔액: {self.me.gold}원\n"
        
        try:
            with open(path, "a", encoding="utf-8") as f:
                f.write(log_line)
        except Exception as e:
            print(f"기록 저장 실패: {e}")

    def start_round(self):
        print("\n" + "="*45)
        print(f"      🎲 {Color.BOLD}PYTHON POKER GAME{Color.RESET} 🎲")
        print("="*45)
        
        self.pack = CardPack()
        self.me.my_cards = []
        self.com.my_cards = []
        self.pot_money = 0
        
        # 카드 5장씩 분배
        self.me.get_card(self.pack, 5)
        self.com.get_card(self.pack, 5)
        self.me.sort_cards()
        
        # 참가비
        fee = 50
        if self.me.gold < fee:
            print("잔액이 부족합니다. 게임 오버!")
            return False

        self.me.gold -= fee
        self.com.gold -= fee
        self.pot_money += (fee * 2)
        print(f"💰 참가비 {fee}원을 냈습니다. (현재 판돈: {self.pot_money})")

        # 내 패 보여주기
        print(f"\n{self.me.show()}")
        
        # 플레이어 카드 교환
        print("\n[ 카드 교환 ]")
        change_input = input("바꿀 순서 입력 (예: 1 3 / 엔터=패스): ")
        
        if len(change_input.strip()) > 0:
            try:
                idx_list = sorted([int(x) for x in change_input.split()], reverse=True)
                count = 0
                for i in idx_list:
                    if 1 <= i <= 5:
                        self.me.my_cards.pop(i-1)
                        count += 1
                self.me.get_card(self.pack, count)
                self.me.sort_cards()
                print(f"🔄 {count}장 교환 완료! \n{self.me.show()}")
            except ValueError:
                print("잘못 입력해서 넘어갑니다.")

        # 컴퓨터 AI (단순 랜덤)
        time.sleep(0.5)
        if random.randint(0, 1) == 1:
            self.com.my_cards.pop()
            self.com.get_card(self.pack, 1)
            print("\n🤖 알파고가 카드를 한 장 바꿨습니다.")
        else:
            print("\n🤖 알파고: '패가 좋군. 바꾸지 않겠다.'")

        # 결과 확인
        print("\n" + "-"*45)
        input("결과를 보려면 엔터(Enter)...")
        
        my_score, my_msg = RuleMaster.check_score(self.me.my_cards)
        com_score, com_msg = RuleMaster.check_score(self.com.my_cards)

        print(f"\n😎 나     : {self.me.show()} -> {my_msg}")
        print(f"🤖 알파고 : {com_msg} (패 비공개)") # 컴퓨터 패는 족보만 공개하는 게 일반적이나 여기선 편의상 생략

        # 승패 판정
        winner = "무승부"
        win_money = 0
        
        if my_score > com_score:
            print(f"\n🎉 {Color.YELLOW}승리! {self.pot_money}원을 획득했습니다!{Color.RESET}")
            self.me.gold += self.pot_money
            winner = "User"
            win_money = self.pot_money
        elif my_score < com_score:
            print(f"\n😭 {Color.RED}패배... 알파고가 돈을 가져갑니다.{Color.RESET}")
            self.com.gold += self.pot_money
            winner = "Computer"
            win_money = self.pot_money
        else:
            print("\n🤝 비겼습니다. 판돈을 나눕니다.")
            half = self.pot_money // 2
            self.me.gold += half
            self.com.gold += half
            winner = "Draw"
            win_money = half

        # 기록 저장
        self.write_history(winner, win_money)
        return True

    def main_loop(self):
        while True:
            if self.me.gold <= 0:
                print(f"\n{Color.RED}💸 파산했습니다...{Color.RESET}")
                break
                
            if not self.start_round():
                break

            print(f"\n[ 현재 잔액: {self.me.gold}원 ]")
            check = input("한 판 더? (y/n): ")
            if check.lower() != 'y':
                print("게임을 종료합니다.")
                break

if __name__ == "__main__":
    app = PokerApp()
    app.main_loop()

