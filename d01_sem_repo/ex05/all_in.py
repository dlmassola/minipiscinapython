import sys

def searchStateOrCapital():
    if (len(sys.argv) != 2):
        return

    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
        }

    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
        }
    
    inv_states = dict(map(reversed, states.items())) 

    inv_capital_cities = dict(map(reversed, capital_cities.items())) 

    words = sys.argv[1].split(",")
    for word in words:
        word = word.strip(" ")

        if word != "":
            state = isCapital(word.title(), inv_states, inv_capital_cities)
            capital = isState(word.title(), states, capital_cities)
            capitalS = isCapitalS(word.upper(), capital_cities)

            if state != "":
                print(word, "is the capital of", state)
            elif capital != "":
                print(capital, "is the capital of", word)
            elif capitalS != "":
                print(capitalS, "is the capital of", word)
            else:
                print(word, "is neither a capital city nor a state")

def isCapital(capital, states, capital_cities):
    state = ""

    if capital_cities.get(capital):
        sigla = capital_cities[capital]
        if states.get(sigla):
            state = states[sigla]

    return state

def isCapitalS(state, capital_cities):
    capital = ""
    
    if capital_cities.get(state):
        capital = capital_cities[state]

    return capital

def isState(state, states, capital_cities):
    capital = ""

    if states.get(state):
        sigla = states[state]
        if capital_cities.get(sigla):
            capital = capital_cities[sigla]

    return capital

if __name__ == '__main__':
    searchStateOrCapital()