from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = 'c545bc87620d4ced81cbddb8a90b4a51'
__human_name__ = 'for'


#""" Your code here. """
def shortest_names(landen):
    lengte = []
    for land in landen:
        naam = len(land)
        lengte = lengte + [len(land)]
        print(lengte)
    kort = min(lengte)
    kortste_landen = []
    for land in landen:
        if len(land) == kort:
            kortste_landen = kortste_landen + [land]
    return kortste_landen

def most_vowels(landen):
    vowels = 'aeiouAEIOU'
    ranking = []
    result_list = []
    for land in landen:
        count = 0
        for i in land:  
            if i in vowels:
                count = count + 1
        ranking = ranking + [count] #score berekenen voor alle landen

    for i in range(3): #maakt een top3
        hoogste = max(ranking) # haalt hoogste waarde uit de lijst
        aantal = ranking.count(hoogste) #bepaalt hoe vaak deze waarde voorkomt.
        for n in range(aantal): #herhaalt dit hoe vaak die waarde voorkomt
            winnaar = ranking.index(hoogste) #hiermee bepaal je de plaats in de lijst van de hoogste score
            land_1= landen[winnaar] # het land met de hoogste score
            result_list = result_list + [land_1] #voegt het land toe aan de string
            ranking[winnaar] = 0 #zet de waarde van de hoogste op 0 waardoor een andere de hoogste wordt
            landen[winnaar] = 0 #idem
    return result_list

def alphabet_set(landen):
    landen_sorted = sorted(landen, key=str.lower)
    landen_sorted = sorted(landen_sorted, key=len, reverse=True)
    alfabet = list('abcdefghijklmnopqrstuvwxyz')
    uitkomst = []
    for land in (landen_sorted):
        uitkomst = uitkomst + [land]
        for i in (alfabet):
            werk = str(uitkomst)
            doorgaan = True if i in alfabet and i not in werk else False
            if doorgaan == True:
               break
        if doorgaan == False:
            break
    return uitkomst


# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == '__main__':
    countries = get_countries()
    
