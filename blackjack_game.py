import random

def blackjack(Dealer_Cards, Player_Cards, Total_Player, Total_Dealer):
    Dealer_Cards = []
    Player_Cards = []
    Total_Player = 0
    Total_Dealer = 0
    # Deal the cards
    # Dealer Cards
    while len(Dealer_Cards) != 2:
        Dealer_Cards.append(random.randint(1, 11))
        if len(Dealer_Cards) == 2:
            print("Dealer has ", Dealer_Cards)

    # Player Cards
    while len(Player_Cards) != 2:
        Player_Cards.append(random.randint(1, 11))
        if len(Player_Cards) == 2:
            print("You have ", Player_Cards)
            print("you have 2 option Hit or Stay:[Click '1' for Hit and if you want to Stay click '0']:")
            option = int(input(""))
            if option == 0:
                Total_Dealer += sum(Dealer_Cards)  # Dealer_Cards= i
                print("sum of the Dealer cards:", Total_Dealer)
                Total_Player += sum(Player_Cards)  # Player_Cards= x
                print("sum of the Player cards:", Total_Player)

                if Total_Dealer > Total_Player:
                    print("Dealer Wons")
                    break
                elif Total_Player > Total_Dealer:
                    print("You Won")
                    break
                else:
                    print("Scoreless.")
                    break

            elif option == 1:
                while len(Player_Cards) != 3:
                    Player_Cards.append(random.randint(1, 11))
                    Dealer_Cards.append(random.randint(1, 11))
            if len(Player_Cards) == 3:
                print("You have ", Player_Cards)
                print("you have 2 option Hit or Stay:[Click '1' for Stay and if you want to Stay click '0']")
                option = int(input(""))
                if option == 0:
                    Total_Dealer += sum(Dealer_Cards)
                    print("sum of the Dealer cards:", Total_Dealer)
                    Total_Player += sum(Player_Cards)
                    print("sum of the Player cards:", Total_Player)

                    if Total_Player > 21 and Total_Dealer <= 21:
                        print("You are BUSTED !")
                        break
                    elif Total_Player == Total_Dealer:
                        print("Scoreless")
                        break
                    elif Total_Player <= 21 and Total_Dealer > 21:
                        print("You WON !")
                        break
                    elif (Total_Player < 21 and Total_Dealer < 21) and (Total_Player > Total_Dealer):
                        print("You WON !")
                    elif (Total_Player < 21 and Total_Dealer < 21) and (Total_Dealer > Total_Player):
                        print("Dealer WON !")
                        break
                elif option == 1:
                    while len(Player_Cards) != 4:
                        Player_Cards.append(random.randint(1, 11))
                        Dealer_Cards.append(random.randint(1, 11))
            if len(Player_Cards) == 4:
                print("You have ", Player_Cards)
                print("you have 2 option Hit or Stay:[Click '1' for Stay and if you want to Stay click '0']")
                option = int(input(""))
                if option == 0:
                    Total_Dealer += sum(Dealer_Cards)
                    print("sum of the Dealer cards:", Total_Dealer)
                    Total_Player += sum(Player_Cards)
                    print("sum of the Player cards:", Total_Player)

                    if Total_Player > 21 and Total_Dealer <= 21:
                        print("You are BUSTED !")
                        break
                    elif Total_Player == Total_Dealer:
                        print("Scoreless")
                        break
                    elif Total_Player <= 21 and Total_Dealer > 21:
                        print("You WON !")
                        break
                    elif (Total_Player < 21 and Total_Dealer < 21) and (Total_Player > Total_Dealer):
                        print("You WON !")
                        break
                    elif (Total_Player < 21 and Total_Dealer < 21) and (Total_Dealer > Total_Player):
                        print("Dealer WON !")
                        break
                elif option == 1:
                    while len(Player_Cards) != 5:
                        Player_Cards.append(random.randint(1, 11))
                        Dealer_Cards.append(random.randint(1, 11))
                        if len(Player_Cards) == 5:
                            print("You have ", Player_Cards)
                            Total_Dealer += sum(Dealer_Cards)
                            print("sum of the Dealer cards:", Total_Dealer)
                            Total_Player += sum(Player_Cards)
                            print("sum of the Player cards:", Total_Player)
                            if Total_Player > 21 and Total_Dealer <= 21:
                                print("You are BUSTED !")
                                break
                            elif Total_Player == Total_Dealer:
                                print("Scoreless")
                                break
                            elif Total_Player <= 21 and Total_Dealer > 21:
                                print("You WON !")
                                break
                            elif (Total_Player < 21 and Total_Dealer < 21) and (Total_Player > Total_Dealer):
                                print("You WON !")
                                break
                            elif (Total_Player < 21 and Total_Dealer < 21) and (Total_Dealer > Total_Player):
                                print("Dealer WON !")
                                break
blackjack([3,7],[1,11], 5, 12)
