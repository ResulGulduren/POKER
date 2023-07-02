players_cards={'P1': ['10H', 'JH'], 'P2': ['3D', 'AS'], 'P3': ['JC', '5H'], 'P4': ['3D', '3S'], 'P5': ['6D', '8H'], 'P6': ['5D', '10S']}
comunity_cards=['JD', '10C', '10D', 'KH', '3H']
player_control_dic={}
winner_list=[]
values={}
def result_card_dic():
    for i,j in players_cards.items():
            a=[]
            a.extend(j)
            a.extend(comunity_cards)
            player_control_dic[i]=a
    return player_control_dic

def values_of_cards():
    for player,cards in player_control_dic.items():
        list_of_values=[]
        for card in cards:
            n = card[:-1]
            if n == "A":
                n = 14
            elif n == "K":
                n = 13                
            elif n == "Q":
                n = 12            
            elif n == "J":
                n = 11
            else:
                n = int(n)
            list_of_values.append(n)    
        list_of_values.sort(reverse=True)
        values[player]=sorted(list_of_values,reverse=True)     
    return values

def full_house():
    result_card_dic()
    values_of_cards()   
    pairs = {}
    final_winner={}
    for player,cards in values.items():
        triple = []
        double=[]
        for card in cards:
            count=cards.count(card)
            if count ==3:
                if card not in triple:
                    triple.append(card)
            if count ==2:
                if card not in double:
                    double.append(card) 
        if len(triple) ==1 and len(double) !=0:
            triple.append(double[0])
            pairs[player]=triple    
        elif len(triple)==2:
            pairs[player]=triple
    max_values =max(pairs.values())
    
    for player,cards in pairs.items():
        if cards[:2] == max_values[:2]:
          final_winner[player]=cards        
    if len(final_winner) > 1:
      return f"Winners {final_winner}"
    
    else: 
      return f" Winner  {final_winner}"
  
sonuc=full_house()
print(sonuc)
