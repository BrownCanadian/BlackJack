

#list with suits and another list with cards and then a for loop to create a full deck.
import random


cards_in_deck=52
def create_deck():

    card_values= ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    card_suits=['♥','♠','♦','♣']
    card_deck=[]
    for suit in card_suits:
        for num in card_values:
            card= suit+num
            card_deck.append(card)
    return card_deck

#fucntion to make a bet

def place_bet():
    bet= (input("Place a bet between $2 to $500:  "))
    while bet.isdigit()==False or int(bet)>500 :
        bet= (input("Bet is Illegal, Place a bet between $2 to $500:  "))


    total_bet=int(bet)   
    print("You have now placed an bet of : $",bet)
    add_bet =input("This is the final bet before the start of the play, if you want to add anything to the bet,you can add by pressing Y. if not, press N:  ")
    if add_bet == 'Y' or add_bet == 'y':
        a_bet= int(input("add a bet:  "))
        total_bet=int(bet)+a_bet
    
    print("Your final bet is of: $", total_bet)
    return total_bet


def card_generate():
    global cards_in_deck
    all_cards = create_deck()
    number = random.randint(0,cards_in_deck)
    cards_in_deck-=1
    card= all_cards[number]
   
    all_cards.remove(card)
    
    return card

def dealing():
    
    
    player_cards=[card_generate(),card_generate()]
    dealers_cards=[card_generate(),'▮ ']
    print("Dealers hand: ",dealers_cards)
    
    # print("Player hand: ",player_cards)
    return [player_cards,dealers_cards]

def hit():
    bet = place_bet()
    win= bet*2
    tie = bet
    final_player = 0
    final_dealer = 0
    table_cards= dealing()
    p_cards = table_cards[0]
    dealers_cards= table_cards[1]
    total=0
    while True:
        total_a1=0
        total_a2 = 0
        for card in p_cards:
            
            number = (card[1:])
            
            if number not in 'AQJK':
                total_a1+= int(number)
                total_a2+= int(number)
            elif number in 'QJK':
                total_a1+=10
                total_a2+=10
            elif number=='A' and total_a1<=10:
               
                total_a1= total_a1+1
                total_a2= total_a2+1
                total_a2=total_a2+11
                total_a1=total_a1+11
            elif number =='A' and total_a1>10:
                
                total_a1= total+1
       
        print("Players hand: ", p_cards)

        if total_a1>21 and total_a2>21:
            print("You got Busted!!!")
            break
        hit = input("Press H to hit or S to stay: ")
        if total_a1<21 and total_a1>total_a2:
            final_player =  total_a1
        else:
            final_player = total_a2
        if hit=='S' or hit =='s':
            
            x=False
            dealers_cards.pop()
            while x==False:
                total_1=0
                total_2=0
                for card in dealers_cards:
                    
                    number = (card[1:])
                    
                    if number not in 'AQJK':
                        total_1+= int(number)
                        total_2+= int(number)
                    elif number in 'QJK':
                        total_1+=10
                        total_2+=10
                    elif number=='A' and total_1<=10:
                    
                        total_1= total_1+1
                        total_2= total_2+1
                        total_2=total_2+11
                        total_1=total_1+11
                    elif number =='A' and total_1>10:
                        
                        total_1= total+1
                print("Dealers Hand: ", dealers_cards)

                
                if total_1<21 and total_1>total_2:
                        final_dealer = total_1
                else:
                    final_dealer = total_2
                if total_1 < 16 or total_2<16:
                    dealers_cards.append(card_generate())
                elif total_1>21 and total_2>21:
                    
                    print("Dealer got busted! You Win!!!")
                    print(" You Credit: $",win)
                    x=True
                else:

                    if final_dealer> final_player:
                        print("You lost the bet, maybe try again")
                    elif final_dealer==final_player:
                        print("Its a tie! Nice game")
                        print("You Credit: $",tie)
                    else:
                        print("You won!!! Congrats")
                        print(" You Credit: $",win)

                    
                    
                    x=True


                 
            # total_1=0
            # total_2=0
            # while True:
            #     total_1=0
            #     total_2=0
                
            #     for cards in dealers_cards:
                    
            #         number= cards[1:]
            #         if number not in 'AJQK':
            #             total_1+=int(number)
            #             total_2+=int(number)
            #         if number in 'JQK':
            #             total_1+=10
            #             total_2+=10
            #         if number == 'A':
            #             total_1+=1
            #             total_2+=11
            #     if total_1>16 or total_2>16:
            #         break
            # print('Dealers : ',total_1, total_2)
            

            break
            # to do: if stay, start appending dealers hand to check if over 21 or under
            
        else:
            p_cards.append(card_generate())


    # add a fucntion called end that ends the
    # game and prompts user to play again or not end()




    




def main_game():
    create_deck()
    # place_bet()
    hit()
    # dtsrt_screen()
    # making the deck()
    #Placing the bets()
    # Dealing cards
    # Hitting or not for Player
    # Hitting or not for dealer
    # Result of main
    #play again function or End screen
main_game()