import random
def card_deal():
    cards= [11,2,3,4,5,6,7,8,9,10,10,10,10]

    card = random.choice(cards)
    return card
def compare(user_score,computer_score):
    if computer_score > 21 and user_score > 21 :
        return "you lose"
    if computer_score ==  user_score:
        return "draw"
    elif user_score==0:
        return "you won we got the black jack situation"   
    elif computer_score==0:
        return "you lose computer got the blackjack"    
    elif user_score > 21:
        return "you lose"
    elif computer_score > 21:
        return "you won"
    elif user_score > computer_score:
        return "you won"    
    else:
        return "you lose"    



def caluculate(cards):
    if sum(cards) == 21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)         


def game():
    user_cards = []
    computer_cards=[]

    game_end= False

    for _ in range(2):
        user_cards.append(card_deal())
        computer_cards.append(card_deal())

    while not game_end :    

        user_score= caluculate(user_cards)
        computer_score = caluculate(computer_cards)    
        print(f"{user_cards} : {user_score}")
        print(f"{computer_cards},X")

        if user_score==0 or computer_score == 0 or user_score> 21 :
            game_end = True

        else:
            user_score < 21 
            draw_deal = input("do you want to draw another card type y  or just want to compare than n : ")
            if draw_deal == "y":
                user_cards.append(card_deal())
                user_score= caluculate(user_cards)
            else:
                game_end= True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(card_deal())    
        computer_score = caluculate(computer_cards)
        print(f"{user_cards} : {user_score}")
        print(f"{computer_cards} : {computer_score}")

        print(compare(user_score,computer_score))

while input("do you want to play y or n")=="y":
    game()        


        