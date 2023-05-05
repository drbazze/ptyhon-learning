import os
import random
from prettytable import PrettyTable

class BlackJack():
    def __init__(self):
        self.computer_deal_threshold_score = 17
        self.user_cards = []
        self.computer_cards = []
        self.leader_board = {
            "user": 0,
            "computer": 0
        }
        self.ui_leader_board_table = PrettyTable(["Player", "Score"])

        self.logo = """
                    .------.            _     _            _    _            _    
                    |A_  _ |.          | |   | |          | |  (_)          | |   
                    |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
                    | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
                    |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
                    `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
                        |  \/ K|                            _/ |                
                        `------'                           |__/           
                    """        

    def deal_cards(self):
        return random.choice([11,2,3,4,6,7,8,9,10,10,10,10])
    
    def calculate_score(self, cards):
        if len(cards) == 2 and sum(cards) == 21: 
            return 0
        #If there is an ACE and the sum is higher then 21 than the ACE count 1 instead of 11
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)
    
    def update_leader_board(self, winner):
        if winner == "both":
            self.leader_board["user"] += 1
            self.leader_board["computer"] += 1        
        else:
            self.leader_board[winner] += 1
    
    def compare_scores(self, user_score, computer_score):
        result = ""
        winner = ""

        if user_score == computer_score:
            result = "Draw 🙃"
            winner = "both"
        elif computer_score == 0:
            result = "Lose, opponent has Blackjack 😱"
            winner = "computer"
        elif user_score == 0:
            result = "Win with a Blackjack 😎"
            winner = "user"
        elif user_score > 21:
            result = "You went over. You lose 😭"
            winner = "computer"
        elif computer_score > 21:
            result = "Opponent went over. You win 😁"
            winner = "user"
        elif user_score > computer_score:
            result = "You win 😃"
            winner = "user"
        else:
            result = "You lose 😤"
            winner = "computer"
        self.update_leader_board(winner)

        print(result)
    
    def show_leader_board(self):
        print("""Leaderboard:
        """)
        #Sort the leader board
        board = sorted(self.leader_board.items(), key=lambda item: item[1], reverse=True)

        for item in board:
            self.ui_leader_board_table.add_row([item[0], item[1]])

        print(self.ui_leader_board_table)
        
    def play(self):
        self.user_cards = []
        self.computer_cards = []
        is_user_turn_over = False
        
        os.system('clear')
        print(self.logo)
        self.ui_leader_board_table.clear_rows()
        
        for _ in range(2):
            self.user_cards.append(self.deal_cards())
            self.computer_cards.append(self.deal_cards())
  
        while not is_user_turn_over:
            user_score = self.calculate_score(self.user_cards)
            computer_score = self.calculate_score(self.computer_cards)

            print(f'''
            Your cards: {self.user_cards}, current score: {user_score}
            Computer's first card: {self.computer_cards[0]}
            ''')

            #If the user or the computer got blackjack or the use went over
            if user_score == 0 or computer_score == 0 or user_score > 21:
                is_user_turn_over = True
            else:
                another_card = input("Type 'y' to get another card, type 'n' to pass: ")
                if another_card == "y":
                    self.user_cards.append(self.deal_cards())
                else:
                    is_user_turn_over = True
        #If the user has already over 21 then no need to deal for the computer
        #If the comp is under the threshold deal
        while user_score < 21 and computer_score != 0 and computer_score < self.computer_deal_threshold_score:
            self.computer_cards.append(self.deal_cards())
            computer_score = self.calculate_score(self.computer_cards)  

        print(f'''
        Your final hand: {self.user_cards}, final score: {user_score}
        Computer's final hand: {self.computer_cards}, final score: {computer_score}
        ''')
        self.compare_scores(user_score, computer_score)
        print("-"*60)
        self.show_leader_board()
        print("-"*60)

if __name__ == "__main__":
    blackjack = BlackJack()
    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        blackjack.play()